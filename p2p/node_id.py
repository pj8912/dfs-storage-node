import requests
import socket
import hashlib


def generate_nodeid():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ip1 = sock.getsockname()[0]

    res = requests.get("https://api.ipify.org?format=json")
    ip2 = res.json()['ip']


    #newip string
    newip = str(ip1)+str(ip2)

    #create hash with sha1
    node_id_hash = hashlib.sha1(newip.encode('utf-8')).hexdigest()
    #print(node_id_hash)

    sock.close()
    return node_id_hash


generate_nodeid()

