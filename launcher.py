import json
import subprocess
import os
import sys

CONFIG_PATH = "config.json"

def load_apps():
    if os.path.exists(CONFIG_PATH) and os.path.getsize(CONFIG_PATH) > 0:
        try:
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error: config.json is not valid JSON.")
    return []

def launch_apps(apps):
    for app in apps:
        if os.path.exists(app):
            try:
                subprocess.Popen(app)
            except Exception as e:
                print(f"Failed to launch {app}: {e}")
        else:
            print(f"App not found: {app}")

if __name__ == "__main__":
    apps = load_apps()
    if apps:
        launch_apps(apps)

    # Optional: silently exit
    sys.exit(0)
