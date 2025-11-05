import os
import json
from pathlib import Path
from tkinter import Tk, filedialog
import subprocess

def save_config(config, config_path):
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

def load_config(config_path):
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {}

def select_qt_exe():
    print("Please select the Qt Creator executable (qtcreator.exe).")
    Tk().withdraw()  # Hide the root window
    exe_path = filedialog.askopenfilename(title="Select Qt Creator Executable", filetypes=[("Executable Files", "*.exe")])
    if exe_path:
        print(f"Selected: {exe_path}")
        return exe_path
    else:
        print("No file selected. Exiting setup.")
        exit(1)

def select_vs_cmd():
    print("Please select the vcvars64.bat file for VS 2022 x64 Native Tools (typically in C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Auxiliary\\Build\\vcvars64.bat).")
    Tk().withdraw()  # Hide the root window
    cmd_path = filedialog.askopenfilename(title="Select vcvars64.bat for VS 2022", filetypes=[("Batch Files", "*.bat"), ("Shortcut Files", "*.lnk"), ("Executables", "*.exe")])
    if cmd_path:
        print(f"Selected: {cmd_path}")
        return cmd_path
    else:
        print("No file selected. Exiting setup.")
        exit(1)

def clone_repo(repo_url, destination, ask_reclone=False):
    if os.path.exists(destination):
        if ask_reclone:
            response = input(f"Repository {destination} already exists. Re-clone? (y/n): ").strip().lower()
            if response != 'y':
                print(f"Skipping clone of {destination}.")
                return
        print(f"Removing existing {destination}...")
        subprocess.run(["rmdir", "/s", "/q", destination], shell=True)
    print(f"Cloning {repo_url} into {destination}...")
    subprocess.run(["git", "clone", repo_url, destination], check=True)

def copy_resources(source, destination):
    if not os.path.exists(destination):
        print(f"Copying resources from {source} to {destination}...")
        subprocess.run(["xcopy", source, destination, "/E", "/H", "/C", "/I"], shell=True)
    else:
        print(f"Resources already copied to {destination}. Skipping.")

def main():
    os.chdir(Path(__file__).parent)  # Change to the script's directory
    config_path = Path("config.json")
    config = load_config(config_path)

    print("Welcome to the First-Time Setup Wizard!")

    # Step 1: Select Qt Creator executable
    if "qt_exe" not in config:
        config["qt_exe"] = select_qt_exe()
        print(f"Qt Creator executable: {config['qt_exe']}")
        save_config(config, config_path)

    # Step 2: Select VS 2022 x64 Native Tools Command Prompt
    if "vs_cmd" not in config:
        config["vs_cmd"] = select_vs_cmd()
        print(f"VS Command Prompt batch file: {config['vs_cmd']}")
        save_config(config, config_path)

    # Step 3: Clone repositories
    config["repos"] = {}
    base_dir = Path(__file__).parent.resolve()  # Ensure cloning happens in the same folder as the script
    serial_programs_repo = "https://github.com/PokemonAutomation/Arduino-Source.git"
    packages_repo = "https://github.com/PokemonAutomation/Packages.git"
    config["repos"]["serial_programs"] = str(base_dir / "Arduino-Source")
    config["repos"]["packages"] = str(base_dir / "Packages")
    clone_repo(serial_programs_repo, config["repos"]["serial_programs"], ask_reclone=True)
    clone_repo(packages_repo, config["repos"]["packages"], ask_reclone=True)
    save_config(config, config_path)

    # Step 4: Copy Resources folder
    resources_source = Path(config["repos"]["packages"]) / "Resources"
    resources_destination = Path(config["repos"]["serial_programs"]) / "Resources"
    copy_resources(resources_source, resources_destination)

    # Step 5: Open Qt Creator with the CMakeLists.txt file
    cmake_file = Path(config["repos"]["serial_programs"]) / "SerialPrograms" / "CMakeLists.txt"
    print(f"Opening Qt Creator with {cmake_file}...")
    print(f"Qt Creator executable: {config['qt_exe']}")
    subprocess.run([config["qt_exe"], str(cmake_file)])

    print("Setup complete! Configuration saved.")

if __name__ == "__main__":
    main()