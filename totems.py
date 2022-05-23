# imports the libaries used within Totems+
import os
import shutil

# TEMPORARY sets the textureList to a tempoary "Dummy" value but in the same format of future inputs
textureList = "D:/Downloads 2.0/totems/bachi_totem.png;D:/Downloads 2.0/totems/rickroll_totem.png;D:/Downloads 2.0/totems/shrek_totem.png;D:/Downloads 2.0/totems/totem (1).png;D:/Downloads 2.0/totems/totem.png;D:/Downloads 2.0/totems/totem_png.png" # NEEDS UPDATING

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
# originalPng = "D:/Totems + Download/pack.png" # NEEDS UPDATING
# targetPng = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT"

# copys the pack.png file into place
# shutil.copy(originalPng, targetPng)

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

    # asks for the rename value for each file and replaceing any " " with "_"
    rename = input("What do you want to rename the texture:" + textureList[counter] + " to in-game?\n")
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
print("Pack creation complete!")
print("Load up Minecraft and the pack will be made in your resource pack folder!")
#   CODE END    #   