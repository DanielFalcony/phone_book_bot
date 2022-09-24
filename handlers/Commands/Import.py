from Utils.XmlInOut import xml_Import
from Utils.TxtInOut import txt_Import
from Utils.JsonInOut import json_Import
import os


# TODO 1.обработать исключение при отправке файла неподходящего формата.
# TODO 2. в идеале нужна проверка содержимого файла, чтобы после ипрота получать словарь коррекного вида
def import_any_file(file):
    file_name, file_extention = os.path.splitext(file)
    if file_extention == ".txt":
        return txt_Import(file)
    elif file_extention == ".xml":
        return xml_Import(file)
    elif file_extention == ".json":
        return json_Import(file)

