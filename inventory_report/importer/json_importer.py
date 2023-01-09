from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith(".json"):
            with open(file_name) as data:
                data_reader = json.load(data)
                return list(data_reader)
        raise ValueError("Arquivo inválido")
