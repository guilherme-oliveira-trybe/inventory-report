from inventory_report.inventory.product import Product


def test_relatorio_produto():
    report = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        567,
        "ao abrigo de luz",
    )
    expect = (
        "O produto farinha"
        " fabricado em 01-05-2021"
        " por Farinini com validade até 02-06-2023"
        " precisa ser armazenado ao abrigo de luz."
    )
    assert expect == str(report)
