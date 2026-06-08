from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.execute_cdp_cmd("Network.enable", {})

driver.execute_cdp_cmd(
    "Network.setBlockedURLs",
    {
        "urls": [
            "*adsbygoogle.js*",
            "*googlesyndication.com*",
            "*doubleclick.net*",
            "*googleadservices.com*",
            "*show_ads_impl*"
        ]
    }
)

driver.get("https://automationexercise.com")
time.sleep(100)