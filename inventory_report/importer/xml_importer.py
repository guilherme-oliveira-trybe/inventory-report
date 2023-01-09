from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith(".xml"):
            with open(file_name) as data:
                data_reader = xmltodict.parse(data.read())["dataset"]["record"]
                return list(data_reader)
        raise ValueError("Arquivo inválido")
