from imports import *

# basic json functions

def get_user_json_path(user_id):
    user_json = str(user_id) + ".json"
    user_json_path = jsons_folder + "/" + user_json
    return user_json_path

def check_user_json_exist(user_id):
    user_json_path = get_user_json_path(user_id)
    return os.path.isfile(user_json_path) # returns true if file exists

def create_user_json(user_id):
    user_json_path = get_user_json_path(user_id)
    f = open(user_json_path, "x")
    f.close()
    json_data = user_json_template
    # json_data["user_id"] = user_id
    write_user_json(user_id, json_data)

def delete_user_json(user_id):
    user_json_path = get_user_json_path(user_id)
    os.remove(user_json_path)

def read_user_json(user_id):
    user_json_path = get_user_json_path(user_id)
    with open(user_json_path, 'r') as json_file:
        json_data = json.load(json_file)
    return json_data

def write_user_json(user_id, new_json_data):
    user_json_path = get_user_json_path(user_id)
    with open(user_json_path, 'w') as json_file:
        json.dump(new_json_data, json_file, indent=4)
    

# database json functions

def read_folder(user_id, addr):
    json_data = read_user_json(user_id)
    folder_json = json_data["root_folder"]
    addr_list = list_from_addr(addr)
    while addr_list: # as long as it has items in it
        # Pop the first item (index 0) from the addr_list
        next_folder = addr_list.pop(0)
        try:
            folder_json = folder_json[next_folder]
        except:
            raise MyErrorMessage("error in read_folder:\nnext folder doesn't exist")
    return folder_json
    

def write_folder(user_id, addr, folder_json):
    # user_json_path = get_user_json_path(user_id)
    # new_json_data = {"user_id": user_id, 
    #                  "root_folder": new_root_folder}
    # write_user_json(user_id, new_json_data)
    pass

def validate_folder_name(name):
    if name == "_":
        return False # underscore is the dedicated name for files
    pattern = r'^[a-zA-Z0-9_-]+$'
    return bool(re.match(pattern, name))

def subfolder_exists(addr, folder):
    return True # to-do: complete later

def chdir(current_addr, folder):
    if folder == "": # go to root_folder
        new_addr = "/"
    elif folder == "..": # go to upper folder
        if current_addr == "/":
            raise MyErrorMessage("can't go upper than root_folder")
        else:
            addr_list = current_addr.split("/")
            new_addr = "/".join(addr_list[:-2]) + "/"
    elif validate_folder_name(folder): # normal folder name has been passed
        if subfolder_exists(current_addr, folder):
            new_addr = current_addr + folder + "/"
        else:
            raise MyErrorMessage("subfolder doesn't exist")
    else:
        raise MyErrorMessage("Invalid folder name")

    return new_addr # to-do: change to better method later

def json_from_folder_addr(addr):
    pass # to-do


# addr functions

def list_from_addr(addr):
    if addr == "/":
        return [] # root folder
    else:
        addr = addr.strip("/") # remove slashes from beginning and end
        addr_list = addr.split("/")
        return addr_list

def addr_from_list(addr_list):
    if addr_list == []:
        return "/" # root folder
    else:
        addr = "/" + "/".join(addr_list)
        return addr
    
def read_folder_from_user_json(user_id, addr):
    json_data = read_user_json(user_id)
    root_folder = json_data["root_folder"]
    pointer = jsonpointer.JsonPointer(addr)
    try:
        folder = pointer.resolve(root_folder)
        return folder
    except jsonpointer.JsonPointerException as e:
        raise MyErrorMessage("JSON Pointer not found.")

def write_folder_to_user_json(user_id, addr, folder_json):
    json_data = read_user_json(user_id)
    root_folder = json_data["root_folder"]
    pointer = jsonpointer.JsonPointer(addr)
    try:
        parent_pointer = pointer[:-1]
        parent_data = parent_pointer.resolve(json_data)
        parent_data[pointer[-1]] = folder_json
    except jsonpointer.JsonPointerException as e:
        raise MyErrorMessage("JSON Pointer not found.")


################################ v1.1


# # show case

# if __name__ == "__main__":
#     input = "/dog/cat/hello/goodbye/"
#     input = "/"

#     json_data = {
#         "person": {
#             "name": {
#                 "first": "John",
#                 "last": "Doe"
#             },
#             "age": 30
#         }
#     }
#     test_path = "/person/name/"

#     output = list_from_addr(input)
#     print(output)
#     output = addr_from_list(output)
#     print(output)

#     # output = read_folder_from_user_json(, test_path)
#     print(output)