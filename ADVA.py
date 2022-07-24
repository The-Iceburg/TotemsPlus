import os
import getpass
import shutil

def ADV():

    advaconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/advaconfig.txt", "r")
    advaconfigread = advaconfig.readlines()
    advaconfig.close()

    worldLocation = advaconfigread[0]
    nameList = advaconfigread[1]

    worldLocation = worldLocation.replace('\n','')
    nameList = nameList.split(';')

    file_exists = os.path.exists(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus')

    if file_exists != True:

        os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus')

    os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements')

    ######

    #original = 'files/root.json'
    #target = worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements'

    #shutil.copyfile(original, target)

    ######

    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collectall.json', 'x')
    collectall.close()

    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collectall.json', 'a')

    collectall.writelines(['{\n',
    '    "__comment": "Made by the Totems+ Team",\n',
    '    "display": {\n',
    '        "title": {\n',
    '            "text": "Collect All Totems",\n',
    '            "color": "gold",\n',
    '            "bold": true\n',
    '        },\n',
    '        "description": {\n',
    '            "text": "Collect all your custom Totems!",\n',
    '            "color": "yellow"\n',
    '        },\n',
    '        "icon": {\n',
    '            "item": "minecraft:totem_of_undying"\n',
    '        },\n',
    '        "frame": "goal",\n',
    '        "show_toast": true,\n',
    '        "announce_to_chat": true,\n',
    '        "hidden": false\n',
    '    },\n',
    '    "criteria": {\n'])

    counter = 0

    while len(nameList) != counter + 1:

        collectall.write('        "Collect' + nameList[counter] + '": {\n')
        collectall.writelines(['            "trigger": "minecraft:inventory_changed",\n',
        '            "conditions": {\n',
        '                "items": [\n',
        '                    {\n',
        '                        "item": "minecraft:totem_of_undying",\n'])
        collectall.write('                        "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
        collectall.writelines(['                    }\n',
        '                ]\n',
        '            }\n',
        '        },\n'])

    def get_size(fileobject):
        fileobject.seek(0,2)
        size = fileobject.tell()
        return size
    
    fsize = get_size(collectall)
    collectall.truncate(fsize - 1)

    collectall.writelines(['    },\n',
    '    "parent": "totemsplus:root"\n',
    '}'])

    #####