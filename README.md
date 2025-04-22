# cloud-bot

## how to use
- clone the repo
- `pip install -r requirements.txt`
- replace you own bot api

## roadmap
- text based (v1)
    - 1.1 no folders
        - sent messages will be replied by question to save or not and buttons {yes/no}✅
        - accepted ones will be added to database
        - `/number` check if message number is available in database first. if so,command will return the saved message (copy message with reply to original one) with some options buttons {delete/publicShare}. message brief will be updated in this process cause user might have been edited it.
        - share process
            - model 1: with revealing user id, e.g. $userid-$messageid
            - model 2: with a dedicated universal id for message that hides user id
    - 1.2 one layer folders
    - 1.3 recursive infinite folders
- mini-app (v2)
- fancy features (v3)
    - support for groups / channels / inline mode / link share

## to-think
- can it become an easy to use utility for channels like cinemafact to store a database and offer it to their subscribers?


## docs
### folder name
(case insensitive) a-z A-Z 0-9 dash or underscore

### address
root_folder: "/"
folderA in root_folder: "/folderA/"
fileB in folderA in root_folder: "/folderA/fileB"

note: folders end with slash