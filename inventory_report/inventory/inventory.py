from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path: str, type_report: str):
        if type_report == "simples":
            with open(path) as data:
                data_reader = csv.DictReader(
                    data, delimiter=",", quotechar='"'
                )
                return SimpleReport.generate(list(data_reader))
        else:
            with open(path) as data:
                data_reader = csv.DictReader(
                    data, delimiter=",", quotechar='"'
                )
                return CompleteReport.generate(list(data_reader))
