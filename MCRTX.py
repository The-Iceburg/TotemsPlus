###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

from PIL import Image, ImageSequence
import os.path, getpass, shutil, PySimpleGUI as sg
from ANIM import ANI

# outlines the versions and there pack formats
packFormat4 = ["1.14","1.14.1","1.14.2","1.14.3","1.14.4"]
packFormat5 = ["1.15","1.15.1","1.15.2","1.16","1.16.1"]
packFormat6 = ["1.16.2","1.16.3","1.16.4","1.16.5"]

def RTX(textureList, version):

    textureList = textureList.split(";")

    index = 0

    if len(textureList) > 1:

         # if the directory resized already exists, then delete it
        if os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/resized'):
            shutil.rmtree('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/resized')

        # make the resized folder
        os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/resized")

        # new list to hold the new file names
        pathList = []

        # the path for the resized folder
        targetIMG = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/resized"

        # for loop for each image
        for i in range(len(textureList)):

            # finds only the names
            splitList = textureList[i].split("/")
            # makes a new file name
            fileName1 = "resize_" + str(splitList[-1]) 

            # Run indented code if it is a GIF
            if textureList[i].endswith(".gif") == True:
                origIMG = Image.open(textureList[i])
                size = 128, 128
                frames = ImageSequence.Iterator(origIMG)
                def thumbnails(frames):
                    for frame in frames:
                        thumbnail = frame.copy()
                        thumbnail = thumbnail.resize(size)
                        thumbnail.thumbnail(size, Image.ANTIALIAS)
                        yield thumbnail
                frames = thumbnails(frames)

                resizedGIF = next(frames)
                resizedGIF.info = origIMG.info
                resizedGIF.save(fileName1, save_all=True, append_images=list(frames), loop=0)

            # Run Code if it is not a GIF
            elif textureList[i].endswith(".gif") == False:

                # copies the images to the resized folder
                shutil.copy(textureList[i], targetIMG)
                IMGpath = targetIMG + "/" + splitList[-1]

                # opens and resizes the image, saves with a new name
                openIMG = Image.open(IMGpath)
                resizedIMG = openIMG.resize((128,128))
                resizedIMG.save(fileName1)

            # moves to the resized folder and saves the path to the path list 
            shutil.move(fileName1, targetIMG)
            fileName2 = targetIMG + "/" + fileName1
            pathList.append(fileName2)

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
            event, values = window.read()

            # if window closed break while loop and end code
            if event == sg.WIN_CLOSED:
                break
            
            # if the cancel button is pressed
            if event == 'cancel':

                # a confirmation window is displayed and if the user agrees all files are removed
                result = sg.popup_ok_cancel("Are you sure?")

                if result == "OK":
                    break

            # else if the next button and the length of the texture list isn't equal to the counter + 1
            if event == 'next':

                index += 1
                if index == len(textureList):
                    index = 0

                window.Element('-IMAGE-').update(filename=pathList[index])

             # else if the next button and the length of the texture list isn't equal to the counter + 1
            if event == 'back':

                index -= 1
                if index == -1:
                    index = len(textureList) - 1

                window.Element('-IMAGE-').update(filename=pathList[index])

            if event == 'choose':
                textureList = [textureList[index]]
                break

    # sets the base name (for if it isn't changed)
    name = "Totems+ RTX"

    # checks if the resource pack exists and if it does user is prompted to suggest a new name
    if os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/.minecraft/resourcepacks/Totems+ RTX'):
        name = sg.popup_get_text("An MCRTX Integration resource pack allready exists\nPlease choose a different name for this one:", title = "Duplicate Pack")

    # pre-makes the resource pack directory in the minecraft resource pack folder
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets")
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft")
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures")
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item")

    # copys the pack.png file into place
    shutil.copy("img/pack.png", "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name)

    # creates & opens the pack.mcmeta file
    packMeta = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/pack.mcmeta", "w+")

    # derrives the resource pack format code from the version
    if version in packFormat4:
        packFormat = 4
    elif version in packFormat5:
        packFormat = 5
    elif version in packFormat6:
        packFormat = 6
    elif version.startswith("1.17"):
        packFormat = 7
    elif version.startswith("1.18"):
        packFormat = 8
    elif version.startswith("1.19"):
        packFormat = 9

    # adds the needed meta data to the pack.mcmeta file
    packMeta.writelines(['{\n',
    '  "pack": {\n',
    '    "pack_format": ' + str(packFormat) + ',\n',
    '	"description": "Version: ' + version + '\n',
    'Made By: The Totems+ Team"\n',
    '  }\n',
    '}'])
    packMeta.close()

     # if the file is a .gif file
    if textureList[0].endswith('.gif'):

        # copys the new gif texture to the pack
        shutil.copy(ANI(textureList[0], name, "MCRTX", None), "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item")

    # else
    else:
        # copys the image into the resource pack
        shutil.copy(textureList[0], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item")

    textureList[0] = textureList[0].split("/")
    old_file = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item/" + textureList[0][-1].replace(".gif", ".png")
    os.rename(old_file, "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + name + "/assets/minecraft/textures/item/totem_of_undying.png")

    # prints completion message to user
    sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="img/totems.ico")
