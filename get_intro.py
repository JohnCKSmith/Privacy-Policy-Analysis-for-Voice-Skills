from selenium import webdriver
import json
import time

skill_list = json.loads(open("./data/skill_list.txt", "r").read())
driver = webdriver.Chrome(executable_path="./chrome driver/chromedriver")
print(len(skill_list))
for i, (hash_tag, skill_content) in enumerate(skill_list.items()):
    skill_address = skill_content["skill_page"]

    if i >= 0:
        print(i, len(skill_list))
        driver.get(skill_address)
        result = {}
        review_count = ""
        description = ""
        details = ""
        privacy_policy_href = ""
        try:
            review_count = driver.find_element_by_class_name("a2s-review-star-count").text
            description = driver.find_element_by_id("a2s-description").text
            details = driver.find_element_by_id("a2s-skill-details").text
        except:
            print("Failed!")
        try:
            privacy_policy_href = driver.find_element_by_id("a2s-skill-details").find_element_by_xpath("//*[contains(text(), 'Privacy Policy')]").get_attribute("href")
        except:
            print("No privacy policy href.")
        result["review-count"] = review_count
        result["description"] = description
        result["details"] = details
        result["privacy_policy_href"] = privacy_policy_href
        result["skill_name"] = skill_content["skill_name"]
        open("./data/skills_intro_pages/"+hash_tag+".json", "w").write(json.dumps(result))
        time.sleep(1)
