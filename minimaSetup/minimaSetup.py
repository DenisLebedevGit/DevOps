import time

import paramiko


class Setup:
    def __init__(self):
        self.hosts_list = ['38.242.234.85', '62.171.148.68', '62.171.148.87', '62.171.148.247', '75.119.157.3']
        self.pass_list = ['1WvIAjR5ZigVZcK95nJhew','e9Pmk5AG41Ba3lAGOtGLIQ62','78dCyNaJKg4','ZnCgXg5yMS4M8E2TU','Germany2281488','vAFFCjgh7q8zi262WKxsm','624d0blW']
        self.key_list = ['db9ec32a-c1ea-40cb-b9a8-9ac976404ea9', '079d5f0a-d847-49e4-8fdd-9e3023587463',
                    '9399ab99-7867-4974-a41d-45acc314bc4c', 'c2a7974e-4616-4190-861b-d826bc30cf04',
                    '07243549-bc0b-4f88-95bc-131561711edd']
        self.cmd_download_remote = 'wget -O minima_setup.sh https://raw.githubusercontent.com/minima-global/Minima/master/scripts/minima_setup.sh ' \
                                   '&& chmod +x minima_setup.sh ' \
                                   '&& sudo ./minima_setup.sh -r 9122 -p 9121 > server.log'

    def installer(self):
        set_max_value = 5
        a = 0
        while a != set_max_value:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.hosts_list[a], username='root', password=self.pass_list[a], port=22)
            stdin, stdout, stderr = client.exec_command(self.cmd_download_remote)
            print(f'{self.hosts_list[a]} conn success, key {self.key_list[a]}')
            time.sleep(120)
            stdin, stdout, stderr = client.exec_command(f'curl 127.0.0.1:9125/incentivecash%20uid:{self.key_list[a]}')
            for i in stdout.readlines():
                print(i)
            a = a+1


a = Setup()
a.installer()
