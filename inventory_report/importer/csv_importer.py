from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.csv'):
            with open(path, encoding="utf8") as file:
                return list(csv.DictReader(file, delimiter=",", quotechar='"'))
        else:
            raise ValueError("Arquivo inválido")
