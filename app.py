from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import sign

w,h= 500,500

def dda(x1,y1,x2,y2):
    if x1 == x2 and y1 == y2:
        return False
    del_x, del_y = abs(x2-x1), abs(y2-y1)
    length = del_x if del_x > del_y else del_y
    del_x, del_y = (x2-x1)/length, (y2-y1)/length
    x, y = x1+.5*sign(del_x), y1+.5*sign(del_y)
    for i in range(length):
        glColor3f(1.0, 0, 0)
        glPointSize(10.0)
        glBegin(GL_POINTS)
        glVertex2d(int(x),int(y))
        glEnd()
        x, y = x+del_x, y+del_y 

def iterate():
    glClearColor(1,1,1,0)
    glViewport(0, 0, 1000,1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    gluOrtho2D(-250, 250, -150, 150)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    # AXIS STARTS
    glBegin(GL_LINES)
    glVertex2f(-1000,0)
    glVertex2f(1000,0)
    glVertex2f(0,-1000)
    glVertex2f(0,1000)
    glEnd()
    # AXIS ENDS
    #5 starts
    dda(-115,-50,-15,-50)
    dda(-15,0,-15,-50)
    dda(-115,0,-15,0)
    dda(-115,0,-115,50)
    dda(-115,50,-15,50)
    # 5 ends
    # 6 starts
    dda(115,-50,15,-50)
    dda(15,0,15,-50)
    dda(115,0,15,0)
    dda(15,0,15,50)
    dda(115,50,15,50)
    dda(115,0,115,-50)
    #6 ends
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("423 Lab 2")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()