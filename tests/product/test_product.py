from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Iogurte de Morango",
        "Itambé",
        "2022-12-12",
        "2023-05-22",
        "5678",
        "Refrigerado",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Iogurte de Morango"
    assert product.nome_da_empresa == "Itambé"
    assert product.data_de_fabricacao == "2022-12-12"
    assert product.data_de_validade == "2023-05-22"
    assert product.numero_de_serie == "5678"
    assert product.instrucoes_de_armazenamento == "Refrigerado"
