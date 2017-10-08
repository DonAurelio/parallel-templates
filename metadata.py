# -*- encoding: utf-8 -*-

import os
import yaml
import settings
import shutil


class CAFile(object):

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

        cafile_path = os.path.join(dir_path,settings.CAFILE_NAME)
        with open(cafile_path) as cafile:
            #: dict: A dictionary containing the cafile.yml data
            self._data = yaml.load(cafile)
            #: str: The location to the directory containing the cafile.yml loaded
            self._dir_path = dir_path

    @property
    def data(self):
        """Returns a dict with the cafile object data."""
        return self._data

    def __str__(self):
        """Returns a string with the cafile object data."""
        raw = 'Directory: %s \nData: \n%s'
        return raw % (self._dir_path,str(self._data))