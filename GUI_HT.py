#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python
from tkinter import*
from PIL import ImageTk, Image
import sys
import os


def mc_HT():
    import cv2,numpy,math
    import matplotlib.pyplot as plt

    input_image = input()
    image = cv2.imread(input_image)
    greying = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(greying, (3,3), 0)

    img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
    img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
    edgeing = img_sobelx + img_sobely

    cv2.imshow('image', edgeing)
    cv2.waitKey(1000)
    cv2.destroyAllWindows() 
    width, height = edgeing.shape
    print(width, height)


    m = numpy.arange(-20, 20, 0.1)


    cs = [i for i in range(0,50)]


    accumulator = numpy.zeros((1000, len(m)), dtype = numpy.uint8)
    edges = edgeing>0


    y_index, x_index = numpy.nonzero(edges)

    for i in range(0, len(x_index)):
        x = x_index[i]
        y = y_index[i]

        for j in range(0, len(m)):
            c = int(round(y - m[j]*x))
            if c<500 and c>-500:
                accumulator[c, j] = accumulator[c, j] + 3

            else:
                pass
    plt.imshow(accumulator,cmap = 'Reds', extent = [(m[0]), (m[-1]), cs[0], cs[-1]])
    plt.title('HoughTransform')
    plt.xlabel('m(slope)')
    plt.ylabel('c(intercept)')
    plt.axis('image')
    plt.show()
    
    
def Rhotheta_HT():
    import cv2,numpy,math
    import matplotlib.pyplot as plt

    input_image = input()
    image = cv2.imread(input_image)
    greying = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(greying, (3,3), 0)

    img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
    img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
    edgeing = img_sobelx + img_sobely

    cv2.imshow('image', edgeing)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

    width, height = edgeing.shape
    theta = numpy.deg2rad(numpy.arange(-90, 90, 1))
    diag_len = int(round(math.sqrt(width*width + height*height)))
    rhos = [i for i in range(-diag_len,diag_len)]
    cos_t = numpy.cos(theta)
    sin_t = numpy.sin(theta)
    num_thetas = len(theta)

    accumulator = numpy.zeros((2*diag_len, num_thetas), dtype = numpy.uint8)
    edges = edgeing>0

    y_index, x_index = numpy.nonzero(edges)
    for i in range(0, len(x_index)):
        x = x_index[i]
        y = y_index[i]
        for j in range(0, num_thetas):
            rho =  int(round(x*cos_t[j] + y*sin_t[j]))
            accumulator[rho, j] = accumulator[rho, j] + 2

    plt.imshow(accumulator, cmap = 'Reds', extent = [numpy.rad2deg(theta[-1]), numpy.rad2deg(theta[0]), rhos[-1], rhos[0]])
    plt.title('HoughTransform')
    plt.xlabel('Angles(degrees)')
    plt.ylabel('Rho(pixels)')
    plt.axis('image')
    plt.show()

#Code for GUI
root = Tk()
root.title('GUI for Hough Transform')
root.iconbitmap('GUI_image.png')

my_img = ImageTk.PhotoImage(Image.open('GUI_image.png'))
my_label = Label(image = my_img)
my_label.pack()

def mc_HTCallBack():
    mc_HT()
def Rhotheta_HTCallBack():
    Rhotheta_HT()


frame1 = LabelFrame(root, text = 'Rho Theta space Hough Transform', padx =50, pady = 50)
frame1.pack(padx=10, pady=10)
b12 = Button(frame1, text = 'Run code', command = Rhotheta_HTCallBack)
b12.pack()


frame2 = LabelFrame(root, text = 'mc space Hough Transform', padx =60, pady = 60)
frame2.pack(padx=10, pady=10)
b22 = Button(frame2, text = 'Run code', command = mc_HTCallBack)
b22.pack()






button_quit = Button(root, text = 'Exit Program', command = root.destroy)
button_quit.pack()

root.mainloop()


# In[ ]:




