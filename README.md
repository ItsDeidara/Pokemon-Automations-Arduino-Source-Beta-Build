# Pokemon Automation SerialPrograms Beta Helper

This script automates some of the setup for building compiling beta builds of the Pokemon Automation Project SerialPrograms. https://github.com/PokemonAutomation

## Current Beta Version
v0.59.9

## Download

To get the latest beta version of this script and precompiled beta of the SerialProgram

1. Click the green "Code" button.
2. Select "Download ZIP" to download the latest version.
3. Extract the ZIP file to your desired location.
4. The exe will be in build/RelWithDebInfo/ 

This allows you to always get the most up-to-date version without waiting for formal releases.

## Prerequisites

Before running this script, ensure you have the following installed:

- **Git**: For cloning repositories
- **Qt Creator**: The IDE for building the project
- **Visual Studio 2022**: With C++ development tools and Windows SDK

Pretty much just follow the Build Tools section of their officlal guide and install QT 6.8.3 (https://github.com/PokemonAutomation/Arduino-Source/blob/main/SerialPrograms/BuildInstructions/Build-Windows-Qt6.8.3.md)

Once complete you can run the python script to automatically do steps 1-6 of the setup process from the same official Tutorial: (https://github.com/PokemonAutomation/Arduino-Source/blob/main/SerialPrograms/BuildInstructions/Build-Windows-Qt6.8.3.md)

## What the Script Does

The setup wizard performs the following steps:

1. **Select Qt Creator Executable**: Prompts you to locate and select your `qtcreator.exe` file for automatically opening
2. **Select Visual Studio Command Prompt**: Prompts you to locate the `vcvars64.bat` file for VS 2022 x64 Native Tools
3. **Clone Repositories**:
   - Clones the Arduino-Source repository from PokemonAutomation
   - Clones the Packages repository from PokemonAutomation
4. **Copy Resources**: Copies necessary resource files from Packages to Arduino-Source
5. **Open Qt Creator**: Launches Qt Creator with the project's CMakeLists.txt file

## Usage

1. Run the script: `python pullOpenQT.py`
2. Follow the prompts to select the required executables
3. The script will handle cloning and setup automatically
4. Qt Creator will open with the project ready for building
5. Follow steps 7-9 in the offiical build tutorial (https://github.com/PokemonAutomation/Arduino-Source/blob/main/SerialPrograms/BuildInstructions/Build-Windows-Qt6.8.3.md)