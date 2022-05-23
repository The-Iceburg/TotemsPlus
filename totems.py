# imports the libaries used within Totems+ 
import os
import shutil
from tkinter.constants import S

import PySimpleGUI as sg

# declares the accepted file types
file_types = [("JPEG, PNG, TGA (.jpg , .png , .tga)", ".jpg , .png , .tga")]

# sets window theme
sg.theme('DarkTeal10')

def main():

    # defines how the main window will be displayed/layed-out
    layout = [
        [
            sg.Text("Toggle your intergration type here:")
        ],
        [
            sg.Button('Optifine CIT', size=(20,1), button_color=('white','orange'), key='B')
        ],
        [
            sg.Text("Select your totem images here:")
        ],
        [
            sg.Text("Image File"),
            sg.Input(size=(10, 1), key="-FILE-"),
            sg.FilesBrowse(file_types=file_types),
            sg.Button("Compile"),
        ],
        [
            sg.Text("Then hit Compile to generate your pack(s)!")
        ]
    ]

    # creates the window
    window = sg.Window("Totems+", layout, icon="D:/Totems + Download/totems.ico")

    down = True

    # while window (GUI) is open
    while True:

        # read all events/actions
        event, values = window.read()

        # if window closed break while loop and end code
        if event == sg.WIN_CLOSED:
            break

        elif event == 'B':
            down = not down
            window.Element('B').Update(('Minecraft CMD','Optifine CIT')[down], button_color=(('white', ('teal','orange')[down])))

        # if compile button pressed and down = true (Optifine CIT selected)
        if event == "Compile" and down == True:
            
            # sets the textureList to the values uploaded by the user
            textureList = values["-FILE-"]

            # splits the textureList into a list at each ";"
            textureList = textureList.split(";")

            # pre-makes the resource pack directory in the minecraft resource pack folder
            os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT")
            os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets")
            os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft")
            os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine")
            os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit")
            os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems")

            # TEMPORARY sets the pack.png original location & destination as variables
            originalPng = "D:/Totems + Download/pack.png" # NEEDS UPDATING
            targetPng = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT"

            # copys the pack.png file into place
            shutil.copy(originalPng, targetPng)

            # creates the pack.mcmeta file
            packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/pack.mcmeta", "x")
            packMeta.close()

            # adds the needed meta data to the pack.mcmeta file
            packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/pack.mcmeta", "a")
            packMeta.write('{')
            packMeta.write("\n")
            packMeta.write('  "pack": {')
            packMeta.write("\n")
            packMeta.write('    "pack_format": 7,')
            packMeta.write("\n")
            packMeta.write('	"description": "Optifine CIT Integration')
            packMeta.write("\n")
            packMeta.write('Made By: The Totems+ Team"')
            packMeta.write("\n")
            packMeta.write('  }')
            packMeta.write("\n")
            packMeta.write('}')
            packMeta.close()

            # starts a counter at 0 (variable is used)
            counter = 0

            # while the length of list (Number of uploaded files) != the counter (which increases after every loop) runs the indent
            while len(textureList) != counter:

                # asks for the rename value for each file and replaceing any " " with "_"
                rename = sg.popup_get_text("Enter your Totem name here:", title = "Item Renaming", image=textureList[counter], icon="D:/Totems + Download/totems.ico")
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
                totemProperties.write("type=item")
                totemProperties.write("\n")
                totemProperties.write("matchItems=totem_of_undying")
                totemProperties.write("\n")
                totemProperties.write("texture=")
                totemProperties.write(substring)
                totemProperties.write("\n")
                totemProperties.write("nbt.display.Name=ipattern:")
                totemProperties.write(rename)
                totemProperties.close()

                # copys the image into the resource pack
                original = textureList[counter]
                target = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + str(renameTexture.lower())
                shutil.copy(original, target)

                # increases counter by 1
                counter = counter + 1

            # prints completion message to user
            sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="D:/Totems + Download/totems.ico")

            break

        # else if compile button pressed and down = false (Minecraft CMD selected)
        elif event == "Compile" and down == False:
            
            # sets the textureList to the values uploaded by the user
            textureList = values["-FILE-"]

            # splits the textureList into a list at each ";"
            textureList = textureList.split(";")

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
            originalPng = "D:/Totems + Download/pack.png" # NEEDS UPDATING
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

            # starts a counter at 0 (variable is used)
            counter = 0

            # while the length of list (Number of uploaded files) != the counter (which increases after every loop) runs the indent
            while len(textureList) != counter:
                
                 # asks for the rename value for each file and replaceing any " " with "_"
                rename = sg.popup_get_text("Enter your Totem name here:", title = "Item Renaming", image=textureList[counter], icon="D:/Totems + Download/totems.ico")
                renameTexture = rename.replace(" ", "_")

                if counter != len(textureList) - 1:

                    totemJSON = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
                    totemJSON.write("\n")
                    totemJSON.write('	  {"predicate": {"custom_model_data":91034'+ str(counter) +'}, "model": "totems/'+ str(renameTexture.lower()) +'"},')
                    totemJSON.close

                else:

                    totemJSON = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
                    totemJSON.write("\n")
                    totemJSON.write('	  {"predicate": {"custom_model_data":91034'+ str(counter) +'}, "model": "totems/'+ str(renameTexture.lower()) +'"}')
                    totemJSON.close

                individualTotem = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/totems/" + str(renameTexture.lower()) + ".json", "x")
                individualTotem.close()

                # deduces the file name from its location
                count = textureList[counter].count("/")
                split_string = textureList[counter].split("/", count)
                substring = split_string[count]
                
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

                # increases counter by 1
                counter = counter + 1

            totemJSON = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ CMD/assets/minecraft/models/item/totem_of_undying.json", "a")
            totemJSON.writelines([']\n',
            '}'])
            totemJSON.close()

            folderLocation = sg.popup_get_folder("Select your world:", title = "World Selection", icon="D:/Totems + Download/totems.ico", initial_folder="AppData/Roaming/.minecraft/saves")

            os.mkdir(folderLocation + "/datapacks/Totems+ CMD")
            os.mkdir(folderLocation + "/datapacks/Totems+ CMD/data")
            os.mkdir(folderLocation + "/datapacks/Totems+ CMD/data/minecraft")
            os.mkdir(folderLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables")
            os.mkdir(folderLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities")

            # TEMPORARY sets the pack.png original location & destination as variables
            originalPng = "D:/Totems + Download/pack.png" # NEEDS UPDATING
            targetPng = folderLocation + "/datapacks/Totems+ CMD"

            # copys the pack.png file into place
            shutil.copy(originalPng, targetPng)

            # creates the pack.mcmeta file
            packMeta = open(folderLocation + "/datapacks/Totems+ CMD/pack.mcmeta", "x")
            packMeta.close()

            # adds the needed meta data to the pack.mcmeta file
            packMeta = open(folderLocation + "/datapacks/Totems+ CMD/pack.mcmeta", "a")
            packMeta.writelines(['{\n',
            '  "pack": {\n',
            '    "pack_format": 7,\n',
            '	"description": "Minecraft CMD Integration\n',
            'Made By: The Totems+ Team"\n',
            '  }\n',
            '}'])
            packMeta.close()

            evokerJSON = open(folderLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "x")
            evokerJSON.close()

            evokerJSON = open(folderLocation + "/datapacks/Totems+ CMD/data/minecraft/loot_tables/entities/evoker.json", "a")
            evokerJSON.writelines(['{\n',
            '  "type": "minecraft:entity",\n',
            '  "pools": [\n',
            '    {\n',
            '      "rolls": 1.0,\n',
            '      "bonus_rolls": 0.0,\n',
            '      "entries": [\n'])

            counter = 0
            
            # while the length of list (Number of uploaded files) != the counter (which increases after every loop) runs the indent
            while len(textureList) != counter:
                
                if counter != len(textureList) - 1:
                    
                    weight = sg.popup_get_text("Enter the weight of your Totem here:", title = "Item Weighting", image=textureList[counter], icon="D:/Totems + Download/totems.ico")

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

                else:

                    weight = sg.popup_get_text("Enter the weight of your Totem here:", title = "Item Weighting", image=textureList[counter], icon="D:/Totems + Download/totems.ico")
                    
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

                counter = counter + 1
                
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
            
            # prints completion message to user
            sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="D:/Totems + Download/totems.ico")

            break

    # closes window if while loop broken
    window.close()

if __name__ == "__main__":
    main()
