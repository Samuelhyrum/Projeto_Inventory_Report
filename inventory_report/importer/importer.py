from abc import ABC


class Importer(ABC):
    @classmethod
    def import_data(cls, path):
        raise NotImplementedError
