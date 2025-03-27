import os
import sys
import subprocess
import urllib.request
import tempfile

def download_get_pip():
    """Download get-pip.py installer"""
    print("Downloading get-pip.py...")
    url = "https://bootstrap.pypa.io/get-pip.py"
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as tmp_file:
            urllib.request.urlretrieve(url, tmp_file.name)
            return tmp_file.name
    except Exception as e:
        print(f"Error downloading get-pip.py: {e}")
        return None

def install_pip():
    """Install pip using get-pip.py"""
    print("Starting pip installation...")
    
    # Download get-pip.py
    get_pip_path = download_get_pip()
    if not get_pip_path:
        print("Failed to download get-pip.py")
        return False
    
    try:
        # Run get-pip.py
        print("Installing pip...")
        subprocess.check_call([sys.executable, get_pip_path])
        
        # Verify installation
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        print("\nPip installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing pip: {e}")
        return False
    finally:
        # Clean up
        try:
            os.unlink(get_pip_path)
        except:
            pass

def main():
    print("Pip Installation Helper")
    print("=" * 50)
    
    # Check if pip is already installed
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        print("\nPip is already installed!")
        return
    except subprocess.CalledProcessError:
        pass
    
    # Install pip
    if install_pip():
        print("\nYou can now use pip to install Python packages.")
        print("Example: pip install package_name")
    else:
        print("\nFailed to install pip. Please try installing manually:")
        print("1. Download get-pip.py from https://bootstrap.pypa.io/get-pip.py")
        print("2. Run: python get-pip.py")

if __name__ == "__main__":
    main() 