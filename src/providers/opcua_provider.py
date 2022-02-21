from src.models.variable import Variable
from src.services.config import Config
from opcua import Client

class OpcuaProvider:
  def __init__(self, config: Config) -> None:
      self.config = config
      self.client = Client(self.config.opc_url)
      self.client.connect()

  def get_value_of(self, variable: Variable):
    value = self.client.get_node(variable.node_id).get_value()
    return value