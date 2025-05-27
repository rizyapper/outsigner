import os
import shutil

home = os.path.expanduser("~")


browser_targets = {
    "Chrome": os.path.join(home, "Library", "Application Support", "Google", "Chrome"),
    "Edge": os.path.join(home, "Library", "Application Support", "Microsoft Edge"),
    "Firefox": os.path.join(home, "Library", "Application Support", "Firefox", "Profiles"),
}

chrome_edge_targets = [
    "Cookies",            
    "Login Data",         
    "Session Storage",    
    "Sessions",           
    "Web Data",           
    "Network"             
]

firefox_targets = [
    "cookies.sqlite",         
    "logins.json",            
    "key4.db",                
    "sessionstore.jsonlz4"    
]

def delete_browser_data(browser, path):
    if not os.path.exists(path):
        print(f"[!] {browser} not found at {path}")
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
                            print(f"    – removed file {item}")
                        elif os.path.isdir(target):
                            shutil.rmtree(target, ignore_errors=True)
                            print(f"    – removed folder {item}")
                    except Exception as e:
                        print(f"    x failed to delete {item}: {e}")

    elif browser == "Firefox":
        for profile in os.listdir(path):
            profile_path = os.path.join(path, profile)
            if os.path.isdir(profile_path) and (".default" in profile):
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

print("[✔] Logout operation completed on macOS.")
