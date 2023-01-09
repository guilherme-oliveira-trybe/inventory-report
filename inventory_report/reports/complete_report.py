from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report):
        simple_report = super().generate(report)
        all_companies = cls.counter_products(report)
        complete_report = simple_report + "\nProdutos estocados por empresa:\n"
        for company, quantity in all_companies.items():
            complete_report += f"- {company}: {quantity}\n"

        return complete_report
