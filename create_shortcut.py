import os
from win32com.client import Dispatch

# Absolute path to launcher.py
target = os.path.abspath("launcher.py")

# Windows Startup folder
startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

# Shortcut path
shortcut_path = os.path.join(startup_folder, "AppLauncher.lnk")

# Create the shortcut
shell = Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.TargetPath = "python"  # or path to python.exe
shortcut.Arguments = f'"{target}"'
shortcut.WorkingDirectory = os.path.dirname(target)
shortcut.IconLocation = target
shortcut.save()

print(f"Shortcut created: {shortcut_path}")
