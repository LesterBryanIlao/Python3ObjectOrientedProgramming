from Chapter10.abstractfactory.localize.backends.FRANCE import FranceFormatterFactory
from Chapter10.abstractfactory.localize.backends.USA import USAFormatterFactory


country_code = "US"
factory_map = {"US": USAFormatterFactory, "FR": FranceFormatterFactory}
formatter_factory = factory_map.get(country_code)()
