"""Module source.py"""
import logging

import datasets

import config


class Interface:
    """
    A class for data preparation.
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

        # The Data
        self.__dataset: datasets.DatasetDict = datasets.load_dataset("DFKI-SLT/few-nerd", "supervised")


        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)


    def exc(self):
        """

        :return:
        """

        # The data segments
        self.__logger.info('The data segments:\n%s', self.__dataset.keys())
