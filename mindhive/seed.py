from scrape import scrape_subway
from app import app, db, OutletModel
from model.outlets import Outlet, OutletSchema


def main():
    outlet_list = scrape_subway()

    with app.app_context():
        db.drop_all()
        db.create_all()
        for data in outlet_list:
            outlet_data = data
            # print(outlet_data)
            outlet_data["add_info"] = ";".join(e for e in outlet_data["add_info"])
            # print(outlet_data["add_info"])
            outlet = OutletModel(**outlet_data)
            db.session.add(outlet)
        db.session.commit()
        # outlet = OutletModel.query.filter_by(name="Subway Caltex Bandar Jitra").first()
        # print("----------------------------------------")
        # print(outlet.add_info)
    print("seeded")


if __name__ == "__main__":
    main()
