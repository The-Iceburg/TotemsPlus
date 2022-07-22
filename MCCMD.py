# imports the libaries used within Totems+ 
import os
import shutil
import getpass
from tkinter.constants import S
import PySimpleGUI as sg
from DOC import DOC

# defines the CMD function
def CMD():

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
            sg.Text('Select a world below to get started!\n', key='tooltip')
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
            sg.Checkbox('Include Original', default=True, disabled=False, key='inc-orig', tooltip='Includes the original totem in the loot-table'),
            sg.Text('Weight:'),
            sg.Spin(values=[i for i in range(1, 100)], initial_value=1, size=(3, 1), disabled=False, key='orig-wei')
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
            sg.Checkbox('TotemLoad Function', default=True, disabled=True, key='totemload',tooltip='Generates a totem load function to summon all your totems!')
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
        
        # if the confirm button (for worlds) is pressed
        if event == 'worldConfirm':

            # popup confirms if the user wishes to continue
            cmdconfirm = sg.popup_ok_cancel('Are you sure? Once confirmed datapack files will be created in your chosen world. This world then cannot be changed and cancelling will delete any data/resourcepack files', title='Are you sure?', icon="img/totems.ico")

            # if they agree then
            if cmdconfirm == 'OK':
                
                # set counter to 0
                counter = 0

                # extract the textureList from the config file
                config = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/cmdconfig.txt", "r")
                textureList = config.readline()
                config.close() 
                textureList = textureList.split(";")

                # updates window elements to either be enabled or disabled
                window.Element('worldBrowse').update(disabled=True)
                window.Element('WORLD').update(disabled=True)
                window.Element('worldConfirm').update(disabled=True)
                window.Element('inc-orig').update(disabled=True)
                window.Element('orig-wei').update(disabled=True)
                window.Element('rolls').update(disabled=True)
                window.Element('bonusrolls').update(disabled=True)
                window.Element('itemName').update(disabled=False)
                window.Element('itemWeight').update(disabled=False)
                window.Element('next').update(disabled=False)
                window.Element('documentation').update(disabled=False)
                window.Element('totemload').update(disabled=False)
                window.Element('in-game').update(disabled=False)
                window.Element('lore').update(disabled=False)
                window.Element('loreCheck').update(disabled=False)

                # pre-makes the resource pack directory in the minecraft resource pack folder
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/textures")
                os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/textures/totems")

                # sets the pack.png original location & destination as variables
                originalPng = "img/pack.png"
                targetPng = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD"

                # copys the pack.png file into place
                shutil.copy(originalPng, targetPng)

                # creates the pack.mcmeta file
                packMeta = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/pack.mcmeta", "x")
                packMeta.close()

                # adds the needed meta data to the pack.mcmeta file
                packMeta = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/pack.mcmeta", "a")
                packMeta.writelines(['{',
                '  "pack": {',
                '    "pack_format": 7,',
                '	"description": "Optifine CMD Integration',
                'Made By: The Totems+ Team"',
                '  }',
                '}'])
                packMeta.close()

                # creates the totem_of_undying.json file
                totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "x")
                totemJSON.close()

                # adds the needed meta data to the totem_of_undying.json file
                totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
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

                # makes datapack directories
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/minecraft")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities")

                # TEMPORARY sets the pack.png original location & destination as variables
                originalPng = "img/pack.png"
                targetPng = worldLocation + "/datapacks/Totems+ CMD"

                # copys the pack.png file into place
                shutil.copy(originalPng, targetPng)

                # creates the pack.mcmeta file
                packMeta = open(worldLocation + "/datapacks/Totems+ CMD/pack.mcmeta", "x")
                packMeta.close()

                # adds the needed meta data to the pack.mcmeta file
                packMeta = open(worldLocation + "/datapacks/Totems+ CMD/pack.mcmeta", "a")
                packMeta.writelines(['{\n',
                '  "pack": {\n',
                '    "pack_format": 7,\n',
                '	"description": "Minecraft CMD Integration\n',
                'Made By: The Totems+ Team"\n',
                '  }\n',
                '}'])
                packMeta.close()

                # creates the evoker.json loot_table file
                evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "x")
                evokerJSON.close()

                # adds non-repatative starting data to the evoker.json file
                evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "a")
                evokerJSON.writelines(['{\n',
                '  "type": "minecraft:entity",\n',
                '  "pools": [\n',
                '    {\n'])
                evokerJSON.write('      "rolls": ' + str(values['rolls']) + '.0,\n')
                evokerJSON.write('      "bonus_rolls": ' + str(values['bonusrolls']) + '.0,\n')
                evokerJSON.write('      "entries": [\n')

                if values['inc-orig'] == True:

                    evokerJSON.writelines(['        {\n',
                    '          "type": "minecraft:item",\n',
                    '          "name": "minecraft:totem_of_undying",\n'])
                    evokerJSON.write('		  "weight": ' + str(values['orig-wei']) +'\n')
                    evokerJSON.write('        },\n')

                evokerJSON.close()

                nameList = []
                weightList = []

                # cycles the image to the first image
                window.Element('-IMAGE-').update(filename=textureList[0])

        # else if the next button and the length of the texture list isn't equal to the counter + 1
        elif event == 'next' and len(textureList) != counter + 1:

            # asks for the rename value for each file and replaceing any " " with "_"
            rename = values["itemName"]
            renameTexture = rename.replace(" ", "_")

            # adds new CustomModel line to the totem_of_undying.json file (with comma)
            totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
            totemJSON.write("\n")
            totemJSON.write('	  {"predicate": {"custom_model_data":' + str(910340 + counter) +'}, "model": "totems/'+ str(renameTexture.lower()) +'"},')
            totemJSON.close()

            # creates a file for the individual totem
            individualTotem = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems/" + str(renameTexture.lower()) + ".json", "x")
            individualTotem.close()

            # deduces the file name from its location
            count = textureList[counter].count("/")
            split_string = textureList[counter].split("/", count)
            substring = split_string[count]
                
            # adds needed meta data to the individual totem file
            individualTotem = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems/" + str(renameTexture.lower()) + ".json", "a")
            individualTotem.writelines(['{\n',
            '	"parent": "minecraft:item/generated",\n',
            '	"textures": {\n'])
            individualTotem.write('	  "layer0": "minecraft:totems/' + substring + '"')
            individualTotem.writelines(['	}\n',
            '}\n'])
            individualTotem.close()

            # copys the image into the resource pack
            original = textureList[counter]
            target = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/textures/totems"
            shutil.copy(original, target)

            # weight is equal to the user input
            weight = values['itemWeight']
            # writes the repetative data to the evoker.josn file (with comma)
            evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "a")
            evokerJSON.writelines(['        {\n',
            '          "type": "minecraft:item",\n',
            '          "name": "minecraft:totem_of_undying",\n'])
            evokerJSON.write('		  "weight": ' + str(weight) +',\n')
            evokerJSON.writelines(['		  "functions": [\n',
            '            {\n',
            '              "function": "minecraft:set_nbt",\n'])
            evokerJSON.write('              "tag": "' + '{' + 'CustomModelData:' + str(910340 + counter) + '}' + '"\n')
            evokerJSON.write('            }')

            if values['in-game'] == True:

                evokerJSON.write(',')
                evokerJSON.writelines(['\n',
                '			{\n',
                '              "function": "minecraft:set_name",\n',
                '              "entity": "this",\n'])
                evokerJSON.write('              "name": "' + values["itemName"] + '"\n')
                evokerJSON.write('			}')

            if values['loreCheck'] == True:

                evokerJSON.write(',')
                evokerJSON.writelines(['\n',
                '			{\n',
                '              "function": "minecraft:set_lore",\n',
                '              "entity": "this",\n',
                '              "lore": [\n',
                '                {\n'])
                evokerJSON.write('                  "text": "' + values['lore'] + '"\n')
                evokerJSON.writelines(['                }\n',
                '              ]\n',
                '            }'])

            evokerJSON.writelines(['\n',
            '          ]\n',
            '        },\n'])
            evokerJSON.close()

            nameList.append(values["itemName"])
            weightList.append(values["itemWeight"])

            # cycles the image to the next in the list
            window.Element('-IMAGE-').update(filename=textureList[counter + 1])

            # clears the text boxes
            window.Element('itemName').update('')
            window.Element('itemWeight').update('1')
            window.Element('lore').update('')

            # increases counter by 1
            counter += 1

        # else if the next button and the length of the texture list is equal to the counter + 1
        elif event == 'next' and len(textureList) == counter + 1:

            # asks for the rename value for each file and replaceing any " " with "_"
            rename = values["itemName"]
            renameTexture = rename.replace(" ", "_")

            # adds new CustomModel line to the totem_of_undying.json file (without comma)
            totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
            totemJSON.write("\n")
            totemJSON.write('	  {"predicate": {"custom_model_data":' + str(910340 + counter) + '}, "model": "totems/'+ str(renameTexture.lower()) +'"}\n')
            totemJSON.close()

            # creates a file for the individual totem
            individualTotem = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems/" + str(renameTexture.lower()) + ".json", "x")
            individualTotem.close()

            # deduces the file name from its location
            count = textureList[counter].count("/")
            split_string = textureList[counter].split("/", count)
            substring = split_string[count]
                
            # adds needed meta data to the individual totem file
            individualTotem = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems/" + str(renameTexture.lower()) + ".json", "a")
            individualTotem.writelines(['{\n',
            '	"parent": "minecraft:item/generated",\n',
            '	"textures": {\n'])
            individualTotem.write('	  "layer0": "minecraft:totems/' + substring + '"')
            individualTotem.writelines(['	}\n',
            '}\n'])
            individualTotem.close()

            # copys the image into the resource pack
            original = textureList[counter]
            target = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/textures/totems"
            shutil.copy(original, target)

            # weight is equal to the user input
            weight = values['itemWeight']
                
            # writes the repetative data to the evoker.josn file (without comma)
            evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "a")
            evokerJSON.writelines(['        {\n',
            '          "type": "minecraft:item",\n',
            '          "name": "minecraft:totem_of_undying",\n'])
            evokerJSON.write('		  "weight": ' + str(weight) +',\n')
            evokerJSON.writelines(['		  "functions": [\n',
            '            {\n',
            '              "function": "minecraft:set_nbt",\n'])
            evokerJSON.write('              "tag": "' + '{' + 'CustomModelData:' + str(910340 + counter) +'}' + '"\n')
            evokerJSON.write('            }')

            if values['in-game'] == True:

                evokerJSON.write(',')
                evokerJSON.writelines(['\n',
                '			{\n',
                '              "function": "minecraft:set_name",\n',
                '              "entity": "this",\n'])
                evokerJSON.write('              "name": "' + values["itemName"] + '"\n')
                evokerJSON.write('			}')

            if values['loreCheck'] == True:

                evokerJSON.write(',')
                evokerJSON.writelines(['\n',
                '			{\n',
                '              "function": "minecraft:set_lore",\n',
                '              "entity": "this",\n',
                '              "lore": [\n',
                '                {\n'])
                evokerJSON.write('                  "text": "' + values['lore'] + '"\n')
                evokerJSON.writelines(['                }\n',
                '              ]\n',
                '            }'])

            evokerJSON.writelines(['\n',
            '          ]\n',
            '        }\n'])

            nameList.append(values["itemName"])
            weightList.append(values["itemWeight"])

            # adds non-repatative ending data to the evoker.json file
            evokerJSON.writelines(['      ]\n',
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
            totemJSON = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
            totemJSON.writelines([']\n',
            '}'])
            totemJSON.close()

            if values['documentation'] == True:

                file_exists = os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/docconfig.txt')

                if file_exists == True:
                
                    os.remove("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/docconfig.txt")

                docconfig = open('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/docconfig.txt', 'x')
                docconfig.close()

                docconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/docconfig.txt", "a")

                docconfig.write(worldLocation)
                docconfig.write('\n')

                for i in nameList:
                    docconfig.write(i)
                    docconfig.write(';')
                docconfig.write('\n')
                for i in weightList:
                    docconfig.write(str(i))
                    docconfig.write(';')
                docconfig.close()

                DOC()

            if values['totemload'] == True:

                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus")
                os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus/functions")

                mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'x')
                mcfunction.close()

                mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'a')
    
                counter = 0
    
                while len(nameList) != counter:

                    mcfunction.write('give @s minecraft:totem_of_undying{CustomModelData:' + str(910340 + counter) +'} 1\n')

                    counter += 1

                mcfunction.close()

            os.remove("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/cmdconfig.txt")

            # prints completion message to user
            sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="img/totems.ico")
            
            # breaks the loop (hence closing all windows)
            break

    # closes window if called
    window.close()
    