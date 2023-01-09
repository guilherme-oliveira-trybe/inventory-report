from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, path: str, type_report: str):
        if path.endswith(".csv"):
            return cls.read_csv(path, type_report)
        if path.endswith(".json"):
            return cls.read_json(path, type_report)
        if path.endswith(".xml"):
            return cls.read_xml(path, type_report)

    @classmethod
    def read_csv(cls, path, type_report):
        if type_report == "simples":
            with open(path) as data:
                data_reader = csv.DictReader(data)
                return SimpleReport.generate(list(data_reader))
        else:
            with open(path) as data:
                data_reader = csv.DictReader(data)
                return CompleteReport.generate(list(data_reader))

    @classmethod
    def read_json(cls, path, type_report):
        if type_report == "simples":
            with open(path) as data:
                data_reader = json.load(data)
                return SimpleReport.generate(list(data_reader))
        else:
            with open(path) as data:
                data_reader = json.load(data)
                return CompleteReport.generate(list(data_reader))

    @classmethod
    def read_xml(cls, path, type_report):
        # https://stackoverflow.com/questions/40154727/how-to-use-xmltodict-to-get-items-out-of-an-xml-file
        # https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
        if type_report == "simples":
            with open(path) as data:
                data_reader = xmltodict.parse(data.read())["dataset"]["record"]
                return SimpleReport.generate(list(data_reader))
        else:
            with open(path) as data:
                data_reader = xmltodict.parse(data.read())["dataset"]["record"]
                return CompleteReport.generate(list(data_reader))
