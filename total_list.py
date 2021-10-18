import json

departments_list = list(map(lambda x: x.split(" : "), open("./data/departments.list", "r").read().splitlines()))
total_file_name = "./data/skills_list_in_department/total.json"
total_dict = {}
for department_tuple in departments_list:
    department_name = department_tuple[0]
    department_list_file = open("./data/skills_list_in_department/" + department_name + "/total.json", "r").read()
    total_dict.update(json.loads(department_list_file))
    print(department_name)
total_file = open(total_file_name, "w")
total_file.write(json.dumps(total_dict))

