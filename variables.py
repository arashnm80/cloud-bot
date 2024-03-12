import os

jsons_folder = "./users"

cloud_bot_api = os.environ["TEST_AND_DEBUG_BOT_API"]

root_folder_addr = "/" # address of each folder starts with slash and ends with folder name

help_message = \
"""
Welcome. This bot helps you to create a cloud storage based on telegram.
you can create folders and add your messages to them with specific names.

general commands:
/help -> guide to use bot
/show -> show all folders and messages (active folder has a ✅)
/erase -> erase all messages and folders

message commands:
/add_m xxx -> add messeage to active folder (should be reply to a message)
/rem_m xxx -> remove messeage from active folder
/see_m xxx -> see message from active folder

folder commands:
/add_f xxx -> add folder to folders list
/rem_f xxx -> remove folder from folders list
/set_f xxx -> set folder as active folder
"""