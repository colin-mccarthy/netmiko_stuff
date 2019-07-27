

---
![](images/NetDevops.png)
---




source netmiko/bin/activate

pip install netmiko


```
Package      Version
------------ -------
asn1crypto   0.24.0 
bcrypt       3.1.7  
cffi         1.12.3 
cryptography 2.7    
future       0.17.1 
netmiko      2.4.1  
paramiko     2.6.0  
pip          19.0.3 
pycparser    2.19   
PyNaCl       1.3.0  
pyserial     3.4    
scp          0.13.2 
setuptools   40.8.0 
six          1.12.0 
textfsm      1.1.0 
```



currently supported device_types
--------------------------------

```
a10
accedian
alcatel_aos
alcatel_sros
apresia_aeos
arista_eos
aruba_os
avaya_ers
avaya_vsp
brocade_fastiron
brocade_netiron
brocade_nos
brocade_vdx
brocade_vyos
calix_b6
checkpoint_gaia
ciena_saos
cisco_asa
cisco_ios
cisco_nxos
cisco_s300
cisco_tp
cisco_wlc
cisco_xe
cisco_xr
cloudgenix_ion
coriant
dell_dnos9
dell_force10
dell_isilon
dell_os10
dell_os6
dell_os9
dell_powerconnect
eltex
endace
enterasys
extreme
extreme_ers
extreme_exos
extreme_netiron
extreme_nos
extreme_slx
extreme_vdx
extreme_vsp
extreme_wing
f5_linux
f5_ltm
f5_tmsh
flexvnf
fortinet
generic_termserver
hp_comware
hp_procurve
huawei
huawei_vrpv8
ipinfusion_ocnos
juniper
juniper_junos
linux
mellanox
mellanox_mlnxos
mikrotik_routeros
mikrotik_switchos
mrv_lx
mrv_optiswitch
netapp_cdot
netscaler
oneaccess_oneos
ovs_linux
paloalto_panos
pluribus
quanta_mesh
rad_etx
ruckus_fastiron
ubiquiti_edge
ubiquiti_edgeswitch
vyatta_vyos
vyos
```


Serial Settings i would like to try later
-----------------------------------------

```        self.serial_settings = {
            "port": "COM1",
            "baudrate": 9600,
            "bytesize": serial.EIGHTBITS,
            "parity": serial.PARITY_NONE,
            "stopbits": serial.STOPBITS_ONE,
        }

```

---

[1]: images/NetDevops.jpg
