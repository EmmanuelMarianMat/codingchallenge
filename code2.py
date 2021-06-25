
from cv2 import *

img = imread('1.png')
grey = cvtColor(img,COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(grey,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)

rect_kernel = getStructuringElement(MORPH_RECT,(13,3))
dilation = dilate(thresh,rect_kernel, iterations=1)

contours, hierarchy = findContours(dilation, RETR_LIST, CHAIN_APPROX_NONE)

lines = []
img2 = img.copy()

for contour in contours:
    x,y,w,h = boundingRect(contour)
    if h<20 and w>17:
        lines.append((x,y,w,h))
        rectangle(img2, (x,y), (x+w,y+h), (0,255,0),2)

imshow('',img2)
waitKey(0)

lines = lines[::-1]
rect_kernel = getStructuringElement(MORPH_RECT,(3,3))

image_count = 1

for l in lines:
    (x,y,w,h) = l
    crop = thresh[y:y+h,x:x+w]
    dilation = dilate(crop,rect_kernel, iterations=1)
    contours, hierarchy = findContours(dilation, RETR_LIST, CHAIN_APPROX_NONE)

    for contour in contours:
        x1,y1,w1,h1 = boundingRect(contour)
        if h1>5 and w1>5:
            rectangle(img2, (x+x1,y+y1), (x+x1+w1,y+y1+h1), (255,0,0),1)
            word = thresh[y+y1:y+y1+h1,x+x1:x+x1+w1]
            col = 0
            while col<w1:
                if any(x==255 for x in word[:,col]):
                    beg = col
                    while any(x==255 for x in word[:,col]):
                        col+=1

                    start = y+y1
                    end = y+y1+h1-1

                    while all(c==0 for c in thresh[start,x+x1+beg:x+x1+col]):
                        start+=1

                    while all(c==0 for c in thresh[end,x+x1+beg:x+x1+col]):
                        end-=1

                    imwrite('letters2/character'+str(image_count)+'.png' ,img[start:end+1,x+x1+beg:x+x1+col])
                    image_count+=1

                    # imshow('aumn',img[start:end+1,x+x1+beg:x+x1+col])
                    # waitKey(0)

                col+=1
                
imshow('',img2)
waitKey(0)