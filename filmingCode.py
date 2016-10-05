# Neil Barooah
# neilbarooah@gatech.edu
# I have worked on this assignment with my partners, Anjani Agrawal, Raghav Meheshwari, and Wai Lam, using only the resources of this class.


from Myro import *

picList = []
def takeMovie():
    init()
    for x in timer (90):
        p = takePicture()
        picList.append(p)
        show(p)
        if 10<x<30:
            rotate(0.015,0.1)
    print(len(picList))
    savePicture(picList, "picList.gif")

p = takePicture
savePicture(p,'crash.jpg')