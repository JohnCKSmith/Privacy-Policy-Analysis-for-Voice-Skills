import time
import json
from selenium import webdriver

departments_list = list(reversed(list(map(lambda x: x.split(" : "), open("./data/missed/departments.list", "r").read().splitlines()))))
total_dict = dict()
for department_tuple in departments_list:
    department_name = department_tuple[0]
    list_length = int(department_tuple[2])
    print(department_name, list_length)
    for j in range(list_length):
        skills_list_file = open("./data/missed/" + department_name + "/" + str(j + 1) + ".json", "r").read()
        skills_list = json.loads(skills_list_file)
        for item in skills_list:
            hash_tag = item[1].split("/dp/")[1].split('/')[0]
            total_dict[hash_tag] = {"skill_name": item[0], "skill_page": item[1]}
            if "department" not in total_dict[hash_tag].keys():
                total_dict[hash_tag]["deparment"] = [department_name]
            else:
                total_dict[hash_tag]["deparment"].append(department_name)
open("./data/final/missed_list.text", "w").write(json.dumps(total_dict))


departments_list = list(map(lambda x: x.split(" : "), open("./data/departments.list", "r").read().splitlines()))
total_dict = dict()
driver = webdriver.Chrome(executable_path="./chrome driver/chromedriver")
for department_tuple in departments_list:
    department_name = department_tuple[0]
    department_address = department_tuple[1]
    list_length = int(department_tuple[2])
    print(department_name, department_address, list_length)
    driver.get(department_address)
    next_bottuon = driver.find_element_by_class_name("a-last")
    next_bottuon.click()
    base_url = driver.current_url
    target_url_list = str(base_url).split("&")
    for j in range(list_length):
        print(department_name, j+1, list_length)
        if target_url_list[-5].startswith("page"):
            target_url_list[-5] = 'page=' + str(j+1)
        elif target_url_list[-6].startswith("page"):
            target_url_list[-6] = 'page=' + str(j + 1)
        target_url = "&".join(target_url_list)
        print(target_url)

        if j >= 0:
            driver.get(target_url)
            main_slot = driver.find_element_by_class_name("s-main-slot")
            main_results = main_slot.find_elements_by_class_name("s-result-item")
            for i in range(16):
                if i < len(main_results):
                    try:
                        skill_name = main_results[i].find_element_by_class_name("a-size-medium").text
                        skill_url = main_results[i].find_element_by_class_name("a-link-normal").get_attribute("href")
                        hash_tag = skill_url.split("/dp/")[1].split('/')[0]
                        total_dict[hash_tag] = {"skill_name": skill_name, "skill_page": skill_url}
                        if "department" not in total_dict[hash_tag].keys():
                            total_dict[hash_tag]["deparment"] = [department_name]
                        else:
                            total_dict[hash_tag]["deparment"].append(department_name)
                    except:
                        print("Not a skill, try jumping to next page.")
            time.sleep(1)

skills_list_file = open("./data/skill_list.txt", "w")
skills_list_file.write(json.dumps(total_dict))

