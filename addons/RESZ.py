###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

import os, shutil, getpass
from PIL import Image, ImageSequence

# defines the resize function
def RES(textureList):

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

            # opens the original image
            origIMG = Image.open(textureList[i])

            # Converts the gif into its separate frames
            frames = ImageSequence.Iterator(origIMG)

            # defines the thumbnails function taking an argument of frames
            def thumbnails(frames):

                # for each frame in frames
                for frame in frames:

                    # sets the thumbnail to the frame
                    thumbnail = frame.copy()

                    # resizes the thumbnail to the predefined size
                    thumbnail = thumbnail.resize((128,128))

                    # sets the physical image thumbnail
                    thumbnail.thumbnail((128,128), Image.ANTIALIAS)

                    # returns object
                    yield thumbnail

            # sets frames to the product of itself in the thumbnails subroutine
            frames = thumbnails(frames)

            # gets the next frame of the gif
            resizedGIF = next(frames)

            # copies meta data
            resizedGIF.info = origIMG.info

            # saves the image appropriately
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
    
    # returns new list of images
    return pathList