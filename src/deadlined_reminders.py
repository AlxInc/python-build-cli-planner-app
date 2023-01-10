from abc import ABC, ABCMeta, abstractmethod
from _collections_abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    def __iter__(self, text, date):
        formatted_date = self.date.isoformat()
        self.text = iter([text, formatted_date])
    @abstractmethod
    def is_due(self):
        pass



class DeadLinedReminder(Iterable, ABC):
    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DeadLinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self):
        if self.date <= datetime.now():
            pass