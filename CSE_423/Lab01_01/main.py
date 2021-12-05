# Naimul Hasan Sabbir
# ID: 18301136
# CSE423

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import itertools

# lists for coordinates *_*
xValues = [random.randint(0,500) for _ in range(50)]
print(xValues)
yValues = [random.randint(0,500) for _ in range(50)]
print(yValues)

def pixelDrawing(x,y):
    glPointSize(5)
    glBegin(GL_POINTS)
    for (a,b) in zip(x,y):
        glVertex2f(a,b)
    glEnd()

def buildingHouse():
    glBegin(GL_LINES)

    # house main part with green color
    glVertex2f(200, 100)
    glVertex2f(200, 300)

    glVertex2f(200, 100)
    glVertex2f(400, 100)

    glVertex2f(400, 100)
    glVertex2f(400, 300)

    glVertex2f(400, 300)
    glVertex2f(200, 300)

    # house roof part with red color
    glColor4f(1.0,0.0,0.0,1.0)

    glVertex2f(200, 300)
    glVertex2f(300, 350)

    glVertex2f(400, 300)
    glVertex2f(300, 350)

    # house door part with red color
    glVertex2f(280, 100)
    glVertex2f(280, 180)

    glVertex2f(320, 100)
    glVertex2f(320, 180)

    glVertex2f(280, 180)
    glVertex2f(320, 180)

    # house window part
    glVertex2f(220, 220)
    glVertex2f(220, 250)

    glVertex2f(220, 220)
    glVertex2f(250, 220)

    glVertex2f(250, 220)
    glVertex2f(250, 250)

    glVertex2f(250, 250)
    glVertex2f(220, 250)
    glEnd()

def ddaDrawing(x1,y1,x2,y2):
    slope = (y2-y1)/(x2-x1)
    glBegin(GL_POINTS)
    for pixel in range(x2):
        x1 = x1+1
        y1 = y1+slope
        if x1 % 2 != 0 :
            glVertex2f(x1,y1)
    glEnd()

def ddaDrawing2(x1,y1,x2,y2):
    slope = (x2-x1)/(y2-y1)
    glBegin(GL_POINTS)
    for pixel in range(y2):
        y1 = y1+1
        x1 = x1+slope
        glVertex2f(x1,y1)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)
    # call the draw methods here
    # pixelDrawing(xValues,yValues)
    # buildingHouse()
    ddaDrawing(200,350,300,350)
    ddaDrawing2(350,150,350,200)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()