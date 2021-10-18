from selenium import webdriver
import time
import json

departments_list = list(reversed(list(map(lambda x: x.split(" : "), open("./data/departments.list", "r").read().splitlines()))))
for department_tuple in departments_list[4:7]:
    department_name = department_tuple[0]
    department_address = department_tuple[1]
    list_length = int(department_tuple[2])
    print(department_name, department_address, list_length)

    driver = webdriver.Chrome(executable_path="./chrome driver/chromedriver")
    driver.get(department_address)

    next_bottuon = driver.find_element_by_class_name("a-last")
    next_bottuon.click()

    base_url = driver.current_url
    target_url_list = str(base_url).split("&")

    for j in range(list_length):
        print(department_name, department_address, list_length, j)
        target_url_list[-5] = 'page=' + str(j+1)
        target_url = "&".join(target_url_list)
        print(target_url)
        if j >= 0:
            skills_list = {}
            driver.get(target_url)
            main_slot = driver.find_element_by_class_name("s-main-slot")
            main_results = main_slot.find_elements_by_class_name("s-result-item")
            for i in range(16):
                if i < len(main_results):
                    try:
                        skill_name = main_results[i].find_element_by_class_name("a-size-medium").text
                        skill_url = main_results[i].find_element_by_class_name("a-link-normal").get_attribute("href")
                        skills_list[skill_name] = skill_url
                    except:
                        print("Not a skill, try jumping to next page.")

            skills_list_file = open("./data/skills_list_in_department/"+department_name+"/"+str(j+1)+".json", "w")
            skills_list_file.write(json.dumps(skills_list))
            time.sleep(1)

    driver.close()
