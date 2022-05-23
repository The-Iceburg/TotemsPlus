# imports the libaries used within Totems+ 
from itertools import count
import os
import shutil
from tkinter.constants import S
import PySimpleGUI as sg

# sets window theme
sg.theme('DarkTeal10')

def CMD():

    # defines how the main window will be displayed/layed-out
    layout = [ 
        [
            sg.Image(filename='AppData/Roaming/Totems +/windowlogo.png', key='-IMAGE-'),
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
            sg.FolderBrowse(initial_folder="AppData/Roaming/.minecraft/saves", disabled=False, key='worldBrowse'),
            sg.Button('Confirm', disabled=False, key='worldConfirm'),
        ],
        [
            sg.Text('Name:  '),
            sg.InputText(size=(25, 1), disabled=True, key='itemName'),
        ],
        [
            sg.Text('Weight:'),
            sg.InputText(size=(25, 1), disabled=True, key='itemWeight'),
        ],
        [
            sg.Button('Next', disabled=True, key='next'),
            sg.Button('Cancel', key='cancel'),
        ],
    ]

    # creates the window
    window = sg.Window("CMD", layout, icon="AppData/Roaming/Totems +/totems.ico")

    # while window (GUI) is open
    while True:

        # read all events/actions
        event, values = window.read()

        # if window closed break while loop and end code
        if event == sg.WIN_CLOSED:
            break

        if event == 'worldConfirm':

            cmdconfirm = sg.popup_ok_cancel('Are you sure? Once confirmed datapack files will be created in your chosen world. This world then cannot be changed and cancelling will delete any data/resourcepack files', title='Are you sure?', icon="AppData/Roaming/Totems +/totems.ico")

            if cmdconfirm == 'OK':

                counter = 0
        
                config = open("AppData/Roaming/Totems +/cmdconfig.txt", "r")
                textureList = config.readline()
                config.close() 
                textureList = textureList.split(";")

                window.Element('worldBrowse').update(disabled=True)
                window.Element('WORLD').update(disabled=True)
                window.Element('worldConfirm').update(disabled=True)
                window.Element('itemName').update(disabled=False)
                window.Element('itemWeight').update(disabled=False)
                window.Element('next').update(disabled=False)

                # pre-makes the resource pack directory in the minecraft resource pack folder
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD")
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets")
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft")
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models")
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item")
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems")
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/textures")
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/textures/totems")

                # TEMPORARY sets the pack.png original location & destination as variables
                originalPng = "AppData/Roaming/Totems +/pack.png"
                targetPng = "AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD"

                # copys the pack.png file into place
                shutil.copy(originalPng, targetPng)

                # creates the pack.mcmeta file
                packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/pack.mcmeta", "x")
                packMeta.close()

                # adds the needed meta data to the pack.mcmeta file
                packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/pack.mcmeta", "a")
                packMeta.writelines(['{',
                '  "pack": {',
                '    "pack_format": 7,',
                '	"description": "Optifine CMD Integration',
                'Made By: The Totems+ Team"',
                '  }',
                '}'])
                packMeta.close()

                # creates the totem_of_undying.json file
                totemJSON = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "x")
                totemJSON.close()

                # adds the needed meta data to the totem_of_undying.json file
                totemJSON = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
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
                originalPng = "AppData/Roaming/Totems +/pack.png" # NEEDS UPDATING
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
                '    {\n',
                '      "rolls": 1.0,\n',
                '      "bonus_rolls": 0.0,\n',
                '      "entries": [\n']),
                evokerJSON.close()

                window.Element('-IMAGE-').update(filename=textureList[0])

        elif event == 'next' and len(textureList) != int(counter + 1):

            # asks for the rename value for each file and replaceing any " " with "_"
            rename = values["itemName"]
            renameTexture = rename.replace(" ", "_")

            # if counter != length of the texture list (-1) then
            if counter != len(textureList) - 1:

                # adds new CustomModel line to the totem_of_undying.json file (with comma)
                totemJSON = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
                totemJSON.write("\n")
                totemJSON.write('	  {"predicate": {"custom_model_data":91034'+ str(counter) +'}, "model": "totems/'+ str(renameTexture.lower()) +'"},')
                totemJSON.close

            # else then
            else:

                # adds new CustomModel line to the totem_of_undying.json file (without comma)
                totemJSON = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
                totemJSON.write("\n")
                totemJSON.write('	  {"predicate": {"custom_model_data":91034'+ str(counter) +'}, "model": "totems/'+ str(renameTexture.lower()) +'"}')
                totemJSON.close

            # creates a file for the individual totem
            individualTotem = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems/" + str(renameTexture.lower()) + ".json", "x")
            individualTotem.close()

            # deduces the file name from its location
            count = textureList[counter].count("/")
            split_string = textureList[counter].split("/", count)
            substring = split_string[count]
                
            # adds needed meta data to the individual totem file
            individualTotem = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems/" + str(renameTexture.lower()) + ".json", "a")
            individualTotem.writelines(['{\n',
            '	"parent": "minecraft:item/generated",\n',
            '	"textures": {\n'])
            individualTotem.write('	  "layer0": "minecraft:totems/' + substring + '"')
            individualTotem.writelines(['	}\n',
            '}\n'])
            individualTotem.close()

            # copys the image into the resource pack
            original = textureList[counter]
            target = "AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/textures/totems"
            shutil.copy(original, target)

            # if counter != length of the texture list (-1) then
            if counter != len(textureList) - 1:
                    
                weight = values['itemWeight']

                # writes the repetative data to the evoker.josn file (with comma)
                evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "a")
                evokerJSON.writelines(['        {\n',
                '          "type": "minecraft:item",\n',
                '          "name": "minecraft:totem_of_undying",\n'])
                evokerJSON.write('		  "weight": ' + weight +',\n')
                evokerJSON.writelines(['		  "functions": [\n',
                '            {\n',
                '              "function": "minecraft:set_nbt",\n'])
                evokerJSON.write('              "tag": "' + '{' + 'CustomModelData:' + '91034'+ str(counter) + '}' + '"\n')
                evokerJSON.writelines(['            }\n',
                '          ]\n',
                '        },\n'])

            # else then
            else:
                    
                weight = values['itemWeight']
                    
                # writes the repetative data to the evoker.josn file (without comma)
                evokerJSON = open(worldLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "a")
                evokerJSON.writelines(['        {\n',
                '          "type": "minecraft:item",\n',
                '          "name": "minecraft:totem_of_undying",\n'])
                evokerJSON.write('		  "weight": ' + weight +',\n')
                evokerJSON.writelines(['		  "functions": [\n',
                '            {\n',
                '              "function": "minecraft:set_nbt",\n'])
                evokerJSON.write('              "tag": "' + '{' + 'CustomModelData:' + '91034'+ str(counter) + '}' + '"\n')
                evokerJSON.writelines(['            }\n',
                '          ]\n',
                '        }\n'])

            window.Element('-IMAGE-').update(filename=textureList[counter + 1])
            window.Element('itemName').update('')
            window.Element('itemWeight').update('')

            # increases counter by 1
            counter = counter + 1

        elif event == 'next' and len(textureList) == counter + 1:

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
            totemJSON = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
            totemJSON.writelines([']\n',
            '}'])
            totemJSON.close()
            os.remove("AppData/Roaming/Totems +/cmdconfig.txt")
            # prints completion message to user
            sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="AppData/Roaming/Totems +/totems.ico")
            # breaks the loop (hence closing all windows)
            break

    # closes window if called
    window.close()

def CIT():

    counter = 0
    config = open("AppData/Roaming/Totems +/citconfig.txt", "r")
    textureList = config.readline()
    config.close() 
    textureList = textureList.split(";")

    # defines how the main window will be displayed/layed-out
    layout = [ 
        [
            sg.Image(filename=textureList[0], key='-IMAGE-'),
            sg.Text("You've selected Totems+ CIT Integration!\n" + 
            'This integration will generate:\n' + 
            'A Custom Resource Pack\n' + 
            'Follow the tooltip below to customize your packs!\n' + 
            ' ', font=('Helvetica', 10), justification='left'),
        ],
        [
            sg.Text('Rename your different textures to what you wish to rename them in-game\n', key='tooltip')
        ],
        [
            sg.Text('Name:  '),
            sg.InputText(size=(25, 1), key='itemName'),
        ],
        [
            sg.Button('Next', key='next'),
            sg.Button('Cancel', key='cancel'),
        ],
    ]

    # creates the window
    window = sg.Window("CMD", layout, icon="AppData/Roaming/Totems +/totems.ico")

    # pre-makes the resource pack directory in the minecraft resource pack folder
    os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT")
    os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets")
    os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft")
    os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine")
    os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit")
    os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems")

    # TEMPORARY sets the pack.png original location & destination as variables
    originalPng = "AppData/Roaming/Totems +/pack.png"
    targetPng = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT"

    # copys the pack.png file into place
    shutil.copy(originalPng, targetPng)

    # creates the pack.mcmeta file
    packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/pack.mcmeta", "x")
    packMeta.close()

    # adds the needed meta data to the pack.mcmeta file
    packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/pack.mcmeta", "a")
    packMeta.writelines(['{\n',
    '  "pack": {\n',
    '    "pack_format": 7,\n',
    '	"description": "Optifine CIT Integration\n',
    'Made By: The Totems+ Team"\n',
    '  }\n',
    '}'])
    packMeta.close()

    # while window (GUI) is open
    while True:

        # read all events/actions
        event, values = window.read()

        # if window closed break while loop and end code
        if event == sg.WIN_CLOSED:
            break

        elif event == 'next' and len(textureList) != int(counter + 1):

            rename = values["itemName"]
            renameTexture = rename.replace(" ", "_")

            # makes custom directory for each file and curates a .properties file 
            os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + str(renameTexture.lower()))
            totemProperties = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + str(renameTexture.lower()) + "/totem_of_undying.properties", "x")
            totemProperties.close()

            # deduces the file name from its location
            count = textureList[counter].count("/")
            split_string = textureList[counter].split("/", count)
            substring = split_string[count]
            
            # adds the needed meta to the totem_of_undying.properties file
            totemProperties = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + str(renameTexture.lower()) + "/totem_of_undying.properties", "a")
            totemProperties.writelines(["type=item\n",
            "matchItems=totem_of_undying\n",
            "texture="])
            totemProperties.write(substring + "\n")
            totemProperties.write("nbt.display.Name=ipattern:")
            totemProperties.write(rename)
            totemProperties.close()

            # copys the image into the resource pack
            original = textureList[counter]
            target = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + str(renameTexture.lower())
            shutil.copy(original, target)

            window.Element('-IMAGE-').update(filename=textureList[counter + 1])
            window.Element('itemName').update('')

            counter = counter + 1

        elif event == 'next' and len(textureList) == int(counter + 1):

            os.remove("AppData/Roaming/Totems +/citconfig.txt")
            # prints completion message to user

            sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="AppData/Roaming/Totems +/totems.ico")

            # breaks the loop (hence closing all windows)
            break
        
    # closes window if called
    window.close()

# declares the accepted texture file types
textureFileTypes = [("JPEG, PNG, TGA (.jpg , .png , .tga)", ".jpg , .png , .tga")]

# defines the main window
def main():

    # defines how the main window will be displayed/layed-out
    layout = [
        [
            sg.Image(filename='AppData/Roaming/Totems +/windowlogo.png', key='-LOGO-'),
            sg.Text('Totems + is a new and unique way to intergrate custom totems into Minecraft!\n' + 
            'This program currently provides support for:\n' + 
            'Minecraft CMD\n' + 
            'Optifine CIT\n' + 
            'To get started follow the instructions below \/\n' + 
            ' '),
        ],
        [
            sg.Text('⚫ You will want to start by choosing your integration type here:\n' + 
            ' \n' + 
            'Optifine CIT - Allows for existing Totems to be renamed to a given string\n' + 
            '                    e.g "Totem of Axolotl" and have its texture change.\n' + 
            ' \n' +
            'Minecraft CMD - Allows for custom totems using custom model data and adds\n' + 
            '                    these with a given weight to the evoker loot_tabel.'),
            sg.Button('Optifine CIT', size=(20,1), button_color=('white','orange'), key='-TOGGLE-')
        ],
        [
            sg.Text("⚫ Select your totem image files here:")
        ],
        [
            sg.Text("Image File"),
            sg.Input(size=(58, 1), key="-TEXTURES-"),
            sg.FilesBrowse(file_types=textureFileTypes),
        ],
        [
            sg.Text("(Remember they will need to be in the following formats: .jpg , .png , .tga)")
        ],
        [
            sg.Text("⚫ Finally hit Compile and follow any further instructions to generate your pack(s):"),sg.Button("Compile")
        ],
    ]

    # creates the window
    window = sg.Window("Totems+", layout, icon="AppData/Roaming/Totems +/totems.ico")

    down = True

    # while window (GUI) is open
    while True:

        # read all events/actions
        event, values = window.read()

        # if window closed break while loop and end code
        if event == sg.WIN_CLOSED:
            break

        elif event == '-TOGGLE-':
            down = not down
            window.Element('-TOGGLE-').Update(('Minecraft CMD','Optifine CIT')[down], button_color=(('white', ('teal','orange')[down])))

        elif event == 'Compile' and down == False:

            config = open('AppData/Roaming/Totems +/cmdconfig.txt', 'x')
            config.close()

            config = open("AppData/Roaming/Totems +/cmdconfig.txt", "a")
            config.write(values["-TEXTURES-"])
            config.close()

            CMD()

            break

        elif event == 'Compile' and down == True:

            config = open('AppData/Roaming/Totems +/citconfig.txt', 'x')
            config.close()

            config = open("AppData/Roaming/Totems +/citconfig.txt", "a")
            config.write(values["-TEXTURES-"])
            config.close()

            CIT()

    # closes window if called
    window.close()

if __name__ == "__main__":
    main()
