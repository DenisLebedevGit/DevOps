import time

import paramiko

dict_hosts = {
    #"38.242.234.85": ["1WvIAjR5ZigVZcK95nJhew", "iixjlgktpjluwkfyxqzkcbxx"],
    #"38.242.143.103": ["DJFOUNDmoneyy63233", "kcikcbojjvobqxzpvvkfbtes"],
    #"185.255.131.221": ["y36Ou6KodyL38XQanK5zzuHdtU", "yqcvejelemcasafepaapcgkk"],
    #"38.242.217.196": ["SkJT5S5K9XvDOFE7Tom0x10EIoJ", "srtolxncpvpazptapfskrovv"],
    #"161.97.157.114": ["3KQSI0T0Imy", "lqvnvfacclkbquuejtwqziew"],
    #"38.242.142.6": ["uoSPuq0VRp7V6gxwWW55I16LUr", "nkkrqwvywpfjpekrgnthszda"],
    #"193.187.129.19": ["Crypto99fundst", "ylhsjyfezyytlbqznvebmrtp"],
    #"38.242.157.208": ["JeCpX7fJ6T7B9Mihf6S", "scafappgiiqwxyhxdrlnlnrr"],
    #"185.255.131.194": ["j6WZwVtGPQ9oOP4c5", "dcdthvbfybxskofvpyyihqzr"],
    #"38.242.217.214": ["624d0blW", "nvrcnkgzmzhdsxwvnsjbddts"],
    #"62.171.148.67": ["vAFFCjgh7q8zi262WKxsm", "jtmskxuqsjmwvefnnfvwffyu"],
    #"62.171.148.68": ["e9Pmk5AG41Ba3lAGOtGLIQ62", "oafgvjixhwyozzickzbonxof"],
    #"62.171.148.87": ["78dCyNaJKg4", "fpogywylvvlqrexxgtakclrh"],
    #"62.171.148.247": ["ZnCgXg5yMS4M8E2TU", "ozjwtvauqdlisawgpnwbwtsb"],
    "75.119.157.3": ["Germany2281488", "qrfxfirqijcqyzuvrkuglycc"]
}


class Setup:
    def __init__(self, host, password, token):

        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.host = host
        self.password = password
        self.key = token
        self.cmd_download = "wget 'https://staticassets.meson.network/public/meson_cdn/v3.1.18/meson_cdn-linux-amd64.tar.gz' && tar -zxf /root/meson_cdn-linux-amd64.tar.gz && rm -f /root/meson_cdn-linux-amd64.tar.gz && cd /root/meson_cdn-linux-amd64 && /root/meson_cdn-linux-amd64/service install meson_cdn"
        self.cmd_install = f"nohup /root/meson_cdn-linux-amd64/meson_cdn config set --token={self.key} --https_port=443 --cache.size=30 &"
        self.cmd_open_port = "iptables -A INPUT -p tcp --dport 443 -j ACCEPT"
        self.cmd_start = "nohup /root/meson_cdn-linux-amd64/service restart meson_cdn &"

    def installer(self):
        self.client.connect(hostname=self.host, username='root', password=self.password, port=22)
        print(f'{self.host} conn success, key {self.key}')
        stdin, stdout, stderr = self.client.exec_command(self.cmd_download)
        for k in stdout.readlines():
            print(k)
        print(f' now i do {self.cmd_download}')
        time.sleep(30)
        self.client.exec_command(f'echo "{self.cmd_install}" > install.sh')
        self.client.exec_command(f'chmod +x /root/install.sh')
        self.client.exec_command('nohup /root/install.sh &')
        stdin, stdout, stderr = self.client.exec_command(self.cmd_install)
        time.sleep(10)
        for m in stdout.readlines():
            print(m)
        print(f' now i do {self.cmd_install}')
        self.client.exec_command(self.cmd_open_port)
        print(f' now i do {self.cmd_open_port}')
        time.sleep(15)
        stdin, stdout, stderr = self.client.exec_command(self.cmd_start)
        print(f' now i do {self.cmd_start}')
        for i in stdout.readlines():
            print(i)
        time.sleep(60)


# a = Setup()
# a.installer()
#

for key in dict_hosts:
    try:
        print(f'host: {key}  pass: {dict_hosts.get(key)[0]}, token: {dict_hosts.get(key)[1]} \n\n')
        a = Setup(host=key, password=dict_hosts.get(key)[0], token=dict_hosts.get(key)[1])
        a.installer()
    except: pass