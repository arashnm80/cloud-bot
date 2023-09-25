from needed_modules import *

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

def init_user_json(user_id):
    json_data = user_json_template
    json_data["user_id"] = user_id
    write_user_json(user_id, json_data)

def read_root_folder(user_id):
    json_data = read_user_json(user_id)
    root_folder = json_data["root_folder"]
    return root_folder

def write_root_folder(user_id, new_root_folder):
    user_json_path = get_user_json_path(user_id)
    new_json_data = {"user_id": user_id, 
                     "root_folder": new_root_folder}
    write_user_json(user_id, new_json_data)

