import subprocess
import os
import sys

def install_req(requirements_file="requirements.txt"):
    if not os.path.exists(requirements_file):
        print(f"{requirements_file} not found!")
        return

    with open(requirements_file, 'r') as file:
        packages = [line.strip() for line in file if line.strip() and not line.startswith('#')]

    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to install {package}: {e}")

if __name__ == "__main__":
    install_req()
