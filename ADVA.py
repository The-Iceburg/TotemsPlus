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
def ADV():

    # grabs info from from the advaconfig file
    advaconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/advaconfig.txt", "r")
    advaconfigread = advaconfig.readlines()
    advaconfig.close()

    # sorts info into appropriate variables
    worldLocation = advaconfigread[0]
    nameList = advaconfigread[1]
    name = advaconfigread[2]

    # creates lists with nessesary values
    worldLocation = worldLocation.replace('\n','')
    nameList = nameList.split(';')

    # checks if the totems plus directory exists and if not creates one
    file_exists = os.path.exists(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus')

    if file_exists != True:

        os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus')

    os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements')

    ######
    
    # sets the backround image to the original variable
    original = 'img/totemwave.png'

    # creates the needed directories in the resource pack
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui")
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui/advancements")

    # sets the target destination
    target = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui/advancements"

    # coppies the file
    shutil.copy(original, target)

    ######

    # creates the root advancement
    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/root.json', 'x')
    collectall.close()

    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/root.json', 'a')

    # writes needed json to the root file
    collectall.writelines(['{\n',
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
    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collectall.json', 'x')
    collectall.close()

    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collectall.json', 'a')

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
    '    "criteria": {\n'])

    # sets the counter to 0
    counter = 0

    # loops through name list
    while len(nameList) != counter + 1:

        # writes the varied meta to the file
        collectall.write('\n        "Collect' + nameList[counter] + '": {\n')
        collectall.writelines(['            "trigger": "minecraft:inventory_changed",\n',
        '            "conditions": {\n',
        '                "items": [\n',
        '                    {\n',
        '                        "item": "minecraft:totem_of_undying",\n'])
        collectall.write('                        "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
        collectall.writelines(['                    }\n',
        '                ]\n',
        '            }\n',
        '        },'])

        # increases the counter by 1
        counter += 1
    
    # removes the last "," cuz json
    fsize = get_size(collectall)
    collectall.truncate(fsize - 1)

    # writes end un-varied meta to file
    collectall.writelines(['\n    },\n',
    '    "parent": "totemsplus:root"\n',
    '}'])

    #####

    # creates the use all advancement
    useall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/useall.json', 'x')
    useall.close()

    useall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/useall.json', 'a')

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
    '    "criteria": {\n'])

    # re-sets counter to 0
    counter = 0

    # loops through name list
    while len(nameList) != counter + 1:

        # writes the varied meta to the file
        useall.write('\n        "Use' + nameList[counter] + '": {\n')
        useall.writelines(['            "trigger": "minecraft:used_totem",\n',
        '            "conditions": {\n',
        '                "item": {\n',
        '                    "item": "minecraft:totem_of_undying",\n'])
        useall.write('                    "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
        useall.writelines(['                }\n',
        '            }\n',
        '        },'])

        # increases the counter by 1
        counter += 1

    # removes the last "," cuz json
    fsize = get_size(useall)
    useall.truncate(fsize - 1)

    # writes end un-varied meta to file
    useall.writelines(['\n    },\n',
    '    "parent": "totemsplus:root"\n',
    '}'])

    #####

    # re-sets the counter to 0
    counter = 0

    # cycles throught the name list
    while len(nameList) != counter + 1:

        # creates the collect totem advancement
        collecttotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collect' + nameList[counter].lower().replace(" ","_") + '.json', 'x')
        collecttotem.close()

        collecttotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collect' + nameList[counter].lower().replace(" ","_") + '.json', 'a')

        # writes the varied meta to the file
        collecttotem.writelines(['{\n',
        '    "__comment": "Made by the Totems+ Team",\n',
        '    "display": {\n',
        '        "title": {\n'])
        collecttotem.write('            "text": "Collect ' + nameList[counter] + '",\n')
        collecttotem.writelines(['            "color": "gold",\n',
        '            "bold": true\n',
        '        },\n',
        '        "description": {\n'])
        collecttotem.write('            "text": "Collect ' + nameList[counter] + ' to add to your collection",\n')
        collecttotem.writelines(['            "color": "yellow"\n',
        '        },\n',
        '        "icon": {\n',
        '            "item": "minecraft:totem_of_undying",\n'])
        collecttotem.write('            "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
        collecttotem.writelines(['        },\n',
        '        "frame": "task",\n',
        '        "show_toast": true,\n',
        '        "announce_to_chat": true,\n',
        '        "hidden": false\n',
        '    },\n',
        '    "criteria": {\n'])
        collecttotem.write('        "Collect' + nameList[counter] + '": {\n')
        collecttotem.writelines(['            "trigger": "minecraft:inventory_changed",\n',
        '            "conditions": {\n',
        '                "items": [\n',
        '                    {\n',
        '                        "item": "minecraft:totem_of_undying",\n'])
        collecttotem.write('                        "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
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

    # re-sets the counter to 0
    counter = 0

    # cycles throught the name list
    while len(nameList) != counter + 1:

        # creates the use totem advancement
        usetotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/use' + nameList[counter].lower().replace(" ","_") + '.json', 'x')
        usetotem.close()

        usetotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/use' + nameList[counter].lower().replace(" ","_") + '.json', 'a')

        # writes the varied meta to the file
        usetotem.writelines(['{\n',
        '    "__comment": "Made by the Totems+ Team",\n',
        '    "display": {\n',
        '        "title": {\n'])
        usetotem.write('            "text": "Use ' + nameList[counter] + '",\n')
        usetotem.writelines(['            "color": "gold",\n',
        '            "bold": true\n',
        '        },\n',
        '        "description": {\n'])
        usetotem.write('            "text": "Use ' + nameList[counter] + ' to cheat death",\n')
        usetotem.writelines(['            "color": "yellow"\n',
        '        },\n',
        '        "icon": {\n',
        '            "item": "minecraft:totem_of_undying",\n'])
        usetotem.write('            "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
        usetotem.writelines(['        },\n',
        '        "frame": "challenge",\n',
        '        "show_toast": true,\n',
        '        "announce_to_chat": true,\n',
        '        "hidden": false\n',
        '    },\n',
        '    "criteria": {\n'])
        usetotem.write('        "Use' + nameList[counter] + '": {\n')
        usetotem.writelines(['            "trigger": "minecraft:used_totem",\n',
        '            "conditions": {\n',
        '                "item": {\n',
        '                    "item": "minecraft:totem_of_undying",\n'])
        usetotem.write('                    "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
        usetotem.writelines(['                }\n',
        '            }\n',
        '        }\n',
        '    },\n',
        '    "parent": "totemsplus:useall"\n',
        '}'])
        usetotem.close()

        # increases the counter by 1
        counter += 1