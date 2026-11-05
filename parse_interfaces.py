router={
  "ietf-interfaces:interfaces": {
    "interface": [
      {
        "name": "GigabitEthernet1",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "192.168.56.101",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      }
    ]
  }
}

print(router["ietf-interfaces:interfaces"]["interface"][0]["enabled"])

