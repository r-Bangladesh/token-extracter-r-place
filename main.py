
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up the Chrome driver
options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

with open("accounts.json") as f:
    accounts = json.load(f)

for account in accounts:
    driver = webdriver.Chrome(options=options)

    # Log in to Reddit
    driver.get("https://www.reddit.com/login")
    username = driver.find_element(By.ID, "loginUsername")
    password = driver.find_element(By.ID, "loginPassword")
    username.send_keys(account["username"])
    password.send_keys(account["password"])
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]").click()

    # Wait for the page to load and navigate to /r/place
    time.sleep(5)
    driver.get('https://www.reddit.com/r/place/?screenmode=fullscreen')
    time.sleep(8)
    result = driver.execute_script("""    const usingOldReddit = window.location.href.includes('new.reddit.com');
        const url = usingOldReddit ? 'https://new.reddit.com/r/place/' : 'https://www.reddit.com/r/place/';
        const response = await fetch(url);
        const responseText = await response.text();

        return responseText.split('"accessToken":"')[1].split('"')[0]""")

    # Write the result to a JSON file
    filename = "result.json"
    if os.path.exists(filename):
        with open(filename) as f:
            data = json.load(f)
    else:
        data = []

    data.append({"accessToken": result})

    with open(filename, "w") as f:
        json.dump(data, f)
    driver.close()
