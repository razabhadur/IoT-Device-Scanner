# Enhanced IoT Device Scanner

The Enhanced IoT Device Scanner is a robust tool designed to bolster the security of networks with IoT devices. As the number of IoT devices continues to surge, networks become increasingly susceptible to vulnerabilities stemming from these devices. This tool empowers users by scanning the local network, pinpointing connected devices, and cross-referencing them with a database of known vulnerabilities or default credentials.

## Features

- **Device Discovery**: Efficiently scans the local network to identify connected devices using ARP.
- **Device Identification**: Recognizes common IoT devices based on their MAC addresses.
- **Vulnerability Database Integration**: Seamlessly checks devices against a database of known vulnerabilities or default credentials.
- **Alerts**: Instantly notifies the user about devices with default credentials or known vulnerabilities.
- **Logging**: Maintains a comprehensive log of scanned devices and identified vulnerabilities.
- **User Interface**: Provides an intuitive command-line interface for seamless user interaction.

## Usage

1. Clone the repository or download the script.
2. Run the script:
   ```
   python enhanced_iot_device_scanner.py
   ```
3. Wait for the scan to complete.
4. Review the generated report for insights and recommendations.

## Contributing

Contributions are always welcome! Please submit a pull request or open an issue to suggest improvements or add new features.

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is for educational and informational purposes only. Ensure thorough testing before using in any critical or production environments.
