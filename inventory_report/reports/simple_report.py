from datetime import datetime, date
from collections import Counter


class SimpleReport:

    @classmethod
    def oldest_manufacture(cls, list):
        manufacture = min([prod["data_de_fabricacao"] for prod in list])
        return manufacture

    @classmethod
    def company_with_more_products(cls, list):
        lista = []
        for company in list:
            lista.append(company["nome_da_empresa"])

        counter = Counter(lista)
        most_common = counter.most_common(1)[0][0]

        return most_common

    @classmethod
    def closest_expiration_date(cls, list):
        test_date = date.today()

        closest = min(
            [
                prod["data_de_validade"]
                for prod in list
                if datetime.strptime
                (prod["data_de_validade"], "%Y-%m-%d").date()
                > test_date
            ]
        )

        return closest

    @classmethod
    def generate(cls, list):
        oldest_product = cls.oldest_manufacture(list)
        most_products = cls.company_with_more_products(list)
        expiration_date = cls.closest_expiration_date(list)
        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {most_products}"
        )
