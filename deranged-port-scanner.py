import socket
import logging
import json
from datetime import datetime

# Configure logging:
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# ANSI escape codes for colored text
GREEN = "\033[92m"
RESET = "\033[0m"


def check_port(ip, port, timeout=1):
    """
    Check if a port is open on a specified IP address.

    Parameters:
    ip (str): The IP address to check.
    port (int): The port number to check.
    timeout (int, optional): The timeout for the socket connection attempt. Defaults to 1 second.

    Returns:
    bool: True if the port is open, False otherwise.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                logging.info(f"{GREEN}Port {port} is open on {ip}{RESET}")
                return True
            else:
                logging.info(f"Port {port} is closed on {ip}")
                return False
    except socket.error as e:
        logging.error(f"Error checking port {port} on {ip}: {e}")
        return False


def generate_report(open_ports):
    """
    Generate a report of the scan results in JSON format.

    Parameters:
    open_ports (dict): A dictionary of IP addresses with a list of open ports.

    Returns:
    None
    """
    report = {
        "scan_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "open_ports": open_ports,
    }
    try:
        with open("report.json", "w") as f:
            json.dump(report, f, indent=4)
    except IOError as e:
        logging.error(f"Error writing report file: {e}")


def validate_ip(ip):
    """
    Validate if the given string is a valid IP address.

    Parameters:
    ip (str): The IP address to validate.

    Returns:
    bool: True if the IP is valid, False otherwise.
    """
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def main():
    try:
        # Ask the user for the base IP address:
        base_ip = input("Enter the base IP address (e.g., 192.168.1.): ")
        if not validate_ip(base_ip + "1"):
            raise ValueError("Invalid base IP address format.")

        # Ask the user for the start and end IP numbers:
        start_ip = int(input("Enter the start IP number: "))
        end_ip = int(input("Enter the end IP number: "))

        if start_ip > end_ip:
            raise ValueError(
                "Start IP number must be less than or equal to end IP number."
            )

        # Ask the user for the start and end port numbers:
        start_port = int(input("Enter the start port number to scan (1-65535): "))
        end_port = int(input("Enter the end port number to scan (1-65535): "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range.")

        open_ports = {}
        for i in range(start_ip, end_ip + 1):
            ip = base_ip + str(i)
            open_ports[ip] = []
            for port in range(start_port, end_port + 1):
                if check_port(ip, port):
                    open_ports[ip].append(port)

        # Filter out IPs with no open ports
        open_ports = {ip: ports for ip, ports in open_ports.items() if ports}

        if open_ports:
            # Generate a report of the scan results:
            generate_report(open_ports)
            logging.info("Report generated: report.json")
    except ValueError as e:
        logging.error(f"Invalid input: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
