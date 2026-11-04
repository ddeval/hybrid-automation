router={
  "ietf-interfaces:interfaces": {
    "interface": [
      {"name": "GigabitEthernet1"},
      {"name": "GigabitEthernet2"}
    ]
  }
}

for interface in router["ietf-interfaces:interfaces"]["interface"]:
    print(interface["name"])