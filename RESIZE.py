from importlib.resources import path
import os, shutil, getpass
from PIL import Image, ImageSequence


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
    
    return pathList