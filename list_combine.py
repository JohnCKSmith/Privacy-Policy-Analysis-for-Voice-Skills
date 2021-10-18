import json

departments_list = list(map(lambda x: x.split(" : "), open("./data/departments.list", "r").read().splitlines()))
for department_tuple in departments_list:
    department_name = department_tuple[0]
    list_length = int(department_tuple[2])
    total_file_name = "./data/skills_list_in_department/"+department_name+"/total.json"
    total_dict = {}
    for num in range(list_length):
        list_file_name = "./data/skills_list_in_department/"+department_name+"/"+str(num+1)+".json"
        list_file = open(list_file_name, "r").read()
        list_dict = json.loads(list_file)
        total_dict.update(list_dict)
    total_file = open(total_file_name, "w")
    total_file.write(json.dumps(total_dict))
