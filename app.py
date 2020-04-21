import logging as logger

from flask import Flask
from flask_restful import Resource, Api
import nmap

app = Flask(__name__)
Api = Api(app)

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    port = [scanner[ip_addr]['tcp'].keys()]
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= '4':
    print("Please enter a valid option")

myitem = []


class openPorts(Resource):

    @app.route('/openport/<string:name>')
    def get(name):
        for item in myitem:
            if item['name'] == name:
                return item

    def post(self, name):
        item = {'name': name, 'price': 120, 'Nmap Version:': scanner.nmap_version(),
                'Scanner Info': scanner.scaninfo(),
                'Ip Status: ': scanner[ip_addr].state()}
        myitem.append(item)
        return item


Api.add_resource(openPorts, '/openport/<string:name>')
app.run(port=5000)

# logger.basicConfig(level="DEBUG")

# app = Flask(__name__)
# if __name__ == '__main__':
# from api import *
# app.run(host="0.0.0.0", port="5000", debug=True, use_reloader=True)
