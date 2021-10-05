from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="./chrome driver/chromedriver")

driver.get("https://www.amazon.com/alexa-skills/b?ie=UTF8&node=13727921011")

lists = driver.find_elements_by_class_name("a-unordered-list")

departments = lists[1]

#print(departments.text)

departments_list = departments.find_elements_by_class_name("a-list-item")

departments_list[1].click()

################
num_skills = 0
num_policies = 0

for j in range(400):
    if j >= 0:
        num = len(driver.find_element_by_class_name("s-main-slot").find_elements_by_class_name("s-result-item"))
        for i in range(num):
            try:
                main_slot = driver.find_element_by_class_name("s-main-slot")
                main_results = main_slot.find_elements_by_class_name("s-result-item")
                intro_link = main_results[i].find_element_by_class_name("a-size-medium")
                num_skills += 1
                print(intro_link.text)
                intro_link.click()
                try:
                    policy_page = driver.find_element_by_xpath("//*[contains(text(), 'Privacy Policy')]")
                    num_policies += 1
                except:
                    print("no policy")
                driver.back()
                print(num_policies, num_skills)
                time.sleep(1)
            except:
                print("not skill")


    try:
        next_bottuon = driver.find_element_by_xpath("//*[contains(text(), 'Next')]")
        next_bottuon.click()
        time.sleep(1)
    except:
        print("end of list")



