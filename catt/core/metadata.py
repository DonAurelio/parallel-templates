# -*- encoding: utf-8 -*-

import os
import yaml
import shutil
from . import settings


class CAFile(object):

    @staticmethod
    def syntax_example():
        """Returns a string with the available syntax for a cafile.yml."""

        cafile_path = settings.CAFILE_PATH
        with open(cafile_path) as cafile:
            return cafile.read()

    @staticmethod
    def create_file(dir_path):
        """Create cafile.

        Creates a cafile.yml file in the given directory.

        Args:
            dir_path (str): path to the directory on which a cafile.yml 
                woul be created.

        Returns:
            A CAFile instance which contains the data of the cafile.yml 
                created in the ``dir_path``.

        """

        file_path = os.path.join(dir_path,settings.CAFILE_NAME)
        cafile_path = settings.CAFILE_PATH
        shutil.copyfile(src=cafile_path,dst=file_path)

        return CAFile(dir_path)

    def __init__(self, dir_path):
        """Cellular automata metadata class.

        A cellular automata specification file decribes the automata 
        to be modeled. A cafile.yml descries aspects like the lattice size, 
        type of the states on the lattice, the neighborhood comunnication 
        pattern, and the númber of generations the cellular automata would 
        evolve.

        Args:
            dir_path (str): An unique location to the dir on which a cafile.yml 
                must exists.

        """

        #: str: The location to the directory containing the cafile.yml loaded
        self._dir_path = dir_path
        #: dict: A dictionary containing the cafile.yml data
        self._data = self.load_file()

    def load_file(self):
        cafile_path = os.path.join(self._dir_path,settings.CAFILE_NAME)
        with open(cafile_path) as cafile:
            return yaml.load(cafile)

    def refresh(self):
        self._data = self.load_file()

    def update(self,data):
        file_path = os.path.join(self._dir_path,settings.CAFILE_NAME)
        with open(file_path,'w') as outfile:
            yaml.dump(data,outfile)
            self.refresh()

    @property
    def data(self):
        """Returns a dict with the cafile object data."""
        return self._data

    @property
    def pattern_name(self):
        return self._data['pattern_name']

    def exists(self):
        file_path = os.path.join(self._dir_path,settings.CAFILE_NAME)
        return os.path.exists(file_path)


    def __str__(self):
        """Returns a string with the cafile object data."""
        raw = 'Directory: %s \nData: \n%s'
        return raw % (self._dir_path,str(self._data))


class Parallel(object):

    