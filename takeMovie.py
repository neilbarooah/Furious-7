from Myro import *
picList = []
def takeMovie():
    init("com40")
    for x in timer (90):
        p = takePicture()
        picList.append(p)
        show(p)
        if 10<x<30:
            rotate(0.015,0.1)
    print(len(picList))
    savePicture(picList, "picList.gif")

takeMovie()

def greenScreen():
    background = makePicture("race.jpg")
    p = makePicture("car.jpg")
    for x in range(0,getWidth(p)//2):
        for y in range( 0, getHeight(p)//2):
            for pix in getPixels(p):
                r = getRed(pix)
                b = getBlue(pix)
                g = getGreen(pix)
