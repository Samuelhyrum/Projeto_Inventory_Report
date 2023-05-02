from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.xml'):
            with open(path, "r", encoding="utf8") as file:
                tree = ET.parse(file)
                root = tree.getroot()

            lista_xml = []
            for item in root.findall("record"):
                key_value = {}
                for child in item:
                    key_value[child.tag] = child.text
                lista_xml.append(key_value)

            return lista_xml

        else:
            raise ValueError("Arquivo inválido")
