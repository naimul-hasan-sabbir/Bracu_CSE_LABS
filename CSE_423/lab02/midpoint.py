from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def midpoint_digit(X1, Y1, X2, Y2):

    if (X2 - X1) == 0:
        M = Y2 -Y1
    else:
        M = (Y2 - Y1) / (X2 - X1)

    if abs(M) < 1:
        if X1 > X2:
            t = X1
            X1 = X2
            X2 = t

            t = Y1
            Y1 = Y2
            Y2 = t

    dx = abs(X2 - X1)
    dy = abs(Y2 - Y1)

    # initial value of decision parameter d
    d = 2 * dy - dx
    x = X1
    y = Y1

    glPointSize(1)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    while x <= X2:
        glVertex2f(x, y)  # jekhane show korbe pixel
        x = x + 1

        if d >= 1:
            if M < 1:
                y = y + 1
            else:
                y = y - 1
            d = d + 2 * dy - 2 * dx

        else:
            y = y
            d = d + 2 * dy


    glEnd()

    if abs(M) >= 1:
        if Y1 > Y2:
            t = X1
            X1 = X2
            X2 = t

            t = Y1
            Y1 = Y2
            Y2 = t

    dx = abs(X2 - X1)
    dy = abs(Y2 - Y1)

    # initial value of decision parameter d
    d = 2 * dx - dy
    x = X1
    y = Y1

    glPointSize(1)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    while y <= Y2:
        glVertex2f(x, y)  # jekhane show korbe pixel
        y = y + 1

        if d >= 1:
            if M >= 1:
                x = x + 1
            else:
                x = x - 1
            d = d + 2 * dx - 2 * dy


        else:
            x = x
            d = d + 2 * dx


    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here

    # for digit [3]
    midpoint_digit(250, 100, 350, 100)
    midpoint_digit(250, 200, 350, 200)
    midpoint_digit(250, 300, 350, 300)
    midpoint_digit(355, 100, 355, 200)
    midpoint_digit(355, 205, 355, 300)
    # for digit [6]
    midpoint_digit(400, 100, 500, 100)
    midpoint_digit(400, 200, 500, 200)
    midpoint_digit(400, 300, 500, 300)
    midpoint_digit(395, 100, 395, 200)
    midpoint_digit(395, 205, 395, 295)
    midpoint_digit(499, 105, 499, 195)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()