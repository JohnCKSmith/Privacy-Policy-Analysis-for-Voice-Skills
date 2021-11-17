import json
from selenium import webdriver
import time


download_dir = "/home/john/PycharmProjects/Mobile Security/data/privacy_pages"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
profile = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome(executable_path="./chrome driver/chromedriver", chrome_options=options)
driver.set_page_load_timeout(30)
privacy_list = json.loads(open("./data/policy_list.txt", "r").read())
for i in range(len(privacy_list)):
    privacy = privacy_list[i]
    print(len(privacy_list), i, privacy)
    if privacy is not None:
        try:
            if ".pdf" in privacy:
                driver.get(privacy)
                time.sleep(2.5)
            else:
                driver.get(privacy)
                time.sleep(2.5)
                open("./data/privacy_pages/"+str(i)+".data", "w").write(driver.find_element_by_xpath("/html/body").text)
        except:
            continue
