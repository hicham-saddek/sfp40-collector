import json
import requests
from time import sleep

class Config:
  def __init__(self):
    with open('config.json') as file:
      self.raw = json.load(file)
    self.app_key = str(self.raw['key'])
    self.api_url = str(self.raw['api'])
    self.load()

  def load(self):
    link = f"{self.api_url}/channels/configurations/{self.app_key}"
    print(f"[LOG: Config] - Loading configurations from {link}")
    response = requests.get(link, headers={"Accept": "application/json", "Content-Type": "application/json"})
    if response.status_code >= 200 and response.status_code < 400:
      print(f"[LOG: Config] successfuly fetched configurations from main server")
      self.api_raw = response.json()['data']
      self.channel = self.api_raw['channel']
      self.config = self.api_raw['configs']
      self.channel_id = self.channel['id']
      self.clock = int(self.config['clock'])
      self.opc_url = str(self.config['opc'])
    else: 
      raise Exception(f"[ERROR: Config] - Configurations cannot be imported from main server - Bad Response from server")
  
  @property
  def channel_link(self):
    return f"{self.api_url}/channels/{self.channel_id}"
  
  def sleep(self):
    sleep(self.clock)