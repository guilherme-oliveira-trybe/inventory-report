from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report):
        simple_report = super().generate(report)
        all_companies = Counter([item["nome_da_empresa"] for item in report])
        complete_report = simple_report + "\nProdutos estocados por empresa:\n"
        for company, quantity in all_companies.items():
            complete_report += f"- {company}: {quantity}\n"

        return complete_report
