from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
import time

def TOR(geckodriver_path, TOR_path, headless=False):
    # Ensure consistent path format
    TOR_path = os.path.normpath(TOR_path)
    geckodriver_path = os.path.normpath(geckodriver_path)

    os.environ['TOR_SOCKS_HOST'] = '127.0.0.1'
    os.environ['TOR_SOCKS_PORT'] = '9150'

    options = Options()

    # Tor Browser profile path
    tor_profile_path = os.path.join(TOR_path, 'Browser', 'TorBrowser', 'Data', 'Browser', 'profile.default')
    options.set_preference("profile", tor_profile_path)

    # Tor SOCKS proxy settings
    options.set_preference('network.proxy.type', 1)
    options.set_preference('network.proxy.socks', '127.0.0.1')
    options.set_preference('network.proxy.socks_port', 9150)
    options.set_preference("network.proxy.socks_remote_dns", False)

    # Additional preferences
    options.set_preference("intl.language_notification.shown", True)
    options.set_preference("intl.locale.requested", "en-US,ru-RU")
    options.set_preference("torbrowser.migration.version", 1)
    options.set_preference("torbrowser.settings.bridges.builtin_type", "")
    options.set_preference("torbrowser.settings.bridges.enabled", False)
    options.set_preference("torbrowser.settings.bridges.source", -1)
    options.set_preference("torbrowser.settings.enabled", True)
    options.set_preference("torbrowser.settings.firewall.enabled", False)
    options.set_preference("torbrowser.settings.proxy.enabled", False)
    options.set_preference("torbrowser.settings.quickstart.enabled", True)

    # Set binary location for Tor Browser
    options.binary_location = os.path.join(TOR_path, 'Browser', 'firefox.exe')

    # Add headless mode if specified
    if headless:
        options.add_argument("--headless")

    # Initialize WebDriver
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(options=options, service=service)

    # Implicitly wait for elements to be found
    driver.implicitly_wait(10)

    # Connect to Tor network
    driver.find_element(By.ID, "connectButton").click()
    time.sleep(5)  # Allow time for connection

    # Redirect to https://check.torproject.org
    driver.get("https://check.torproject.org")

    return driver

if __name__ == "__main__":
    driver = TOR(
        "C://Program Files//geckodriver//geckodriver.exe",
        "C://Users//abeck//OneDrive//Desktop//Tor Browser"
    )
