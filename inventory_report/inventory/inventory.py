from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:

    File_path = {
        "inventory_report/data/inventory.csv": CsvImporter.import_data,
        "inventory_report/data/inventory.json": JsonImporter.import_data,
        "inventory_report/data/inventory.xml": XmlImporter.import_data,
    }

    REPORTS = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    @classmethod
    def import_data(cls, path, type):
        lista = cls.File_path[path](path)
        return cls.REPORTS[type](lista)
