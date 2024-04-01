from re import DEBUG
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from marshmallow import ValidationError
from flask_sqlalchemy import SQLAlchemy

from model.outlets import Outlet, OutletSchema
from scrape import scrape_subway


app = Flask(__name__, template_folder="frontend", static_folder="static")
api = Api(app)

# TODO: database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///outlets.db"
db = SQLAlchemy(app)
# db.init_app(app)
# print(outlets[:10])


@app.route("/")
def index():
    return render_template("index.html")


class OutletModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    waze = db.Column(db.String, nullable=False)
    add_info = db.Column(db.String)

    def __repr__(self) -> str:
        return f"Outlet(name = {self.name})"

    def save_to_db(self):
        db.session.add(self)
        db.commit()


# with app.app_context():
#     db.create_all()


class OutletResource(Resource):
    def get(self):
        # TODO: db stuff
        # outlet = OutletModel.query.get(id=outlet_id)
        # parser = reqparse.RequestParser()
        # parser.add_argument(
        #     "name", type=str, required=True, help="Name of outlet to search"
        # )
        # args = parser.parse_args()

        outlet_name = request.args.get("name")
        if outlet_name:
            outlet = OutletModel.query.filter(
                OutletModel.name.contains(outlet_name)
            ).first()
            print(outlet)
            if not outlet:
                return {"error": "Outlet not found"}, 404
            schema = OutletSchema()
            print(outlet)
            # if type(outlet) == list:
            #     for o in outlet:
            #         o.add_info = o.add_info.split(";")
            # else:
            outlet.add_info = outlet.add_info.split(";")
            data = schema.dump(outlet)
            return data, 200
        else:
            outlet = OutletModel.query.all()
            for o in outlet:
                o.add_info = o.add_info.split(";")
            schema = OutletSchema(many=True)
            data = schema.dump(outlet)
            return data, 200

    def post(self):
        # try:
        schema = OutletSchema()
        outlet_data = schema.load(self.request.get_json())
        outlet = OutletModel(**outlet_data)
        outlet.save_to_db()
        data = schema.dump(outlet_data)
        return data, 204

    def put(self):
        return

    def delete(self, video_id):
        return

    # except ValidationError as err:
    #     return jsonify({"Error": err.messages}), 404


api.add_resource(OutletResource, "/outlets/")
# api.add_resource(OutletResource, "/outlets")

if __name__ == "__main__":
    # db.create_all(app=app)
    # outlets = scrape_subway()

    app.run(debug=True)
