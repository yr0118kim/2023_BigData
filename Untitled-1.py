# %%
import cv2
import numpy as np

# %%
def line():
    img = np.zeros((512,512,3),np.uint8)
    img.fill(255)
    img = cv2.line(img,(300,0),(100,511),(0,255,0),5)
    cv2.imshow('JetsonNano_Line',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# %%
def rectangle():
    img = np.zeros((512,512,3),np.uint8)
    img.fill(255)
    img = cv2.rectangle(img,(100,150),(500,300),(255,255,0),5)
    cv2.imshow('JetsonNano_Rectangle',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# %%
def circle():
    img = np.zeros((512,512,3),np.uint8)
    img.fill(255)
    img = cv2.circle(img,(100,150),100,(255,255,0),2)
    cv2.imshow('JetsonNano_Circle',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# %%
def ellipse():
    img = np.zeros((512,512,3),np.uint8)
    img.fill(255)
    img = cv2.ellipse(img,(256,256),(100,100),0,0,275,(255,255,255),-1)
    cv2.imshow('',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# %%
# line()
rectangle()
circle()
ellipse()

