from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": '192.168.161.15', 
    "username": 'pi', 
    "use_keys": True,
    "key_file": "/Users/pi/.ssh/id_rsa", 
    "device_type": 'cisco_ios',
 #   "session_log": 'my_session.txt',
}


net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip int brief")
print(output)

net_connect.disconnect()
