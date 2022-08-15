###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within Totems+ 
import os, shutil, getpass, PySimpleGUI as sg
from PIL import Image
from DOC import DOC
from FUNC import FUN
from ADVA import ADV
from ANIM import ANI

# outlines the versions and there pack formats
resourcepackFormat4 = ["1.14","1.14.1","1.14.2","1.14.3","1.14.4"]
resourcepackFormat5 = ["1.15","1.15.1","1.15.2","1.16","1.16.1"]
resourcepackFormat6 = ["1.16.2","1.16.3","1.16.4","1.16.5"]
datapackFormat4 = ["1.14","1.14.1","1.14.2","1.14.3","1.14.4"]
datapackFormat5 = ["1.15","1.15.1","1.15.2","1.16","1.16.1"]
datapackFormat6 = ["1.16.2","1.16.3","1.16.4","1.16.5"]
datapackFormat8 = ["1.18","1.18.1"]

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
                
                # if the directory resized already exists, then delete it
                if os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/resized'):
                    shutil.rmtree('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/resized')

                # make the resized folder
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/resized")

                # new list to hold the new file names
                pathList = []

                # for loop for each image
                for i in range(len(textureList)):

                    # the first image gets opened
                    origIMG = str(open(textureList[i]))

                    # removes the leading and prior words
                    origIMG = origIMG.replace("<_io.TextIOWrapper name='", "")
                    origIMG = origIMG.replace("' mode='r' encoding='cp1252'>", "")

                    # finds only the names
                    splitList = textureList[i].split("/")

                    # the path for the resized folder
                    targetIMG = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/resized"

                    # copies the images to the resized folder
                    shutil.copy(origIMG, targetIMG)
                    IMGpath = targetIMG + "/" + splitList[-1]

                    # opens the new image path
                    openIMG = Image.open(IMGpath)
                    
                    # resizes the image, and saves with a new name
                    resizedIMG = openIMG.resize((128,128))
                    fileName1 = "resize_" + str(splitList[-1]) 
                    resizedIMG.save(fileName1)

                    # moves to the resized folder and saves the path to the path list 
                    shutil.move(fileName1, targetIMG)
                    fileName2 = targetIMG + "/" + fileName1
                    pathList.append(fileName2)

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

                # checks if the folder exists and if itdoes user is prompted to choose their own name
                if os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD'):
                    name = sg.popup_get_text("An MCCMD Integration resource pack allready exists\nPlease choose a different name for this one:", title = "Duplicate Pack")

                # pre-makes the resource pack directory in the minecraft resource pack folder
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/item")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/totems")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/totems")

                # copys the pack.png file into place
                shutil.copy("img/pack.png", "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)

                # creates the pack.mcmeta file
                packMeta = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/pack.mcmeta", "w+")

                # derives the packformat code from
                if version in resourcepackFormat4:
                    packformat = 4
                elif version in resourcepackFormat5:
                    packformat = 5
                elif version in resourcepackFormat6:
                    packformat = 6
                elif version.startswith("1.17"):
                    packformat = 7
                elif version.startswith("1.18"):
                    packformat = 8
                elif version.startswith("1.19"):
                    packformat = 9

                # adds the needed meta data to the pack.mcmeta file
                packMeta.writelines(['{',
                '  "pack": {',
                '    "pack_format": ' + str(packformat) + ',',
                '	"description": "Version: ' + version + '\n',
                'Made By: The Totems+ Team"',
                '  }',
                '}'])
                packMeta.close()

                # creates the totem_of_undying.json file
                totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/item/totem_of_undying.json", "w+")
                totemJSON.writelines(['{\n',
                '  "parent": "minecraft:item/generated",\n',
                '  "textures": {\n',
                '    "layer0": "minecraft:item/totem_of_undying"\n',
                '  },\n',
                '"overrides":\n',
                '['])
                totemJSON.close()

                # sets the variable worldLocation to the avlues in the world selection box
                worldLocation = values["WORLD"]

                # if a datapack allready exists then an option to delete it is shown
                if os.path.exists(worldLocation + "/datapacks/Totems+ CMD"):

                    namedata = sg.PopupOKCancel("An MCCMD Integration datapack allready exists\nClick Ok to delete the existing pack", title = "Duplicate Pack")

                    if namedata == "OK":
                        shutil.rmtree(worldLocation + "/datapacks/Totems+ CMD")

                # makes datapack directories
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/minecraft")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities")

                # copys the pack.png file into place
                shutil.copy("img/pack.png", worldLocation + "/datapacks/Totems+ CMD")

                # creates the pack.mcmeta file
                packMeta = open(worldLocation + "/datapacks/Totems+ CMD/pack.mcmeta", "w+")

                # derives the packformat code from
                if version in datapackFormat4:
                    datapackformat = 4
                elif version in datapackFormat5:
                    datapackformat = 5
                elif version in datapackFormat6:
                    datapackformat = 6
                elif version.startswith("1.17"):
                    datapackformat = 7
                elif version in datapackFormat8:
                    datapackformat = 8
                elif version == "1.18.2":
                    datapackformat = 9
                elif version.startswith("1.19"):
                    datapackformat = 10

                # adds the needed meta data to the pack.mcmeta file
                packMeta.writelines(['{\n',
                '  "pack": {\n',
                '    "pack_format": ' + str(datapackformat) + ',\n',
                '	"description": "Version: ' + version + '\n',
                'Made By: The Totems+ Team"\n',
                '  }\n',
                '}'])
                packMeta.close()

                # creates the evoker.json loot_table file
                evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "w+")

                # adds non-repatative starting data to the evoker.json file
                evokerJSON.writelines(['{\n',
                '  "type": "minecraft:entity",\n',
                '  "pools": [\n',
                '    {\n',
                '      "rolls": ' + str(values['rolls']) + '.0,\n',
                '      "bonus_rolls": ' + str(values['bonusrolls']) + '.0,\n',
                '      "entries": [\n'])
                evokerJSON.close()

                # creates new lists for transfer of data to other files
                nameList = []
                loreList = []
                weightList = []
                incnamelist = []
                inclorelist = []

                # cycles the image to the first image
                window.Element('-IMAGE-').update(filename=pathList[0])

                # sets the counter to 1
                counter = 0

        # else if the next button and the length of the texture list isn't equal to the counter + 1
        elif event == 'next' and len(textureList) != counter + 1:

            # asks for the rename value for each file and replaceing any " " with "_"
            rename = values["itemName"].replace(" ", "_")

            # adds new CustomModel line to the totem_of_undying.json file (with comma)
            totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/item/totem_of_undying.json", "a")
            totemJSON.writelines("\n")
            totemJSON.write('	  {"predicate": {"custom_model_data":' + str(910340 + counter) +'}, "model": "totems/'+ str(rename.lower()) +'"},')
            totemJSON.close()

            # creates a file for the individual totem
            individualTotem = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/totems/" + str(rename.lower()) + ".json", "w+")

            # deduces the file name from its location
            textureListSplit = textureList[counter].split("/")
            TLSfilename = textureListSplit[-1].replace(".gif", ".png")
            
            # adds needed meta data to the individual totem file
            individualTotem.writelines(['{\n',
            '	"parent": "minecraft:item/generated",\n',
            '	"textures": {\n',
            '	  "layer0": "minecraft:totems/' + TLSfilename + '"',
            '	}\n',
            '}\n'])
            individualTotem.close()
            
            # if the file is a .gif file
            if textureList[counter].endswith('.gif'):
                
                
                # copys the new gif texture to the pack
                shutil.copy(ANI(textureList[counter], name, "MCCMD", rename), "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/totems")

            # else
            else:

                # copys the image into the resource pack
                shutil.copy(textureList[counter], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/totems")

            # writes the repetative data to the evoker.josn file (with comma)
            evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "a")
            evokerJSON.writelines(['        {\n',
            '          "type": "minecraft:item",\n',
            '          "name": "minecraft:totem_of_undying",\n',
            '		  "weight": ' + str(values['itemWeight']) +',\n',
            '		  "functions": [\n',
            '            {\n',
            '              "function": "minecraft:set_nbt",\n'])
            evokerJSON.write('              "tag": "' + '{' + 'CustomModelData:' + str(910340 + counter) + '}' + '"\n')
            evokerJSON.write('            }')

            # if the name is chosen to be in-game then
            if values['in-game']:
                
                # sets the item name to value the user entered
                evokerJSON.writelines([',\n',
                '			{\n',
                '              "function": "minecraft:set_name",\n',
                '              "entity": "this",\n',
                '              "name": "' + values["itemName"] + '"\n',
                '			}'])

            # if the lore is chosen to be in-game then
            if values['loreCheck']:

                # sets the lore to value the user entered
                evokerJSON.writelines([',\n',
                '			{\n',
                '              "function": "minecraft:set_lore",\n',
                '              "entity": "this",\n',
                '              "lore": [\n',
                '                {\n',
                '                  "text": "' + values['lore'] + '"\n',
                '                }\n',
                '              ]\n',
                '            }'])

            # writes final info to evoker loot_tabel
            evokerJSON.writelines(['\n',
            '          ]\n',
            '        },\n'])
            evokerJSON.close()

            # adds nessesary info to lists for file transfer later
            nameList.append(values["itemName"])
            weightList.append(values["itemWeight"])
            loreList.append(values["lore"])
            incnamelist.append(values["in-game"])
            inclorelist.append(values["loreCheck"])

            # cycles the image to the next in the list
            window.Element('-IMAGE-').update(filename=pathList[counter + 1])

            # clears the text boxes
            window.Element('itemName').update('')
            window.Element('itemWeight').update('1')
            window.Element('lore').update('')

            # increases counter by 1
            counter += 1

        # else if the next button and the length of the texture list is equal to the counter + 1
        elif event == 'next' and len(textureList) == counter + 1:

            # asks for the rename value for each file and replaceing any " " with "_"
            rename = values["itemName"].replace(" ", "_")

            # adds new CustomModel line to the totem_of_undying.json file (without comma)
            totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/item/totem_of_undying.json", "a")
            totemJSON.write("\n")
            totemJSON.write('	  {"predicate": {"custom_model_data":' + str(910340 + counter) + '}, "model": "totems/'+ str(rename.lower()) +'"}\n')
            totemJSON.close()

            # creates a file for the individual totem
            individualTotem = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/totems/" + str(rename.lower()) + ".json", "w+")

            # deduces the file name from its location
            textureListSplit = textureList[counter].split("/")
            TLSfilename = textureListSplit[-1].replace(".gif", ".png")
            
            # adds needed meta data to the individual totem file
            individualTotem.writelines(['{\n',
            '	"parent": "minecraft:item/generated",\n',
            '	"textures": {\n',
            '	  "layer0": "minecraft:totems/' + TLSfilename + '"',
            '	}\n',
            '}\n'])
            individualTotem.close()

            shutil.copy(textureList[counter], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/totems")
                
            # writes the repetative data to the evoker.josn file (without comma)
            evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "a")
            evokerJSON.writelines(['        {\n',
            '          "type": "minecraft:item",\n',
            '          "name": "minecraft:totem_of_undying",\n',
            '		  "weight": ' + str(values['itemWeight']) +',\n',
            '		  "functions": [\n',
            '            {\n',
            '              "function": "minecraft:set_nbt",\n'])
            evokerJSON.write('              "tag": "' + '{' + 'CustomModelData:' + str(910340 + counter) +'}' + '"\n')
            evokerJSON.write('            }')

            # if the name is chosen to be in-game then
            if values['in-game'] == True:

                # sets the item name to value the user entered
                evokerJSON.write(',')
                evokerJSON.writelines(['\n',
                '			{\n',
                '              "function": "minecraft:set_name",\n',
                '              "entity": "this",\n',
                '              "name": "' + values["itemName"] + '"\n',
                '			}'])

            # if the lore is chosen to be in-game then
            if values['loreCheck'] == True:

                # sets the lore to value the user entered
                evokerJSON.write(',')
                evokerJSON.writelines(['\n',
                '			{\n',
                '              "function": "minecraft:set_lore",\n',
                '              "entity": "this",\n',
                '              "lore": [\n',
                '                {\n',
                '                  "text": "' + values['lore'] + '"\n',
                '                }\n',
                '              ]\n',
                '            }'])

            # adds nessesary info to lists for file transfer later
            nameList.append(values["itemName"])
            loreList.append(values["lore"])
            weightList.append(values["itemWeight"])
            incnamelist.append(values["in-game"])
            inclorelist.append(values["loreCheck"])

            # adds non-repatative ending data to the evoker.json file
            evokerJSON.writelines(['\n',
            '          ]\n',
            '        }\n',
            '      ]\n',
            '    },\n',
            '    {\n',
            '      "rolls": 1.0,\n',
            '      "bonus_rolls": 0.0,\n',
            '      "entries": [\n',
            '        {\n',
            '          "type": "minecraft:item",\n',
            '          "functions": [\n',
            '            {\n',
            '              "function": "minecraft:set_count",\n',
            '              "count": {\n',
            '                "type": "minecraft:uniform",\n',
            '                "min": 0.0,\n',
            '                "max": 1.0\n',
            '              },\n',
            '              "add": false\n',
            '            },\n',
            '            {\n',
            '              "function": "minecraft:looting_enchant",\n',
            '              "count": {\n',
            '                "type": "minecraft:uniform",\n',
            '                "min": 0.0,\n',
            '                "max": 1.0\n',
            '              }\n',
            '            }\n',
            '          ],',
            '          "name": "minecraft:emerald"\n',
            '        }\n',
            '      ],\n',
            '      "conditions": [\n',
            '        {\n',
            '          "condition": "minecraft:killed_by_player"\n',
            '        }\n',
            '      ]\n',
            '    }\n',
            '  ]\n',
            '}'])
            evokerJSON.close()

            # finishes the totem_of_undying.json file
            totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/models/item/totem_of_undying.json", "a")
            totemJSON.writelines([']\n',
            '}'])
            totemJSON.close()

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

                # writes adv subroutine
                ADV(worldLocation, nameList, name)

            # prints completion message to user
            sg.popup_ok("Pack creation complete! Load up Minecraft and your Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="img/totems.ico")
            
            # breaks the loop (hence closing all windows)
            break

    # closes window if called
    window.close()
    