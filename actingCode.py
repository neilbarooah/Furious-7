# We, Wenzhong Jin, daniel-jin@gatech.edu, 903048854
# Hanxiong Wu, hwu329@gatech.edu, 903039536
# worked on this assignment together using only
# the materials from this semester.

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
##         rc.forward(1,2)
##         rc.backward(1,2)
        rp.backward(1,2)
        rp.rotate(0.1,2.5)
        rp.forward(1, 4)
    except:
        stop()
race()