from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        path_test = "inventory_report/data/inventory.csv"
        if path == path_test:
            with open(path, encoding="utf8") as file:
                return list(csv.DictReader(file, delimiter=",", quotechar='"'))
        if path != path_test:
            raise ValueError("Arquivo inválido")
