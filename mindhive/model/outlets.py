from marshmallow import Schema, fields, post_load
from flask_sqlalchemy import SQLAlchemy
from typing import List


# names, addresses, operating hours, waze link of outlets
class Outlet(object):
    def __init__(self, name, add_info, waze, latitude, longitude):
        self.name = name
        self.add_info: List[str] = add_info
        self.waze = waze
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self) -> str:
        return "<Outlet(name={self.name!r})>".format(self=self)


class OutletSchema(Schema):
    name = fields.Str()
    add_info = fields.List(fields.Str())
    # add_info = fields.Str()
    waze = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()

    # @post_load
    # def make_outlet(self, data, **kwargs):
    #     return Outlet(**data)

    def load(self, data, *args, **kwargs):
        if "add_info" in data:
            data["add_info"] = ";".join(str(e) for e in data["add_info"])
        return super().load(data, *args, **kwargs)

    def dump(self, data, *args, **kwargs):
        # print(data[0])
        # print("in dump")
        # if "add_info" in data:
        #     data["add_info"] = [data["add_info"].split(";")]
        # print("in add infor")
        # print("DATA---------------------------------------")
        # print(data["add_info"])
        return super().dump(data, *args, **kwargs)
