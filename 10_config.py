from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": '192.168.161.15', 
    "username": 'pi', 
    "password": getpass(), 
    "device_type": 'cisco_ios',
 #   "session_log": 'my_session.txt',
}


net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())


cfg = 'logging buffered 20000'


output = net_connect.send_config_set(cfg)
print(output)

net_connect.disconnect()
