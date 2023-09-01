import socket
import os
import re

class IoTDeviceScanner:

    def __init__(self):
        self.vulnerability_db = {
            '00:11:22:33:44:55': 'Vulnerable Smart Camera',
            '66:77:88:99:AA:BB': 'Router with Default Credentials'
        }
        self.scanned_devices = {}

    def scan_local_network(self):
        devices = os.popen('arp -a').read()
        ip_mac_pairs = re.findall(r'(\d+\.\d+\.\d+\.\d+).+?([a-fA-F0-9]{2}(-[a-fA-F0-9]{2}){5}|[a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){5})', devices)
        return {ip: mac.replace('-', ':') for ip, mac in ip_mac_pairs}

    def identify_vulnerable_devices(self, devices):
        for ip, mac in devices.items():
            if mac in self.vulnerability_db:
                self.scanned_devices[ip] = self.vulnerability_db[mac]

    def generate_report(self):
        report = 'IoT Device Scanner Report\n'
        report += '=' * 30 + '\n'
        for ip, device in self.scanned_devices.items():
            report += f'IP Address: {ip} - Device: {device}\n'
        return report

    def run(self):
        devices = self.scan_local_network()
        self.identify_vulnerable_devices(devices)
        report = self.generate_report()
        print(report)

if __name__ == '__main__':
    scanner = IoTDeviceScanner()
    scanner.run()
