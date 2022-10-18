###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within Totems+ 
import os, shutil, getpass, PySimpleGUI as sg, json
from addons.ANIM import ANI
from addons.RESZ import RES

# outlines the versions and there pack formats
packFormatCodes = {"1.14": 4, "1.14.1": 4, "1.14.2": 4,"1.14.3": 4,"1.14.4": 4,
                   "1.15": 5, "1.15.1": 5,"1.15.2": 5, "1.16": 5,"1.16.1": 5,
                   "1.16.2": 6, "1.16.3": 6, "1.16.4": 6, "1.16.5": 6,
                   "1.17": 7, "1.17.1": 7,
                   "1.18": 8, "1.18.1": 8, "1.18.2": 8,
                   "1.19": 9, "1.19.1": 9, "1.19.2": 9}

packMeta = {"pack" : {"pack_format": 0, "description": ""}}

# defines the CIT function
def CIT(textureList, version):

    # sets the counter to 0
    counter = 0

    # transforms texture list into a list
    textureList = textureList.split(";")

    pathList = RES(textureList)

    # defines how the main window will be displayed/layed-out
    layout = [ 
        [
            sg.Image(filename=pathList[0], key='-IMAGE-'),
            sg.Text("You've selected Totems+ CIT Integration!\n" + 
            'This integration will generate:\n' + 
            'A Custom Resource Pack\n' + 
            'Follow the tooltip below to customize your packs!\n' + 
            ' ', font=('Helvetica', 10), justification='left'),
        ],
        [
            sg.Text('Rename your different textures to what you wish to rename them in-game\nIt should be noted totems may appear blurred/streched here but\n wont in Minecraft. .GIF files also wont play in this release', key='tooltip')
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
    window = sg.Window("CIT", layout, icon="img/totems.ico")

    # sets the base name (for if it isn't changed)
    name = "Totems+ OFCIT"

    # finds all the resourcepacks you already have
    dirList = os.listdir('C:/Users/' + getpass.getuser() + '/AppData/Roaming/.minecraft/resourcepacks')
    
    # starts a constant repeating loop
    repeatLoop = True
    while repeatLoop:

        # takes the range of values
        for i in range(len(dirList)):

            # checks if the name is already in use and popup for rename
            if name == dirList[i]:
                name = sg.popup_get_text("An OFCIT Integration resource pack already exists\nPlease choose a different name for this one:", title = "Duplicate Pack")
                break

        # else if the name is unique, end the loop
        else:
            repeatLoop = False

    # pre-makes the resource pack directory in the minecraft resource pack folder
    os.makedirs("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/optifine/cit/totems")

    # copys the pack.png file into place
    shutil.copy("img/pack.png", "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)

    # creates & opens the pack.mcmeta file
    with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/pack.mcmeta", "w+") as packMetaFile:

        # adds the needed meta data to the pack.mcmeta file
        packMeta["pack"]["pack_format"] = packFormatCodes[version]
        packMeta["pack"]["description"] = (f"Version: {version}\nMade By: The Totems+ Team")
        packMetaFile.write(json.dumps(packMeta))

    # while window (GUI) is open
    while True:

        # read all events/actions
        event, values = window.read()

        # if window closed break while loop and end code
        if event == sg.WIN_CLOSED:
            break
        
        # if the cancel button is pressed
        if event == 'cancel':
            
            # a confirmation window is displayed and if the user agrees all files are removed
            result = sg.popup_ok_cancel("Are you sure? Cancelling now will remove any current progress/packs")

            if result == "OK":
                shutil.rmtree("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)
        
        # else if the next button and the length of the texture list isn't equal to the counter + 1
        elif event == 'next' and len(textureList) != int(counter + 1):

            # sets the rename value to the user input ensuring no spaces are included
            rename = values["itemName"].replace(" ", "_")

            # makes custom directory for each file and curates a .properties file 
            os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/optifine/cit/totems/" + str(rename.lower()))
            totemProperties = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/optifine/cit/totems/" + str(rename.lower()) + "/totem_of_undying.properties", "w+")

            # deduces the file name from its location
            textureListSplit = textureList[counter].split("/")
            
            # adds the needed meta to the totem_of_undying.properties file
            totemProperties.writelines(["type=item\n",
            "matchItems=totem_of_undying\n",
            "texture=" + textureListSplit[-1] + "\n",
            "nbt.display.Name=ipattern:" + values["itemName"]])
            totemProperties.close()

            # if the file is a .gif file
            if textureList[counter].endswith('.gif'):

                # copys the new gif texture to the pack
                shutil.copy(ANI(textureList[counter], name, "MCCMD", rename), "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/optifine/cit/totems/" + str(rename.lower()))

            # else
            else:

                # copys the image into the resource pack
                shutil.copy(textureList[counter], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/optifine/cit/totems/" + str(rename.lower()))

            # cycles the image and clears the text box
            window.Element('-IMAGE-').update(filename=pathList[counter + 1])
            window.Element('itemName').update('')

            # increases the counter by 1
            counter += 1

        # else if the next button and the length of the texture list is equal to the counter + 1
        elif event == 'next' and len(textureList) == int(counter + 1):

            # prints completion message to user
            sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="img/totems.ico")

            # breaks the loop (hence closing all windows)
            break
        
    # closes window if called
    window.close()