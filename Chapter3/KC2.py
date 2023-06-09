import abc
import uuid


class Vehicle(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def drive(self):
		pass

	@abc.abstractmethod
	def park(self):
		pass

	@classmethod
	def __subclasshook__(cls, SubClass):
		if cls is Vehicle:
			attrs = set(dir(SubClass))
			if set(cls.__abstractmethods__) <= attrs:
				return True
		return NotImplemented


class Jeep:
	def drive(self):
		return f"""You are driving."""

	def park(self):
		return f"""You are parking."""


print(issubclass(Jeep, Vehicle))
