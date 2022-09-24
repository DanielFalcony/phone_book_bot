import json
import os


def json_Import(filename):
    data = {}
    if (os.stat(filename).st_size != 0):
        with open(filename, "r") as f:
            data = json.load(f)
    return data


def json_Export(filename, data):
    with open(filename, "w+") as f:
        json.dump(data, f)
