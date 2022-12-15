from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(report):
        today = date.today()
        manufacturing_dates = [item["data_de_fabricacao"] for item in report]
        expiration_date = [
            item["data_de_validade"]
            for item in report
            if item["data_de_validade"] > str(today)
        ]
        all_companies = Counter([item["nome_da_empresa"] for item in report])

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_dates)}\n"
            f"Data de validade mais próxima: {min(expiration_date)}\n"
            f"Empresa com mais produtos: {all_companies.most_common()[0][0]}"
        )


print(
    SimpleReport.generate(
        [
            {
                "id": 1,
                "nome_do_produto": "CADEIRA",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2022-04-04",
                "data_de_validade": "2023-02-09",
                "numero_de_serie": "FR48",
                "instrucoes_de_armazenamento": "Conservar em local fresco",
            },
            {
                "id": 2,
                "nome_do_produto": "CADEIRA",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2022-02-03",
                "data_de_validade": "2023-09-10",
                "numero_de_serie": "FR48",
                "instrucoes_de_armazenamento": "Conservar em local fresco",
            },
        ]
    )
)
