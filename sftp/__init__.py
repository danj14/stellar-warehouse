import os
import paramiko

private_key = os.environ["private_key"]
host_key = os.environ["host_key"]

# 1) Load encryption keys for connection authentication
private_pkey = paramiko.rsakey.RSAKey(data=host_key, filename=private_key)
cert_key = private_pkey.load_certificate(host_key)

# 2) Start new connection session
# ...Link: https://docs.paramiko.org/en/stable/api/transport.html#paramiko.transport.Transport
session = paramiko.transport.Transport(sock='192.168.1.9:22')
session.connect(hostkey=cert_key, username='pi', pkey=private_pkey)

# 2) https://docs.paramiko.org/en/stable/api/channel.html#paramiko.channel.Channel



# 3) Host keys? https://docs.paramiko.org/en/stable/api/hostkeys.html


# 4) https://docs.paramiko.org/en/stable/api/sftp.html


# par = paramiko.hostkeys.HostKeys(os.environ["host_key"])
# par.load(host_key)
# print(par.lookup('192.168.1.9'))
# par.clear()

# TODO: we are going to try paramiko
