user_json_template = \
{
    "user_id": "",
    "root_folder": { # can be empty - root folder doesn't have 'folder_name'
        "sub_folders": [
            # "folder1_name": {},
            # "folder2_name": {}
        ],
        "sub_messages":[
            # "message1_id": {},
            # "message2_id": {}
        ]
    }
}

# key for folder json is the folder name
folder_json_template = \
{
    "sub_folders": [ # can be empty

    ],
    "sub_messages": [ # can be empty

    ]
}

# key for message json is the message id
message_json_template = \
{
    # empty for now
}