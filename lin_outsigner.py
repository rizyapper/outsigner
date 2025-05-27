import os
import shutil
import getpass

# Get the current user's home directory
home = os.path.expanduser("~")

# Define browser session directories on Linux
browser_targets = {
    "Chrome": os.path.join(home, ".config", "google-chrome"),
    "Chromium": os.path.join(home, ".config", "chromium"),
    "Edge": os.path.join(home, ".config", "microsoft-edge"),
    "Firefox": os.path.join(home, ".mozilla", "firefox"),
}

# Files/folders typically storing session and login data
chrome_edge_targets = [
    "Cookies",            # cookie jar (session IDs, auth cookies)
    "Login Data",         # saved passwords
    "Session Storage",    # origin-based storage
    "Sessions",           # session recovery files
    "Web Data",           # autofill, etc.
    "Network"             # network-related caches
]

firefox_targets = [
    "cookies.sqlite",         # cookie jar
    "logins.json",            # saved logins
    "key4.db",                # encryption keys (DPAPI equivalent)
    "sessionstore.jsonlz4",   # session recovery
]

def delete_browser_data(browser, path):
    if not os.path.isdir(path):
        print(f"[!] {browser} not found at {path}")
        return

    print(f"[+] Processing {browser}...")

    # Chrome-style browsers (profile folders like 'Default', 'Profile 1', etc.)
    if browser in ["Chrome", "Chromium", "Edge"]:
        for profile in os.listdir(path):
            profile_path = os.path.join(path, profile)
            if os.path.isdir(profile_path):
                for item in chrome_edge_targets:
                    target = os.path.join(profile_path, item)
                    try:
                        if os.path.isfile(target):
                            os.remove(target)
                            print(f"    – removed file {item}")
                        elif os.path.isdir(target):
                            shutil.rmtree(target, ignore_errors=True)
                            print(f"    – removed dir  {item}")
                    except Exception as e:
                        print(f"    x failed to delete {item}: {e}")

    # Firefox (each profile is a *.default or *.default-release folder)
    elif browser == "Firefox":
        for entry in os.listdir(path):
            profile_path = os.path.join(path, entry)
            if os.path.isdir(profile_path) and entry.endswith((".default", ".default-release")):
                for item in firefox_targets:
                    target = os.path.join(profile_path, item)
                    try:
                        if os.path.exists(target):
                            os.remove(target)
                            print(f"    – removed {item}")
                    except Exception as e:
                        print(f"    x failed to delete {item}: {e}")

    print(f"[+] Done with {browser}.\n")

# Run cleanup
for browser, path in browser_targets.items():
    delete_browser_data(browser, path)

print("[✔] Logout operation completed.")
