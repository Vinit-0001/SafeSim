import os
import json
import subprocess
import psutil
from pynput import keyboard
import requests
import socket
from datetime import datetime

# Logger
LOG_FILE = "logs.txt"

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {event}\n")
    print(f"[{timestamp}] {event}")

# File Operations
def simulate_file_operations(config):
    log_event("Simulating file operations")
    directory = config["file_operations"]["directory"]
    file_name = config["file_operations"]["file_name"]
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, "w") as f:
        f.write("This is a test file for malware simulation.")
    log_event(f"Created file: {file_path}")
    
    if config["file_operations"]["delete_after_creation"]:
        os.remove(file_path)
        log_event(f"Deleted file: {file_path}")

# Registry Operations (Windows only)
def simulate_registry_operations(config):
    log_event("Simulating registry operations")
    if os.name != "nt":
        log_event("Registry operations are Windows-only.")
        return
    
    try:
        import winreg
        key = config["registry_operations"]["key"]
        value_name = config["registry_operations"]["value_name"]
        value_data = config["registry_operations"]["value_data"]
        
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, value_data)
        log_event(f"Registry key created: {key} -> {value_name} = {value_data}")
    except Exception as e:
        log_event(f"Registry simulation error: {e}")

# Network Simulation
def simulate_network_traffic(config):
    log_event("Simulating network traffic")
    target_url = config["network_simulation"]["target_url"]
    simulate_dns = config["network_simulation"]["simulate_dns_queries"]

    try:
        response = requests.get(target_url)
        log_event(f"HTTP GET Request to {target_url} | Status Code: {response.status_code}")
        
        if simulate_dns:
            ip = socket.gethostbyname(target_url.replace("http://", "").replace("https://", ""))
            log_event(f"Simulated DNS Query: {target_url} resolved to {ip}")
    except Exception as e:
        log_event(f"Network simulation error: {e}")

# Process Simulation
def simulate_process_creation(config):
    log_event("Simulating process creation")
    process_name = config["process_simulation"]["process_name"]
    
    try:
        process = subprocess.Popen([process_name])
        log_event(f"Created process: {process.pid} ({process_name})")
        
        if config["process_simulation"]["terminate_process"]:
            process.terminate()
            log_event(f"Terminated process: {process.pid} ({process_name})")
    except Exception as e:
        log_event(f"Process simulation error: {e}")

# Memory-Resident Simulation
def simulate_memory_resident(config):
    log_event("Simulating memory-resident malware")
    payload = "This is a simulated memory-only payload." * 1000
    log_event(f"Payload loaded into memory: {len(payload)} bytes")

# Keylogger Simulation
def simulate_keylogging(config):
    log_event("Simulating keylogger")
    
    def on_press(key):
        try:
            log_event(f"Key pressed: {key.char}")
        except AttributeError:
            log_event(f"Special key pressed: {key}")
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    log_event("Keylogger running... Press Ctrl+C to stop.")

# Lateral Movement
def simulate_lateral_movement(config):
    log_event("Simulating lateral movement")
    remote_host = config["lateral_movement"]["remote_host"]
    command = config["lateral_movement"]["command"]

    try:
        result = subprocess.run(["ssh", f"user@{remote_host}", command], capture_output=True, text=True)
        log_event(f"Lateral movement command executed: {result.stdout}")
    except Exception as e:
        log_event(f"Lateral movement error: {e}")

# Phishing Simulation
def simulate_phishing(config):
    log_event("Simulating phishing email")
    fake_email = config["phishing_simulation"]["email"]
    phishing_url = config["phishing_simulation"]["url"]
    log_event(f"Simulated phishing email sent to {fake_email} with link: {phishing_url}")

# Main
def main():
    with open("config.json") as f:
        config = json.load(f)
    
    if config["simulate_file_operations"]:
        simulate_file_operations(config)
    if config["simulate_registry_operations"]:
        simulate_registry_operations(config)
    if config["simulate_network_traffic"]:
        simulate_network_traffic(config)
    if config["simulate_process_creation"]:
        simulate_process_creation(config)
    if config["simulate_memory_resident"]:
        simulate_memory_resident(config)
    if config["simulate_keylogging"]:
        simulate_keylogging(config)
    if config["simulate_lateral_movement"]:
        simulate_lateral_movement(config)
    if config["simulate_phishing"]:
        simulate_phishing(config)

if __name__ == "__main__":
    main()
