#Simple Nmap Scan Tool

This Python script is a **basic network scanning tool** that utilizes the `nmap` library to perform port scans on a target IP address. It allows users to select different scanning techniques and provides detailed scan results, including open ports, services, and protocols.  


#Features 
✅ **User Input for Target IP Address**  
✅ **Multiple Scan Modes:**  
   - **SYN Scan (-sS) [TCP]**  
   - **UDP Scan (-sU)**  
   - **Comprehensive Scan (-sS -O -A -sC) [Requires Root]**  
✅ **Scans Ports 1-1024**  
✅ **Displays Open Ports, Protocols, and Service Details**  

#Usage 
1. Install required dependencies:  
   
   images/Install required dependencies.png
   
2. Run the script:
   
   images/Run the script.png
   
4. Enter the **IP address** and select the scan type.  
5. View the scan results, including open ports and running services. 

#Requirements
- Python 3  
- `nmap` installed on the system  
- `python-nmap` module (`pip install python-nmap`)  
- Root privileges for **Comprehensive Scan (-O)**  

#Disclaimer
🔹 This script is intended for **educational and security research purposes only**.  
🔹 Unauthorized scanning of networks **without permission** may be illegal.  
🔹 The author is **not responsible** for any misuse of this tool.  


