from selenium import webdriver
import json
import time


total_file = open("./data/skills_list_in_department/total.json", "r").read()
total_dict = json.loads(total_file)
driver = webdriver.Chrome(executable_path="./chrome driver/chromedriver")

group_size = 100
group_result = {}

print(len(total_dict))

for i, (skill_name, skill_address) in enumerate(total_dict.items()):
    if i >= 26700:
        print(i)
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

        group_result[skill_name] = result

        if i % group_size == group_size - 1 or i == len(total_dict)-1:
            open("./data/skills_intro_pages/"+str(int(i / group_size))+".json", "w").write(json.dumps(group_result))
            group_result = {}

        time.sleep(1)

