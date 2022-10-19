###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within Totems+ 
import os, shutil, getpass, json, PySimpleGUI as sg
from addons.DOC import DOC
from addons.FUNC import FUN
from addons.ADVA import ADV
from addons.ANIM import ANI
from addons.RESZ import RES

# outlines the versions and there pack formats
resourcePackformatCodes = {"1.14": 4, "1.14.1": 4, "1.14.2": 4,"1.14.3": 4,"1.14.4": 4,
                           "1.15": 5, "1.15.1": 5,"1.15.2": 5, "1.16": 5,"1.16.1": 5,
                           "1.16.2": 6, "1.16.3": 6, "1.16.4": 6, "1.16.5": 6,
                           "1.17": 7, "1.17.1": 7,
                           "1.18": 8, "1.18.1": 8, "1.18.2": 8,
                           "1.19": 9, "1.19.1": 9, "1.19.2": 9}
dataPackformatCodes = {"1.14": 4, "1.14.1": 4, "1.14.2": 4,"1.14.3": 4,"1.14.4": 4,
                       "1.15": 5, "1.15.1": 5,"1.15.2": 5, "1.16": 5,"1.16.1": 5,
                       "1.16.2": 6, "1.16.3": 6, "1.16.4": 6, "1.16.5": 6,
                       "1.17": 7, "1.17.1": 7,
                       "1.18": 8, "1.18.1": 8,
                       "1.18.2": 9,
                       "1.19": 10, "1.19.1": 10, "1.19.2": 10}

packMeta = {"pack" : {"pack_format": 0, "description": ""}}

totemJSON = {"parent" : "minecraft:item/generated", "textures": { "layer0": "minecraft:item/totem_of_undying"},"overrides":[]}

evokerJSON = {"type": "minecraft:entity", "pools": [ { "rolls": 1.0, "bonus_rolls": 0.0, "entries": [] }, { "rolls": 1.0, "bonus_rolls": 0.0, "entries": [ { "type": "minecraft:item", "functions": [ { "function": "minecraft:set_count", "count": { "type": "minecraft:uniform", "min": 0.0, "max": 1.0 }, "add": False }, { "function": "minecraft:looting_enchant", "count": { "type": "minecraft:uniform", "min": 0.0, "max": 1.0 } } ], "name": "minecraft:emerald" } ], "conditions": [ { "condition": "minecraft:killed_by_player" } ] } ] }

# defines the CMD function
def CMD(textureList, version):

    # defines how the main window will be displayed/layed-out
    layout = [
        [
            sg.Image(filename='img/windowlogo.png', key='-IMAGE-'),
            sg.Text("You've selected Totems+ CMD Integration!\n" + 
            'This integration will generate:\n' + 
            'A Custom Resource Pack\n' + 
            'A Custom Data Pack\n' + 
            'Follow the tooltip below to customize your packs!\n' + 
            ' ', font=('Helvetica', 10), justification='left'),
        ],
        [
            sg.Text('Select a world & decide to include the original Totem\n', key='tooltip')
        ],
        [
            sg.Text('World:  '),
            sg.Input(size=(25, 1), disabled=False, key="WORLD"),
            sg.FolderBrowse(initial_folder="C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/saves", disabled=False, key='worldBrowse'),
            sg.Button('Confirm', disabled=False, key='worldConfirm'),
        ],
        [
            sg.Text('Rolls:'),
            sg.Spin(values=[i for i in range(1, 100)], initial_value=1, size=(3, 1), disabled=False, key='rolls'),
            sg.Text('BonusRolls:'),
            sg.Spin(values=[i for i in range(1, 100)], initial_value=0, size=(3, 1), disabled=False, key='bonusrolls'),
            sg.Checkbox('Include Original', default=True, disabled=False, key='inc-orig', tooltip='Includes the original totem in the loot-table')
        ],
        [
            sg.Text('Name:  '),
            sg.InputText(size=(25, 1), disabled=True, key='itemName'),
            sg.Checkbox('In-Game', default=False, disabled=True, key='in-game', tooltip='Changes the dropped totem name in-game')
        ],
        [
            sg.Text('Weight:'),
            sg.Spin(values=[i for i in range(1, 100)], initial_value=1, size=(25, 1), disabled=True, key='itemWeight'),
        ],
        [
            sg.Text('Lore:    '),
            sg.InputText(size=(25, 1), disabled=True, key='lore'),
            sg.Checkbox('Lore', default=False, disabled=True, key='loreCheck',tooltip='Add custom lore to the totem item in-game')
        ],
        [
            sg.Checkbox('Documentation', default=True, disabled=True, key='documentation',tooltip='Generates a custom documentation file!'),
            sg.Checkbox('Functions', default=True, disabled=True, key='functions',tooltip='Generates functions to access all your totems!'),
            sg.Checkbox('Advancements', default=False, disabled=True, key='advancements',tooltip='Generates advancements to guide your totem experience.')
        ],
        [
            sg.Button('Next', disabled=True, key='next'),
            sg.Button('Cancel', key='cancel'),
        ],
    ]

    # creates the window
    window = sg.Window("CMD", layout, icon="img/totems.ico")

    # while window (GUI) is open
    while True:

        # read all events/actions
        event, values = window.read()

        # if window closed break while loop and end code
        if event == sg.WIN_CLOSED:
            break
        
        # if the cancel button is pressed
        if event == 'cancel':
            
            # user is asked if they are sure
            result = sg.popup_ok_cancel("Are you sure? Cancelling now will remove any current progress/packs")

            # if they are sure all created files are deleted and program is closed
            if result == "OK":
                shutil.rmtree("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)
                shutil.rmtree(worldLocation + "/datapacks/Totems+ CMD")
                break
        
        # if the confirm button (for worlds) is pressed
        if event == 'worldConfirm':

            # popup confirms if the user wishes to continue
            cmdconfirm = sg.popup_ok_cancel('Are you sure? Once confirmed datapack files will be created in your chosen world. This world then cannot be changed and cancelling will delete any data/resourcepack files', title='Are you sure?', icon="img/totems.ico")

            # if they agree then
            if cmdconfirm == 'OK':

                # updates the tooltip
                window.Element('tooltip').update('Fill out the details for each totem as they cycle in the top right.\nIt should be noted totems may appear blurred/streched here but\n wont in Minecraft. .GIF files also wont play in this release')

                # transforms the texture list into a list
                textureList = textureList.split(";")

                # if the include original box is checked then the original totem is added to the list
                if values['inc-orig'] == True:
                    textureList.append("img/totem_of_undying.png")
                
                pathList = RES(textureList)

                # updates window elements to either be enabled or disabled
                window.Element('worldBrowse').update(disabled=True)
                window.Element('WORLD').update(disabled=True)
                window.Element('worldConfirm').update(disabled=True)
                window.Element('inc-orig').update(disabled=True)
                window.Element('rolls').update(disabled=True)
                window.Element('bonusrolls').update(disabled=True)
                window.Element('itemName').update(disabled=False)
                window.Element('itemWeight').update(disabled=False)
                window.Element('next').update(disabled=False)
                window.Element('documentation').update(disabled=False)
                window.Element('functions').update(disabled=False)
                window.Element('in-game').update(disabled=False)
                window.Element('lore').update(disabled=False)
                window.Element('loreCheck').update(disabled=False)
                window.Element('advancements').update(disabled=False)

                # sets the deafult foleder name
                name = "Totems+ CMD"

                # finds all the resourcepacks you already have
                dirList = os.listdir('C:/Users/' + getpass.getuser() + '/AppData/Roaming/.minecraft/resourcepacks')

                # starts a constant repeating loop                
                repeatLoop = True
                while repeatLoop:

                    # takes the range of values
                    for i in range(len(dirList)):

                        # checks if the name is already in use and popup for rename
                        if name == dirList[i]:
                            name = sg.popup_get_text("An MCCMD Integration resource pack already exists\nPlease choose a different name for this one:", title = "Duplicate Pack")
                            break
                        
                    # else if the name is unique, end the loop
                    else:
                        repeatLoop = False

                # pre-makes the resource pack directory in the minecraft resource pack folder
                os.makedirs("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/totems")
                os.makedirs("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/totems")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/item")

                # copys the pack.png file into place
                shutil.copy("img/pack.png", "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)

                # creates & opens the pack.mcmeta file
                with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/pack.mcmeta", "w+") as packMetaFile:

                    # adds the needed meta data to the pack.mcmeta file
                    packMeta["pack"]["pack_format"] = resourcePackformatCodes[version]
                    packMeta["pack"]["description"] = (f"Version: {version}\nMade By: The Totems+ Team")
                    packMetaFile.write(json.dumps(packMeta))

                # sets the variable worldLocation to the avlues in the world selection box
                worldLocation = values["WORLD"]

                # if a datapack allready exists then an option to delete it is shown
                if os.path.exists(worldLocation + "/datapacks/Totems+ CMD"):

                    namedata = sg.PopupOKCancel("An MCCMD Integration datapack allready exists\nClick Ok to delete the existing pack", title = "Duplicate Pack")

                    if namedata == "OK":
                        shutil.rmtree(worldLocation + "/datapacks/Totems+ CMD")

                # makes datapack directories
                os.makedirs(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities")

                # copys the pack.png file into place
                shutil.copy("img/pack.png", worldLocation + "/datapacks/Totems+ CMD")

                # creates the pack.mcmeta file
                with open(worldLocation + "/datapacks/Totems+ CMD/pack.mcmeta", "w+") as packMetaFile:

                    # writes nesesary info to the pack.mcmeta file for the datapack
                    packMeta["pack"]["pack_format"] = dataPackformatCodes[version]
                    packMeta["pack"]["description"] = (f"Version: {version}\nMade By: The Totems+ Team")
                    packMetaFile.write(json.dumps(packMeta))

                # creates new lists for transfer of data to other files
                nameList, loreList, weightList, incnamelist, inclorelist = [], [], [], [], []

                # cycles the image to the first image
                window.Element('-IMAGE-').update(filename=pathList[0])

                # sets the counter to 1
                counter = 0

        # else if the next button and the length of the texture list isn't equal to the counter + 1
        elif event == 'next':

            # asks for the rename value for each file and replaceing any " " with "_"
            rename = values["itemName"].replace(" ", "_")

            # adds new CustomModel line to the totem_of_undying.json file (with comma
            totemJSON["overrides"].append({"predicate": {"custom_model_data": (910340 + counter)}, "model": (f"totems/{rename.lower()}")})

            # creates a file for the individual totem
            with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/totems/" + str(rename.lower()) + ".json", "w+") as individualTotemFile:

                # deduces the file name from its location
                textureListSplit = textureList[counter].split("/")
                TLSfilename = textureListSplit[-1].replace(".gif", ".png")

                # writes appropeiate data to the json file
                individualTotem = {"parent": "minecraft:item/generated", "textures": {"layer0": (f"minecraft:totems/{TLSfilename}")}}
                individualTotemFile.write(json.dumps(individualTotem))
            
            # if the file is a .gif file
            if textureList[counter].endswith('.gif'):
                
                # copys the new gif texture to the pack
                shutil.copy(ANI(textureList[counter], name, "MCCMD", rename), "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/totems")

            # else
            else:

                # copys the image into the resource pack
                shutil.copy(textureList[counter], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/totems")

            customModelDataKey = '{' + 'CustomModelData:' + str(910340 + counter) + '}'
            evokerJSON["pools"][0]["entries"].append({"type": "minecraft:item", "name": "minecraft:totem_of_undying", "weight": values['itemWeight'], "functions": [ { "function": "minecraft:set_nbt", "tag": str(customModelDataKey) } ] })

            # if the name is chosen to be in-game then
            if values['in-game']:
                
                evokerJSON["pools"][0]["entries"][counter]["functions"].append({"function": "minecraft:set_name", "entity": "this", "name": values['itemName']})

            # if the lore is chosen to be in-game then
            if values['loreCheck']:

                evokerJSON["pools"][0]["entries"][counter]["functions"].append({"function": "minecraft:set_lore", "entity": "this", "lore": [ { "text": values['lore']}]})

            # adds nessesary info to lists for file transfer later
            nameList.append(values["itemName"])
            weightList.append(values["itemWeight"])
            loreList.append(values["lore"])
            incnamelist.append(values["in-game"])
            inclorelist.append(values["loreCheck"])

            # increases counter by 1
            counter += 1

            if len(textureList) == counter:

                # if the documentation box remains checked
                if values['documentation'] == True:

                    # runs the documentation subroutine
                    DOC(worldLocation, nameList, weightList, incnamelist, inclorelist, loreList)

                # if the functions box remains checked
                if values['functions'] == True:

                    # runs FUN subroutine
                    FUN(worldLocation, nameList, incnamelist, inclorelist, loreList)

                # if advancements is checked
                if values['advancements'] == True:

                    totemJSON["overrides"].append({"predicate": {"custom_model_data": 910339}, "model": "totems/totemsplus"})

                    # writes adv subroutine
                    ADV(worldLocation, nameList, name)

                # finishes the totem_of_undying.json file
                with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/item/totem_of_undying.json", "w+") as totemJSONFile:
                    totemJSONFile.write(json.dumps(totemJSON))

                with open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "w+") as evokerJSONFile:
                    evokerJSONFile.write(json.dumps(evokerJSON))

                # prints completion message to user
                sg.popup_ok("Pack creation complete! Load up Minecraft and your Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="img/totems.ico")

                # breaks the loop (hence closing all windows)
                break

            # cycles the image to the next in the list
            window.Element('-IMAGE-').update(filename=pathList[counter])

            # clears the text boxes
            window.Element('itemName').update('')
            window.Element('itemWeight').update('1')
            window.Element('lore').update('')

    # closes window if called
    window.close()
