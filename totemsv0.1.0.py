import os

import shutil

variable = "D:/totems/hello1.png;D:/totems/hello2.png;D:/totems/hello3.png"

variable = variable.split(";")

os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT")
os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets")

# original1 = "D:/Totems + Download/pack.png"
# target1 = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets"

# shutil.copy(original1, target1)

packMeta = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/pack.mcmeta", "x")

packMeta.close()

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

os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft")
os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine")
os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit")
os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems")

counter = 0

while len(variable) != counter:

    rename = input("What do you want to rename the texture:" + variable[counter] + " to in-game?\n")

    renameTexture = rename.replace(" ", "_")

    os.mkdir("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + renameTexture.lower())

    totemProperties = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + renameTexture.lower() + "/totem_of_undying.properties", "x")

    totemProperties.close()

    totemProperties = open("AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + renameTexture.lower() + "/totem_of_undying.properties", "a")

    totemProperties.write("type=item")
    totemProperties.write("\n")
    totemProperties.write("matchItems=totem_of_undying")

    count = variable[counter].count("/")

    split_string = variable[counter].split("/", count)

    substring = split_string[count]

    totemProperties.write("\n")
    totemProperties.write("texture=")
    totemProperties.write(substring)
    totemProperties.write("\n")
    totemProperties.write("nbt.display.Name=ipattern:")
    totemProperties.write(rename)

    totemProperties.close()

    original = variable[counter]
    target = "AppData/Roaming/.minecraft/resourcepacks/Totems+ OFCIT/assets/minecraft/optifine/cit/totems/" + renameTexture.lower()

    shutil.copy(original, target)

    counter = counter + 1


print("Pack creation complete!")
print("Load up Minecraft and the pack will be made in your resource pack folder!")