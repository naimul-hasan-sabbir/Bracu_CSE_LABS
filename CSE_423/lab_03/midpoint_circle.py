from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def midPointCircleDraw(x_centre_point, y_centre_point, radius):

    glPointSize(3)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)

    x_coordinate = radius
    y_coordinate = 0

    # Printing the initial point the
    # axes after translation
    glVertex2f(x_coordinate + x_centre_point, y_coordinate + y_centre_point)

    # Initialising the value of P
    P = 1 - radius

    while x_coordinate > y_coordinate:

        y_coordinate += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y_coordinate + 1

        # Mid-point outside the perimeter
        else:
            x_coordinate -= 1
            P = P + 2 * y_coordinate - 2 * x_coordinate + 1

        # All the perimeter points have
        # already been printed
        if x_coordinate < y_coordinate:
            break

        # Printing the generated point its reflection
        # in the other octants after translation
        glVertex2f(x_coordinate + x_centre_point, y_coordinate + y_centre_point)
        glVertex2f(-x_coordinate + x_centre_point, y_coordinate + y_centre_point)
        glVertex2f(x_coordinate + x_centre_point, -y_coordinate + y_centre_point)
        glVertex2f(-x_coordinate + x_centre_point, -y_coordinate + y_centre_point)

        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x_coordinate != y_coordinate:
            glVertex2f(y_coordinate + x_centre_point, x_coordinate + y_centre_point)
            glVertex2f(-y_coordinate + x_centre_point, x_coordinate + y_centre_point)
            glVertex2f(y_coordinate + x_centre_point, -x_coordinate + y_centre_point)
            glVertex2f(-y_coordinate + x_centre_point, -x_coordinate + y_centre_point)
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
    glColor3f(0.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    midPointCircleDraw(275, 300, 120)
    midPointCircleDraw(275, 350, 38)
    midPointCircleDraw(175, 185, 47)
    midPointCircleDraw(377, 185, 47)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()