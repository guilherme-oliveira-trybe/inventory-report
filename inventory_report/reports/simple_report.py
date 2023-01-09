from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def counter_products(cls, report):
        return Counter([item["nome_da_empresa"] for item in report])

    @classmethod
    def generate(cls, report):
        today = date.today()
        manufacturing_dates = [item["data_de_fabricacao"] for item in report]
        expiration_date = [
            item["data_de_validade"]
            for item in report
            if item["data_de_validade"] > str(today)
        ]
        all_companies = cls.counter_products(report)

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_dates)}\n"
            f"Data de validade mais próxima: {min(expiration_date)}\n"
            f"Empresa com mais produtos: {all_companies.most_common()[0][0]}"
        )
