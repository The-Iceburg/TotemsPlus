###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within Totems+ 
import os.path, getpass, shutil, json, PySimpleGUI as sg
from addons.ANIM import ANI
from addons.RESZ import RES

# outlines the versions corresponding pack format code
packFormatCodes = {"1.14": 4, "1.14.1": 4, "1.14.2": 4,"1.14.3": 4,"1.14.4": 4,
                   "1.15": 5, "1.15.1": 5,"1.15.2": 5, "1.16": 5,"1.16.1": 5,
                   "1.16.2": 6, "1.16.3": 6, "1.16.4": 6, "1.16.5": 6,
                   "1.17": 7, "1.17.1": 7,
                   "1.18": 8, "1.18.1": 8, "1.18.2": 8,
                   "1.19": 9, "1.19.1": 9, "1.19.2": 9}

# outlines the pack meta information
packMeta = {"pack" : {"pack_format": 0, "description": ""}}

# defines the RTX function
def RTX(textureList, version):

    # makes texttureList an actual list
    textureList = textureList.split(";")

    # sets deafult index to 0
    index = 0

    # if the length of texture list is greater than 1
    if len(textureList) > 1:

        pathList = RES(textureList)

        # defines how the main window will be displayed/layed-out
        layout = [ 
            [
                sg.Image(filename=pathList[index], key='-IMAGE-'),
                sg.Text("You've selected Totems+ RTX Integration!\n" + 
                'This integration will generate:\n' + 
                'A Custom Resource Pack\n' + 
                'Follow the tooltip below to customize your packs!\n' + 
                ' ', font=('Helvetica', 10), justification='left'),
            ],
            [
                sg.Text('Select which Totem Texture you want te replace the original\nIt should be noted totems may appear blurred/streched here but\n wont in Minecraft. .GIF files also wont play in this release', key='tooltip')
            ],
            [
                sg.Button('Select Texture', key='choose'),
                sg.Button('Previous', key='back'),
                sg.Button('Next', key='next'),
                sg.Button('Cancel', key='cancel'),
            ],
        ]

        # creates the window
        window = sg.Window("CIT", layout, icon="img/totems.ico")

        # while window (GUI) is open
        while True:

            # read all events/actions
            event = window.read()

            # if window closed break while loop and end code
            if event == sg.WIN_CLOSED:
                exit()
            
            # if the cancel button is pressed closes the window
            if event == 'cancel':
                exit()

            # if the next button
            if event == 'next':

                # increases the index
                index += 1

                # if it reaches max then resets it
                if index == len(textureList):
                    index = 0

                # updates the displayed image
                window.Element('-IMAGE-').update(filename=pathList[index])

            # if the back button
            if event == 'back':

                # decreases the index
                index -= 1

                # if index reaches min then resets it
                if index == -1:
                    index = len(textureList) - 1

                # updates the displayed image
                window.Element('-IMAGE-').update(filename=pathList[index])

            # if the choose button
            if event == 'choose':

                # resets the texturelIst to the current value
                textureList = [textureList[index]]

                # breaks the window
                break

    # sets the base name (for if it isn't changed)
    name = "Totems+ RTX"

    # finds all the resourcepacks you already have 
    dirList = os.listdir('C:/Users/' + getpass.getuser() + '/AppData/Roaming/.minecraft/resourcepacks')
    
    # starts a constant repeating loop
    repeatLoop = True
    while repeatLoop:
        
        # takes the range of values
        for i in range(len(dirList)):
            
            # checks if the name is already in use and popup for rename
            if name == dirList[i]:
                name = sg.popup_get_text("An MCRTX Integration resource pack already exists\nPlease choose a different name for this one:", title = "Duplicate Pack")
                break
        # else if the name is unique, end the loop
        else:
            repeatLoop = False

    # makes the resource pack directory in the minecraft resource pack folder
    os.makedirs("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item")

    # copys the pack.png file into place
    shutil.copy("img/pack.png", "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)

    # creates & opens the pack.mcmeta file
    with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/pack.mcmeta", "w+") as packMetaFile:

        # adds the needed meta data to the pack.mcmeta file
        packMeta["pack"]["pack_format"] = packFormatCodes[version]
        packMeta["pack"]["description"] = (f"Version: {version}\nMade By: The Totems+ Team")
        packMetaFile.write(json.dumps(packMeta))

    # if the file is a .gif file
    if textureList[0].endswith('.gif'):

        # copys the new gif texture to the pack
        shutil.copy(ANI(textureList[0], name, "MCRTX", None), "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item")

    # else
    else:

        # copys the image into the resource pack
        shutil.copy(textureList[0], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item")

    # gets the actual file name
    textureList[0] = textureList[0].split("/")

    # gets the current location of the file
    old_file = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item/" + textureList[0][-1].replace(".gif", ".png")

    # renames the file to totem_of_undying.png
    os.rename(old_file, "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item/totem_of_undying.png")

    # prints completion message to user
    sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="img/totems.ico")
