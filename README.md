Explanation of the Code:
------------------------

This Python script is designed to perform a network port scan on a range of IP addresses and ports. It checks for open ports on 
specified IP addresses and generates a report in JSON format detailing the open ports found.



User Instructions:
------------------
------------------


Running the Script:
-------------------

Ensure you have Python installed on your system.

Save the script to a file, for example, deranged-port-scanner.py.

Open a terminal or command prompt and navigate to the directory containing the script.

Run the script by typing python deranged-port-scanner.py and press Enter.



Input Instructions:
-------------------

Base IP Address: Enter the base part of the IP address (e.g., 192.168.1.). Do not include the last part (the number).

Start and End IP Numbers: Enter the range of IP numbers you want to scan. For example, if your base IP is 192.168.1., 
entering 1 and 10 will scan from 192.168.1.1 to 192.168.1.10.

Start and End Port Numbers: Enter the range of ports you want to scan. Ports range from 1 to 65535.



Output:
-------

The script will log its activities in the terminal.

If any open ports are found, a report file named report.json will be created in the same directory as the script, detailing the open ports for each IP address.



Error Handling:
---------------

The script includes error handling for invalid IP addresses, incorrect IP ranges, and invalid port ranges. If an error occurs, it will log the 
error message and stop execution.



Developed by FeakNorris

-----------------------