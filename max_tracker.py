import os
import subprocess
import ctypes
import sys

def is_admin():
    """Check if the script is running with admin privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def synchronize_time():
    """Synchronize the system clock with internet time servers."""
    try:
        # Run the command to sync time
        subprocess.run("w32tm /resync", check=True, shell=True)
        print("System time synchronized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to synchronize time: {e}")

def configure_time_service():
    """Configure the Windows Time service to start automatically."""
    try:
        # Set the Windows Time service to start automatically
        subprocess.run("sc config w32time start= auto", check=True, shell=True)
        # Start the Windows Time service
        subprocess.run("net start w32time", check=True, shell=True)
        print("Windows Time service configured and started.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to configure Windows Time service: {e}")

def main():
    if not is_admin():
        print("This script requires administrative privileges. Please run as administrator.")
        sys.exit(1)

    configure_time_service()
    synchronize_time()

if __name__ == "__main__":
    main()