**SafeSim: Malware Behavior Simulation Tool**

SafeSim is a Python-based tool designed to simulate various malware behaviors in a controlled and safe environment. It is built for cybersecurity professionals, researchers, and students to analyze and understand how different malware operates without risking actual systems or data.

This tool provides a hands-on approach to studying malware tactics, techniques, and procedures (TTPs), enhancing training and improving incident response strategies.


**Features**

File Operations: Simulates malicious file creation, modification, and deletion.

Registry Manipulation: Mimics changes to the Windows registry (Windows only).

Network Traffic: Simulates HTTP requests and DNS queries.

Process Creation and Termination: Emulates malware-like process behaviors.

Memory-Resident Malware: Demonstrates fileless malware techniques.

Keylogging: Captures simulated keystrokes to mimic keylogger behavior.

Lateral Movement: Simulates remote command execution over SSH.

Phishing Simulation: Logs a simulated phishing email with malicious links.


**How It Works**

SafeSim operates by executing simulated malware behaviors based on a customizable configuration file (config.json). Each action is logged for detailed analysis, allowing users to study how malware operates and test the response of security systems.

**Installation**

**Prerequisites**

Python 3.8 or higher
Recommended: Use a virtual environment for installation
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/username/SafeSim.git
cd SafeSim
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the tool by editing the config.json file (optional).

Run the tool:

bash
Copy code
python safe_sim.py


**Configuration**

The behavior of the tool is controlled via the config.json file. Each module (e.g., file operations, network traffic) can be enabled or disabled. Below is an example configuration:

json
Copy code
{
  "simulate_file_operations": true,
  "simulate_registry_operations": true,
  "simulate_network_traffic": true,
  "simulate_process_creation": true,
  "simulate_memory_resident": true,
  "simulate_keylogging": false,
  "simulate_lateral_movement": false,
  "simulate_phishing": true
}
You can also customize the parameters for each simulation, such as file paths, URLs, and registry keys.


**Logging**

All activities performed by the tool are logged in logs.txt with timestamps. The logs provide details of every simulated behavior, making it easy to analyze the output.

**Example log entry:**

plaintext
Copy code
[2024-11-23 14:15:30] Created file: temp_simulation/malware_test.txt
[2024-11-23 14:15:32] HTTP GET Request to http://example.com | Status Code: 200
[2024-11-23 14:15:34] Simulated phishing email sent to victim@example.com with link: http://malicious.example.com
Use Cases
Cybersecurity Training:
Study malware behaviors in a safe and controlled manner.
Security Testing:
Test the effectiveness of antivirus, firewalls, and detection tools.
Incident Response Practice:
Train security teams to identify and mitigate simulated malware activities.
Legal Disclaimer
This tool is designed strictly for educational and research purposes. It should only be used in a controlled, sandboxed environment. Any malicious or unethical use of this tool is strictly prohibited and the responsibility lies solely with the user.



**Future Enhancements**

Add support for additional malware behaviors (e.g., ransomware simulation, advanced persistence).
Export logs to JSON or CSV for integration with SIEM tools.
Create a graphical interface for easier interaction.


**Support**

If you have any questions or issues, please open an issue on the repository or contact the author at hbhavar12@gmail.com.
