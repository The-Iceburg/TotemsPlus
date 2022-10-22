###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
import os, getpass, shutil, json

# defines the advancement fucntion
def ADV(worldLocation, nameList, name):

    # checks if the totems plus directory exists and if not creates one
    if not os.path.exists(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus'):
        os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus')
    os.mkdir(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements')

    ######

    # creates the needed directories in the resource pack
    os.makedirs("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui/advancements")

    # coppies the file
    shutil.copy('img/totemwave.png', "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/gui/advancements")

    ######
    
    # adds the totems
    shutil.copy("img/totemsplus.png", "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/totems")

    with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/totems/totemsplus.json", "w+") as modelFile:
    
        model = {"parent": "minecraft:item/generated", "textures": {"layer0": (f"minecraft:totems/totemsplus")}}
        modelFile.write(json.dumps(model))

    # creates the root advancement
    with open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/root.json', 'w+') as rootFile:

        nbt = "{" + "CustomModelData:910339}"

        root = { "__comment": "Made by the Totems+ Team", "display": { "title": { "text": "Totems+", "color": "gold", "bold": False }, "description" : { "text": "Collect your first totem!", "color": "yellow" }, "icon": { "item": "minecraft:totem_of_undying", "nbt": nbt }, "frame": "goal", "show_toast": True, "announce_to_chat": True, "hidden": False, "background": "minecraft:textures/gui/advancements/totemwave.png" }, "criteria": { "totemget": { "trigger": "minecraft:inventory_changed", "conditions": { "items": [ { "items": [ "minecraft:totem_of_undying" ] } ] } } } }
        rootFile.write(json.dumps(root))

    ######

    # creates the collect all advancement
    with open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collectall.json', 'w+') as collectAllFile:

        collectAll = { "__comment": "Made by the Totems+ Team", "display": { "title": { "text": "Collect All Totems", "color": "gold", "bold": False }, "description" : { "text": "Collect all your custom Totems!", "color": "yellow" }, "icon": { "item": "minecraft:totem_of_undying" }, "frame": "goal", "show_toast": True, "announce_to_chat": True, "hidden": False }, "criteria": {}, "parent": "totemsplus:root" }
        for i in range(len(nameList)):

            nbt = "{CustomModelData:" + str(910340 + i) + "}"

            collectAll["criteria"][f"Collect{nameList[i]}"] = { "trigger": "minecraft:inventory_changed", "conditions": { "items": [ { "item": "minecraft:totem_of_undying", "nbt": nbt } ] } }

        collectAllFile.write(json.dumps(collectAll))

    #####

    # creates the use all advancement
    with open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/useall.json', 'w+') as useAllFile:
  
        useAll = { "__comment": "Made by the Totems+ Team", "display": { "title": { "text": "Use All Totems", "color": "gold", "bold": False }, "description" : { "text": "Use all your custom Totems!", "color": "yellow" }, "icon": { "item": "minecraft:totem_of_undying" }, "frame": "goal", "show_toast": True, "announce_to_chat": True, "hidden": False }, "criteria": {}, "parent": "totemsplus:root" }
        for i in range(len(nameList)):

            nbt = "{CustomModelData:" + str(910340 + i) + "}"

            useAll["criteria"][f"Use{nameList[i]}"] = { "trigger": "minecraft:used_totem", "conditions": { "item": { "item": "minecraft:totem_of_undying", "nbt": nbt } } }

        useAllFile.write(json.dumps(useAll))

    #####

    # cycles throught the name list
    for i in range(len(nameList)):

        # creates the collect totem advancement
        with open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/collect' + nameList[i].lower().replace(" ","_") + '.json', 'w+') as collectTotemFile:

            nbt = "{CustomModelData:" + str(910340 + i) + "}"
            collectTotem = { "__comment": "Made by the Totems+ Team", "display": { "title": { "text": (f"Collect {nameList[i]}"), "color": "gold", "bold": True }, "description" : { "text": (f"Collect {nameList[i]} to add to your collection!"), "color": "yellow" }, "icon": { "item": "minecraft:totem_of_undying", "nbt": nbt }, "frame": "task", "show_toast": True, "announce_to_chat": True, "hidden": False }, "criteria": { "totemget": { "trigger": "minecraft:inventory_changed", "conditions": { "items": [ { "item": "minecraft:totem_of_undying", "nbt": nbt } ] } } }, "parent": "totemsplus:collectall" }

            collectTotemFile.write(json.dumps(collectTotem))
    #####

    # cycles throught the name list
    for i in range(len(nameList)):

        # creates the use totem advancement+
        with open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/advancements/use' + nameList[i].lower().replace(" ","_") + '.json', 'w+') as useTotemFile:
 
            nbt = "{CustomModelData:" + str(910340 + i) + "}"
            useTotem = { "__comment": "Made by the Totems+ Team", "display": { "title": { "text": (f"Use {nameList[i]}"), "color": "gold", "bold": True }, "description" : { "text": (f"Use {nameList[i]} to cheat death"), "color": "yellow" }, "icon": { "item": "minecraft:totem_of_undying", "nbt": nbt }, "frame": "challenge", "show_toast": True, "announce_to_chat": True, "hidden": False }, "criteria": { (f"Use{nameList[i]}"): { "trigger": "minecraft:used_totem", "conditions": { "item": { "item": "minecraft:totem_of_undying", "nbt": nbt } } } }, "parent": "totemsplus:useall" }
            useTotemFile.write(json.dumps(useTotem))