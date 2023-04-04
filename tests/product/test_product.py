from inventory_report.inventory.product import Product


def test_cria_produto():
    returnAssert = [
        "O produto CADEIRA fabricado em 2022-04-04 por Forces of Nature "
        "com validade até 2023-02-09"
        "precisa ser armazenado Conservar em local fresco."
        ]
    assert Product(
        '1', 'CADEIRA', 'Forces of Nature', '2022-04-04', '2023-02-09', "FR48",
        'Conservar em local fresco'
        ) == returnAssert
