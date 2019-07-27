from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
    "host": '192.168.161.15', 
    "username": 'pi', 
    "password": getpass(), 
    "device_type": 'cisco_ios',
 #   "session_log": 'my_session.txt',
}


net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip interface brief", use_genie=True)
pprint(output)

net_connect.disconnect()
