import os
import shutil
import getpass

# Get the current user's AppData path
user = getpass.getuser()
local = f"C:\\Users\\{user}\\AppData\\Local"
roaming = f"C:\\Users\\{user}\\AppData\\Roaming"


browser_targets = {
    "Chrome": os.path.join(local, "Google", "Chrome", "User Data"),
    "Edge": os.path.join(local, "Microsoft", "Edge", "User Data"),
    "Firefox": os.path.join(roaming, "Mozilla", "Firefox", "Profiles"),
}

# Files/folders typically storing session and login data
chrome_edge_targets = [
    "Cookies", "Login Data", "Sessions", "Session Storage", "Web Data", "Network"
]

firefox_targets = [
    "cookies.sqlite", "logins.json", "sessionstore.jsonlz4"
]

def delete_browser_data(browser, path):
    if not os.path.exists(path):
        print(f"[!] {browser} not found.")
        return

    print(f"[+] Processing {browser}...")

    if browser in ["Chrome", "Edge"]:
        for profile in os.listdir(path):
            profile_path = os.path.join(path, profile)
            if os.path.isdir(profile_path):
                for item in chrome_edge_targets:
                    target = os.path.join(profile_path, item)
                    try:
                        if os.path.isfile(target):
                            os.remove(target)
                        elif os.path.isdir(target):
                            shutil.rmtree(target, ignore_errors=True)
                    except Exception as e:
                        print(f"[-] Failed to delete {target}: {e}")
    elif browser == "Firefox":
        for profile in os.listdir(path):
            profile_path = os.path.join(path, profile)
            if os.path.isdir(profile_path):
                for item in firefox_targets:
                    target = os.path.join(profile_path, item)
                    try:
                        if os.path.exists(target):
                            os.remove(target)
                    except Exception as e:
                        print(f"[-] Failed to delete {target}: {e}")

    print(f"[+] Done with {browser}.\n")


for browser, path in browser_targets.items():
    delete_browser_data(browser, path)

print(" Logout operation completed.")
