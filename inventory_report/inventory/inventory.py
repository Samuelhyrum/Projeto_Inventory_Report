from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:

    @classmethod
    def import_data(cls, path, type):
        with open(path, encoding="utf8") as file:
            all_file = csv.DictReader(file, delimiter=",", quotechar='"')
            lista = list(all_file)

            if type == "simples":
                return SimpleReport.generate(lista)
            if type == "completo":
                return CompleteReport.generate(lista)
