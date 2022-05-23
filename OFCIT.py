# imports the libaries used within Totems+ 
import os
import shutil
from tkinter.constants import S
import PySimpleGUI as sg

# defines the CIT function
def CIT():

    # sets the counter to 0
    counter = 0

    # extract the textureList from the config file
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
    window = sg.Window("CIT", layout, icon="AppData/Roaming/Totems +/totems.ico")

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
        
        # else if the next button and the length of the texture list isn't equal to the counter + 1
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

            # cycles the image and clears the text box
            window.Element('-IMAGE-').update(filename=textureList[counter + 1])
            window.Element('itemName').update('')

            # increases the counter by 1
            counter += 1

        # else if the next button and the length of the texture list is equal to the counter + 1
        elif event == 'next' and len(textureList) == int(counter + 1):

            # deletes the config file
            os.remove("AppData/Roaming/Totems +/citconfig.txt")

            # prints completion message to user
            sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="AppData/Roaming/Totems +/totems.ico")

            # breaks the loop (hence closing all windows)
            break
        
    # closes window if called
    window.close()