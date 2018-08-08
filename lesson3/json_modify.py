# coding=utf-8

import json


def json_dumps():
    j = {
        "name": "wanghan",
        "age": 18,
        "sex": "male"
    }

    json_str = json.dumps(j)
    print(json_str)
    print(type(json_str))

    json_data = json.loads(json_str)
    print(json_data)
    print(type(json_data))
    print(json_data.get("name"))


if __name__ == '__main__':
    pass