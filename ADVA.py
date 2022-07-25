import os
import getpass
import shutil

def get_size(fileobject):
        fileobject.seek(0,2)
        size = fileobject.tell()
        return size

def ADV():

    advaconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/advaconfig.txt", "r")
    advaconfigread = advaconfig.readlines()
    advaconfig.close()

    worldLocation = advaconfigread[0]
    nameList = advaconfigread[1]
    name = advaconfigread[2]

    worldLocation = worldLocation.replace('\n','')
    nameList = nameList.split(';')

    file_exists = os.path.exists(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus')

    if file_exists != True:

        os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus')

    os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements')

    ######
    
    original = 'img/totemwave.png'

    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui")
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui/advancements")

    target = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui/advancements"

    shutil.copy(original, target)

    ######

    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/root.json', 'x')
    collectall.close()

    collectall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/root.json', 'a')

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

        counter += 1
    
    fsize = get_size(collectall)
    collectall.truncate(fsize - 1)

    collectall.writelines(['\n    },\n',
    '    "parent": "totemsplus:root"\n',
    '}'])

    #####

    useall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/useall.json', 'x')
    useall.close()

    useall = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/useall.json', 'a')

    useall.writelines(['{\n',
    '    "__comment": "Made by the Totems+ Team",\n',
    '    "display": {\n',
    '        "title": {\n',
    '            "text": "Collect All Totems",\n',
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

    counter = 0

    while len(nameList) != counter + 1:

        useall.write('\n        "Use' + nameList[counter] + '": {\n')
        useall.writelines(['            "trigger": "minecraft:used_totem",\n',
        '            "conditions": {\n',
        '                "items": {\n',
        '                    "item": "minecraft:totem_of_undying",\n'])
        useall.write('                    "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
        useall.writelines(['                }\n',
        '            }\n',
        '        },'])

        counter += 1

    fsize = get_size(useall)
    useall.truncate(fsize - 1)

    useall.writelines(['\n    },\n',
    '    "parent": "totemsplus:root"\n',
    '}'])

    #####

    counter = 0

    while len(nameList) != counter + 1:

        collecttotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collect' + nameList[counter] + '.json', 'x')
        collecttotem.close()

        collecttotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collect' + nameList[counter] + '.json', 'a')

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

        counter += 1

    #####

    counter = 0

    while len(nameList) != counter + 1:

        usetotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/use' + nameList[counter] + '.json', 'x')
        usetotem.close()

        usetotem = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/use' + nameList[counter] + '.json', 'a')

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
        '                "items": [\n',
        '                    {\n',
        '                        "item": "minecraft:totem_of_undying",\n'])
        usetotem.write('                        "nbt": "{CustomModelData:' + str(910340 + counter) + '}"\n')
        usetotem.writelines(['                    }\n',
        '                ]\n',
        '            }\n',
        '        }\n',
        '    },\n',
        '    "parent": "totemsplus:useall"\n',
        '}'])
        usetotem.close()

        counter += 1