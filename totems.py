# imports the libaries used within Totems+
import io
import os
import shutil
from tkinter.constants import S
import PySimpleGUI as sg
from PIL import Image

file_types = [("JPEG, PNG, TGA (.jpg , .png , .tga)", ".jpg , .png , .tga")]

sg.theme('DarkTeal10')

def main():
    layout = [
        [
            sg.Text("Select your texture files here!")
        ],
        [
            sg.Text("Once selected hit 'Compile'")
        ],
        [
            sg.Text("Image File"),
            sg.Input(size=(10, 1), key="-FILE-"),
            sg.FilesBrowse(file_types=file_types),
            sg.Button("Compile"),
        ],
    ]
    window = sg.Window("Totems+", layout, icon="C:/Users/Joshu/Desktop/Python/TOTEMS +/totems.ico")
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Compile":
            
            # sets the textureList to the values selected by the user
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
            originalPng = "C:/Users/Joshu/Desktop/Python/TOTEMS +/pack.png" # NEEDS UPDATING
            targetPng = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT"

            # copys the pack.png file into place
            shutil.copy(originalPng, targetPng)

            # creates the pack.mcmeta file
            packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/pack.mcmeta", "x")
            packMeta.close()

            # adds the needed meta data to the pack.mcmeta file
            packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/pack.mcmeta", "a")
            packMeta.write("{")
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

            # starts a counter at 0 (variable is used)
            counter = 0

            # while the length of list (Number of uploaded files) != the counter (which increases after every loop) runs the indent
            while len(textureList) != counter:
                
                image = Image.open(textureList[counter])
                new_image = image.resize((512, 512))
                new_image.close()

                # asks for the rename value for each file and replaceing any " " with "_"
                rename = sg.popup_get_text("Enter your Totem name here:", title = "Item Renaming", image=textureList[counter], icon="C:/Users/Joshu/Desktop/Python/TOTEMS +/totems.ico")
                renameTexture = rename.replace(" ", "_")

                # makes custom directory for each file and curates a .properties file 
                os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + renameTexture.lower())
                totemProperties = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + renameTexture.lower() + "/totem_of_undying.properties", "x")
                totemProperties.close()

                # deduces the file name from its location
                count = textureList[counter].count("/")
                split_string = textureList[counter].split("/", count)
                substring = split_string[count]

                # adds the needed meta to the totem_of_undying.properties file
                totemProperties = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + renameTexture.lower() + "/totem_of_undying.properties", "a")
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
                target = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + renameTexture.lower()
                shutil.copy(original, target)

                # increases counter by 1
                counter = counter + 1

            # prints completion message to user
            sg.popup_ok("Pack creation complete! Load up Minecraft and you Totems+ pack will appear in your resourcepack folder!", title = "Pack Completion", icon="C:/Users/Joshu/Desktop/Python/TOTEMS +/totems.ico")
    window.close()

if __name__ == "__main__":
    main()
