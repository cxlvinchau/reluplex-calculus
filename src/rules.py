import abc
from abc import ABC

from configuration import ReluplexConfiguration


class Rule(ABC):

    @abc.abstractmethod
    def is_applicable(self, configuration: ReluplexConfiguration):
        pass

    @abc.abstractmethod
    def get_results(self, configuration: ReluplexConfiguration):
        pass