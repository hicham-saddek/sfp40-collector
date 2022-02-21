from datetime import datetime
from src.models.variable import Variable
from src.services.config import Config
import requests

class Api:
  def __init__(self, config: Config):
    self.config = config
  
  @property
  def headers(self):
    return {"Accept": "application/json", "Content-type": "application/json"}

  @staticmethod
  def response_good(response):
    return response.status_code >= 200 and response.status_code < 400
  
  @staticmethod
  def response_bad(response):
    return not Api.response_good(response)

  @property
  def watched(self):
    link = f"{self.config.channel_link}/variables/watched"
    print(f"[LOG: ApiProvider] - Using the link {link}")
    response = requests.get(link, headers=self.headers)
    if Api.response_good(response):
      return Variable.from_bulk_json(response.json()['data']['watched'])
    else:
      return []

  def register_data_entry(self, variable: Variable, value: bool):
    link = f"{self.config.channel_link}/variables/{variable.id}/data"
    print(f"[LOG: ApiProvider] - Registering new data entry for (V-{variable.id}, {value}) using ({link})")
    data = {"value": bool(value), "collected_at": datetime.now().isoformat()}
    response = requests.post(link, headers=self.headers, json=data)
    if response.status_code > 400:
      print(response.json()['message'])
    return Api.response_good(response)