from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith(".csv"):
            with open(file_name) as data:
                data_reader = csv.DictReader(data)
                return list(data_reader)
        raise ValueError("Arquivo inválido")
