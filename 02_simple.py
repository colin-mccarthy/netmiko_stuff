from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    host='192.168.161.15', 
    username='pi', 
    password=getpass(), 
    device_type='cisco_ios',
    session_log='my_session.txt',
)


print(net_connect.find_prompt())
