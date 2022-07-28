###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
import os
import getpass
import shutil

# defines the get size subroutine
def get_size(fileobject):
        fileobject.seek(0,2)
        size = fileobject.tell()
        return size

# defines the advancement fucntion
def ADV(worldLocation, nameList, name):

    # checks if the totems plus directory exists and if not creates one
    if not os.path.exists(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus'):
        os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus')

    os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements')

    ######

    # creates the needed directories in the resource pack
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui")
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui/advancements")

    # coppies the file
    shutil.copy('img/totemwave.png', "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui/advancements")

    ######

    # creates the root advancement
    root = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/root.json', 'w+')

    # writes needed json to the root file
    root.writelines(['{\n',
    '    "__comment": "Made by the Totems+ Team",\n',
    '    "display": {\n',
    '        "title": {\n',
    '            "text": "Totems+",\n',
    '            "color": "gold",\n',
    '            "bold": false\n',
    '        },\n',
    '        "description": {\n',
    '            "text": "Collect your first totem!",\n',
    '            "color": "yellow"\n',
    '        },\n',
    '        "icon": {\n',
    '            "item": "minecraft:totem_of_undying"\n',
    '        },\n',
    '        "frame": "goal",\n',
    '        "show_toast": true,\n',
    '        "announce_to_chat": true,\n',
    '        "hidden": false,\n',
    '        "background": "minecraft:textures/gui/advancements/totemwave.png"\n',
    '    },\n',
    '    "criteria": {\n',
    '        "totemget": {\n',
    '            "trigger": "minecraft:inventory_changed",\n',
    '            "conditions": {\n',
    '                "items": [\n',
    '                    {\n',
    '                        "items": [\n',
    '							"minecraft:totem_of_undying"\n',
    '						]\n',
    '                    }\n',
    '                ]\n',
    '            }\n',
    '        }\n',
    '    }\n',
    '}'])

    ######

    # creates the collect all advancement
    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collectall.json', 'w+')

    # writes start un-varied meta to file
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
    '    "criteria": {'])

    # loops through name list
    for i in range(len(nameList)):

        # writes the varied meta to the file
        collectall.writelines(['\n        "Collect' + nameList[i] + '": {\n',
        '            "trigger": "minecraft:inventory_changed",\n',
        '            "conditions": {\n',
        '                "items": [\n',
        '                    {\n',
        '                        "item": "minecraft:totem_of_undying",\n'])
        collectall.write('                        "nbt": "{CustomModelData:' + str(910340 + i) + '}"\n')
        collectall.writelines(['                    }\n',
        '                ]\n',
        '            }\n',
        '        },'])
    
    # removes the last "," cuz json
    fsize = get_size(collectall)
    collectall.truncate(fsize - 1)

    # writes end un-varied meta to file
    collectall.writelines(['\n    },\n',
    '    "parent": "totemsplus:root"\n',
    '}'])

    #####

    # creates the use all advancement
    useall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/useall.json', 'w+')
  
    # writes start un-varied meta to file
    useall.writelines(['{\n',
    '    "__comment": "Made by the Totems+ Team",\n',
    '    "display": {\n',
    '        "title": {\n',
    '            "text": "Use All Totems",\n',
    '            "color": "gold",\n',
    '            "bold": true\n',
    '        },\n',
    '        "description": {\n',
    '            "text": "Use all your custom Totems!",\n',
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
    '    "criteria": {'])

    # loops through name list
    for i in range(len(nameList)):

        # writes the varied meta to the file
        useall.writelines(['\n        "Use' + nameList[i] + '": {\n',
        '            "trigger": "minecraft:used_totem",\n',
        '            "conditions": {\n',
        '                "item": {\n',
        '                    "item": "minecraft:totem_of_undying",\n'])
        useall.write('                    "nbt": "{CustomModelData:' + str(910340 + i) + '}"\n')
        useall.writelines(['                }\n',
        '            }\n',
        '        },'])

    # removes the last "," cuz json
    fsize = get_size(useall)
    useall.truncate(fsize - 1)

    # writes end un-varied meta to file
    useall.writelines(['\n    },\n',
    '    "parent": "totemsplus:root"\n',
    '}'])

    #####

    # cycles throught the name list
    for i in range(len(nameList)):

        # creates the collect totem advancement
        collecttotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collect' + nameList[counter].lower().replace(" ","_") + '.json', 'w+')

        # writes the varied meta to the file
        collecttotem.writelines(['{\n',
        '    "__comment": "Made by the Totems+ Team",\n',
        '    "display": {\n',
        '        "title": {\n',
        '            "text": "Collect ' + nameList[i] + '",\n',
        '            "color": "gold",\n',
        '            "bold": true\n',
        '        },\n',
        '        "description": {\n',
        '            "text": "Collect ' + nameList[i] + ' to add to your collection",\n',
        '            "color": "yellow"\n',
        '        },\n',
        '        "icon": {\n',
        '            "item": "minecraft:totem_of_undying",\n'])
        collecttotem.write('            "nbt": "{CustomModelData:' + str(910340 + i) + '}"\n')
        collecttotem.writelines(['        },\n',
        '        "frame": "task",\n',
        '        "show_toast": true,\n',
        '        "announce_to_chat": true,\n',
        '        "hidden": false\n',
        '    },\n',
        '    "criteria": {\n',
        '        "Collect' + nameList[i] + '": {\n',
        '            "trigger": "minecraft:inventory_changed",\n',
        '            "conditions": {\n',
        '                "items": [\n',
        '                    {\n',
        '                        "item": "minecraft:totem_of_undying",\n'])
        collecttotem.write('                        "nbt": "{CustomModelData:' + str(910340 + i) + '}"\n')
        collecttotem.writelines(['                    }\n',
        '                ]\n',
        '            }\n',
        '        }\n',
        '    },\n',
        '    "parent": "totemsplus:collectall"\n',
        '}'])
        collecttotem.close()

        # increases the counter by 1
        counter += 1

    #####

    # cycles throught the name list
    for i in range(len(nameList)):

        # creates the use totem advancement
        usetotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/use' + nameList[counter].lower().replace(" ","_") + '.json', 'w+')
 
        # writes the varied meta to the file
        usetotem.writelines(['{\n',
        '    "__comment": "Made by the Totems+ Team",\n',
        '    "display": {\n',
        '        "title": {\n',
        '            "text": "Use ' + nameList[i] + '",\n',
        '            "color": "gold",\n',
        '            "bold": true\n',
        '        },\n',
        '        "description": {\n',
        '            "text": "Use ' + nameList[i] + ' to cheat death",\n',
        '            "color": "yellow"\n',
        '        },\n',
        '        "icon": {\n',
        '            "item": "minecraft:totem_of_undying",\n'])
        usetotem.write('            "nbt": "{CustomModelData:' + str(910340 + i) + '}"\n')
        usetotem.writelines(['        },\n',
        '        "frame": "challenge",\n',
        '        "show_toast": true,\n',
        '        "announce_to_chat": true,\n',
        '        "hidden": false\n',
        '    },\n',
        '    "criteria": {\n',
        '        "Use' + nameList[i] + '": {\n',
        '            "trigger": "minecraft:used_totem",\n',
        '            "conditions": {\n',
        '                "item": {\n',
        '                    "item": "minecraft:totem_of_undying",\n'])
        usetotem.write('                    "nbt": "{CustomModelData:' + str(910340 + i) + '}"\n')
        usetotem.writelines(['                }\n',
        '            }\n',
        '        }\n',
        '    },\n',
        '    "parent": "totemsplus:useall"\n',
        '}'])
        usetotem.close()