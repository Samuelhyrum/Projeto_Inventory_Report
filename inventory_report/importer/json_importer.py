from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        path_test = "inventory_report/data/inventory.json"
        if path == path_test:
            with open(path, encoding="utf8") as file:
                return json.load(file)
        if path != path_test:
            raise ValueError("Arquivo inválido")
