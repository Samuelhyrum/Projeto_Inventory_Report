from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:

    REPORTS = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    @classmethod
    def import_data(cls, path, type):
        with open(path, encoding="utf8") as file:
            all_file = csv.DictReader(file, delimiter=",", quotechar='"')
            lista = list(all_file)

            return cls.REPORTS[type](lista)
