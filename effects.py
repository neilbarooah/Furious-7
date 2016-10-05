from Myro import * 

picList = makePicture("picList.gif")
finalList = []

def seeingRed():
    for x in range(getWidth(p)):
        for y in range(getHeight(p)):
            pix = getPixel(p,x,y)
            setRed(pix, 255)

def fade():
    for i in range(15) :
        p1 = copyPicture(p)
        for pix in getPixels(p1):
            r = getRed(pix)
            g = getGreen(pix)
            b = getBlue(pix)
            setRed(pix, r - (i*(r/15)))
            setGreen(pix, g - (i*(g/15)))
            setBlue(pix, b - (i*(b)/15))
        finalList.append(p1)

def crossfade(p1,p2):
    x = getWidth(p1)
    y = getHeight(p1)
    for num1 in range(x):
        for num2 in range(y):
            pix1 = getPixel(p1, num1, num2)
            pix2 = getPixel(p2, num1, num2)
            red1 = getRed(pix1)
            blue1 = getBlue(pix1)
            green1 = getGreen(pix1)
            red2 = getRed(pix2)
            blue2 = getBlue(pix2)
            green2 = getGreen(pix2)
            while red1 > red2:
                red1 = red1 - 2
                setRed(pix1, red1)
            while red1 < red2:
                red1 = red1 + 2
                setRed(pix1, red1)
            while blue1 > blue2:
                blue1 = blue1 - 2
                setBlue(pix1, blue1)
            while blue1 < blue2:
                blue1 = blue1 + 2
                setBlue(pix1, blue1)
            while green1 > green2:
                green1 = green1 - 2
                setGreen(pix1, green1)
            while green1 < green2:
                green1 = green1 + 2
                setGreen(pix1, green1)
        finalList.append(p1)


for p in picList:
	if 1 < p < 3:
		#GREENSCREEN!
	if 3 < p < 12:
		seeingRed()
		finalList.append(p)
	if p == 13:
		fade()
	if 14 < p < 50:
		finalList.append(p)
	if p == 51:
		p1 = picList[51]
		p2 = picList[52]
		crossfade(p1,p2)


#insertion
#merge
#bubble