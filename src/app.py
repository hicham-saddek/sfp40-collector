from lib2to3.pgen2.token import OP
from src.providers.opcua_provider import OpcuaProvider
from src.providers.api_provider import Api
from src.services.config import Config

class Application:
  def loop(self, api: Api, opcua: OpcuaProvider):
    print(f"[LOG: Application run] - Pulling watched variables from server")
    self.register_variables(api.watched, api, opcua)
    api.config.sleep()

  def run(self):
    print("[LOG: Application boot] - Running application ...")
    config = Config()
    api = Api(config)
    opcua = OpcuaProvider(config)
    while True:
      self.loop(api, opcua)

  def register_variables(self, variables: list, api: Api, opcua: OpcuaProvider):
    for i in range(len(variables)):
      variable = variables[i]
      value = opcua.get_value_of(variable)
      api.register_data_entry(variable, value)