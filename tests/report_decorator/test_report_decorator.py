from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    mock_Input = [
        {
            "id": 1,
            "nome_do_produto": "SOFÁ",
            "nome_da_empresa": "Jhuly's of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-12-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco"
        },
        {
            "id": 2,
            "nome_do_produto": "MESA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-02-06",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "keep close to the sam"
        },
        {
            "id": 3,
            "nome_do_produto": "Gloss",
            "nome_da_empresa": "Jhuly's of Nature",
            "data_de_fabricacao": "2004-06-22",
            "data_de_validade": "2023-02-05",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "keep close to the sam"
        }
    ]
    mock_data = "Data de fabricação mais antiga"
    mock_expire = "Data de validade mais próxima"
    mock_company = "Empresa com mais produtos"

    product_Mock_Colored = ColoredReport(SimpleReport)

    return_Assert = (
        f"\033[32m{mock_data}:\033[0m \033[36m2004-06-22\033[0m\n"
        f"\033[32m{mock_expire}:\033[0m \033[36m2023-12-09\033[0m\n"
        f"\033[32m{mock_company}:\033[0m \033[31mJhuly's of Nature\033[0m"
    )

    assert product_Mock_Colored.generate(mock_Input) == return_Assert
