from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:

    File_path = {
        "inventory_report/data/inventory.csv": "csv_import_data",
        "inventory_report/data/inventory.json": "json_import_data",

    }

    REPORTS = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    @classmethod
    def import_data(cls, path, type):
        lista = getattr(cls, cls.File_path[path])(path)
        return cls.REPORTS[type](lista)

    @classmethod
    def csv_import_data(cls, path):
        with open(path, encoding="utf8") as file:
            return list(csv.DictReader(file, delimiter=",", quotechar='"'))

    @classmethod
    def json_import_data(cls, path):
        with open(path, encoding="utf8") as file:
            return json.load(file)
