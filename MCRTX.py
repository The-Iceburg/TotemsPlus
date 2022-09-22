###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

import os.path, getpass, shutil, PySimpleGUI as sg
from ANIM import ANI

# outlines the versions and there pack formats
packFormat4 = ["1.14","1.14.1","1.14.2","1.14.3","1.14.4"]
packFormat5 = ["1.15","1.15.1","1.15.2","1.16","1.16.1"]
packFormat6 = ["1.16.2","1.16.3","1.16.4","1.16.5"]

def RTX(textureList, version):

    textureList = textureList.split(";")

    if len(textureList) > 1:
        print("Uh oh now something more complicated gotta happen")

    else:
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
