# Shanghaitech-Autologin
Script for logging into the network of ShanghaiTech automatically.

Code derived from [https://github.com/ShanghaitechGeekPie/WifiLoginer/blob/master/eznetloginer/Src/EZNetLoginerForPython3.py](https://github.com/ShanghaitechGeekPie/WifiLoginer/blob/master/eznetloginer/Src/EZNetLoginerForPython3.py). Copyright belongs to the original authors. 

Removed unusable files or code.

Tested on Windows 10.

## Usage
- Install [Python](https://www.python.org/downloads/)
- Edit `login.py`, fill in your user name and password
- Run `login.py`.
## Auto-start in the background
- Put `login.py` and `login.bat` in the same directory/folder
- Replace "admin" with your Windows user name on the second line in `login.bat`, make sure you have a valid path to `pythonw.exe`.
- Create a shortcut of `login.bat`
- Copy the shortcut to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
