from inventory_report.reports.simple_report import SimpleReport
import numpy as np


class CompleteReport:

    @classmethod
    def company_with_more_products(cls, list):
        lista = []
        stock = ""
        for company in list:
            lista.append(company["nome_da_empresa"])

        fdist = dict(zip(*np.unique(lista, return_counts=True)))

        for key, value in fdist.items():
            stock += f"- {key}: {value}\n"

        return stock

    @classmethod
    def generate(cls, list):
        simple_rep = SimpleReport.generate(list)
        complete_rep = cls.company_with_more_products(list)
        return (
            f"{simple_rep}\n"
            f"Produtos estocados por empresa:\n"
            f"{complete_rep}"
        )
