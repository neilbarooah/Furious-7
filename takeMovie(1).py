from Myro import *

def zoom():
    aList = []
    for num in range(10):
        p = takePicture()
        show(p)
        aList.append(p)
        forward(1,0.1)
        wait(0.1)
    savePicture(aList, "car.gif")

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

#takeMovie()

def fade():
    r = 0
    g = 0
    b = 0
    
    aList = []
    for x in range(51):
        if r < 255 and g < 255 and b < 255:
            p = makePicture("car.jpg")
            r = r-5
            g = g-5
            b = b-5
            for pix in getPixels(p):
                red = getRed(pix)
                green = getGreen(pix)
                blue = getBlue(pix)
                setRed(pix,red+r)
                setGreen(pix,green+g)
                setBlue(pix,blue+b)
            show(p)
            aList.append(p)  
    savePicture(aList,'fade.jpg')

    
def redtint():
    p = makePicture('picList-75 (dragged).tiff')
    for pix in getPixels(p):
        setRed(pix, 255)
    show(p)
    savePicture(p,'red.jpg')