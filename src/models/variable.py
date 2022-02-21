from opcua import Client
import requests


class Variable:
  def __init__(self, id, namespace, identifier):
    self.id = int(id)
    self.namespace = int(namespace)
    self.identifier = int(identifier)

  def from_json(json):
    print(f"[LOG: Models actions] - Model parsed with ({json['id']}, {json['opc_ua_namespace_index']}, {json['opc_ua_identifier']})")
    return Variable(json['id'], json['opc_ua_namespace_index'], json['opc_ua_identifier'])
  
  def from_bulk_json(json):
    variables = []
    for i in range(len(json)):
      variables.append(Variable.from_json(json[i]))
    return variables

  def __str__(self) -> str:
      return f"OPC-UA Variable {self.id} of ({self.namespace}, {self.identifier})"

  @property
  def node_id(self):
    return f"ns={self.namespace};i={self.identifier}"

  def register(self):
    pass

  def process(self, client: Client, config: dict):
    self.client = client
    self.config = config
    return client.get_node(self.node_id)