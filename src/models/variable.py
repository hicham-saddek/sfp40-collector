from opcua import Client
import requests


class Variable:
  def __init__(self, id, nodeid):
    self.id = int(id)
    self.nodeid = str(nodeid)

  def from_json(json):
    print(f"[LOG: Models actions] - Model parsed with ({json['id']}, {json['node_id']})")
    return Variable(json['id'], json['node_id'])
  
  def from_bulk_json(json):
    variables = []
    for i in range(len(json)):
      variables.append(Variable.from_json(json[i]))
    return variables

  def __str__(self) -> str:
      return f"OPC-UA Variable {self.id} of {self.nodeid})"

  @property
  def node_id(self):
    return self.nodeid

  def register(self):
    pass

  def process(self, client: Client, config: dict):
    self.client = client
    self.config = config
    return client.get_node(self.node_id)