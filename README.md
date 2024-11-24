**SafeSim: Malware Behavior Simulation Tool**

**Overview:**
SafeSim is a secure, sandboxed tool for simulating various types of malware behaviors in a controlled environment. It is designed for cybersecurity professionals, ethical hackers, and educators to better understand malware tactics, techniques, and procedures (TTPs). This tool operates entirely within isolated environments to ensure safety and prevent any unintended risks to real-world systems.

---

**Features:**

SafeSim includes simulations for the following malware behaviors:

1. File Operations
   - Simulates file creation, modification, and deletion.
2. Registry Operations (Windows-only)
   - Creates registry keys and writes values to simulate registry manipulations.
3. Network Traffic
   - Performs HTTP GET requests to simulate network-based activities.
4. Ransomware Behavior
   - Encrypts files in a specified directory and logs a simulated ransom message.
5. Credential Harvesting
   - Simulates the collection of fake credentials from common websites.
6. Data Exfiltration
   - Sends simulated sensitive data to a configured remote endpoint.
7. Persistence Mechanism (Windows-only)
   - Creates a registry entry to simulate adding persistence for malware.
8. Remote Access Trojan (RAT)
   - Simulates a RAT session by establishing a remote connection and executing commands. (Disabled by default for safety.)
9. Screenshot Capture
   - Simulates capturing a screenshot of the host machine and saving it locally.
10. Keylogger Behavior (Upcoming)
    - Logs simulated keystrokes (placeholder implementation for future enhancements).

---


**Repository Structure:**

SafeSim/

├── safe_sim.py           # Main script for running malware simulations

├── config.json           # Configuration file to customize simulation options

├── requirements.txt      # Python dependencies

├── utils.py              # Helper functions (e.g., logging)

├── logs.txt              # Log file (generated during execution)

├── LICENSE               # Licensing information

└── README.md             # Documentation (this file)


---

**Prerequisites:**
- Python 3.7 or higher
- A sandboxed or virtual environment for safe execution.

---

**Installation:**
1. Clone the repository:

```
git clone https://github.com/unknown-02/SafeSim.git

cd SafeSim
```

2. Install dependencies:
   
```
pip install -r requirements.txt
```

---

**Usage:**
1. Edit the ```config.json``` file to enable/disable specific simulations and customize their parameters:
   
   ```
   {
   
     "simulate_file_operations": true,
   
     "simulate_registry_operations": true,
   
     "simulate_network_traffic": true,
   
     "network_traffic": {   
       "url": "http://example.com"   
     },
   
     "simulate_ransomware": true,
   
     "ransomware_simulation": {   
       "target_directory": "ransomware_simulation"   
     },
   
     "simulate_credential_harvesting": true,
   
     "simulate_data_exfiltration": true,
   
     "data_exfiltration": {   
       "target_url": "http://example.com/exfiltrate"   
     },
   
     "simulate_persistence": true,
   
     "simulate_rat": false,
   
     "rat_simulation": {
   
       "host": "127.0.0.1",
   
       "port": 4444
   
     },
   
     "simulate_screenshot_capture": true
   
   }
   ```
   

2. Run the tool:

   ```
   python3 safe_sim.py
   ```

4. View logs:
   All events are logged in the logs.txt file for auditing and analysis.

---

**Safety and Legal Disclaimer:**
- This tool is strictly for educational and research purposes.
- Ensure SafeSim is executed in a sandboxed or virtual environment.
- Do not use this tool for malicious purposes; doing so is illegal and unethical.

---

**Customizable Malware Behaviors:**
- Each simulation is customizable via config.json. For example:
  - Change the target directory for ransomware simulation.
  - Specify the remote endpoint for data exfiltration.
  - Configure the RAT host and port.

---

**Limitations:**
- Registry and persistence simulations work only on Windows systems.
- Keylogger behavior is currently a placeholder and will be fully implemented in future updates.



---

**Future Enhancements:**
- Add full keylogger functionality.
- Improve RAT simulation with enhanced features.
- Implement more malware TTPs, such as privilege escalation and system reconnaissance.
