# Neil Barooah
# neilbarooah@gatech.edu
# I have worked on this assignment with my partners, Anjani Agrawal, Raghav Meheshwari, and Wai Lam, using only the resources of this class.

from Myro import*

def race():
    rc=makeRobot("Scribbler","COM14")
    rp=makeRobot("Scribbler","COM20")
    rc.getBattery()
    try:
        for x in timer(25):
            rc.forward(0.1)
            rp.forward(0.1)
            wait(0.5)
            rc.forward(0.2)
            rp.forward(0.15)
            rc.forward(0.1)
        rc.rotate(0.4)
        rc.forward(0.2)
        rp.rotate(-0.1,4)
        rp.forward(1,1)
        rc.forward(0.1,4)
        rc.forward(0.3,4)
        rc.beep(2,650)
        rc.rotate(1,4)
        rc.beep(2,650)
        rp.backward(1,2)
        rp.rotate(0.1,2.5)
        rp.forward(1, 4)
    except:
        stop()
race()