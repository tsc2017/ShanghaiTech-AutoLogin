# Shanghaitech-Autologin
Script for logging into the network of ShanghaiTech automatically.

Code derived from [https://github.com/ShanghaitechGeekPie/WifiLoginer/blob/master/eznetloginer/Src/EZNetLoginerForPython3.py](https://github.com/ShanghaitechGeekPie/WifiLoginer/blob/master/eznetloginer/Src/EZNetLoginerForPython3.py). Copyright belongs to the original authors. 

Removed unusable files or code.

Tested on Windows 10 and Ubuntu 18.04.

## Usage
- Install [Python3](https://www.python.org/downloads/)
- Edit `login.py`, fill in your user name and password
- Run `login.py`
## Auto-start in the background 
- Windows
  - Put `login.py` and `login.bat` in the same directory/folder
  - Replace "admin" with your Windows user name on the second line in `login.bat`, make sure you have a valid path to `pythonw.exe`
  - Create a shortcut of `login.bat`
  - Copy the shortcut to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
  - Reboot. Press <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>ESC</kbd> to launch Task Manager. You will see that Python is running in the background and is not taking up much system resource.

- Linux
  - Append the following line to `/etc/rc.local` before `exit 0` (You will need to [configure](https://www.centos.bz/2018/05/ubuntu-18-04-rc-local-systemd%E8%AE%BE%E7%BD%AE/) `rc.local` first if you are using Ubuntu 18.04):
   ```sh
    python3 PATH/TO/login.py
    ```
  - Reboot and run `top`. You will see that python3 is running in the background and is not taking up much system resource.
