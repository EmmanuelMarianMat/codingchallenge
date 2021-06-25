from cv2 import *

img = imread('TextDocument.png')
grey_img = cvtColor(img, COLOR_RGB2GRAY)

valid_row_start = 0
while not any(col==255 for col in grey_img[valid_row_start]):
    valid_row_start+=1

valid_row_end = -1
while not any(col==255 for col in grey_img[valid_row_end]):
    valid_row_end-=1

valid_col_start = 0
found = False
while valid_col_start<len(img[0]):
    for i in range(len(img)):
        if grey_img[i][valid_col_start]==255:
            found = True
            break
    if found:
        break
    valid_col_start+=1

valid_col_end = -1
found = False
while valid_col_end>-len(img[0]):
    for i in range(len(img)):
        if grey_img[i][valid_col_end]==255:
            found = True
            break
    if found:
        break
    valid_col_end-=1

page = grey_img[valid_row_start:valid_row_end,valid_col_start:valid_col_end]

idx = 0
lines= []
while idx<len(page):
    if any(col<255 for col in page[idx]):
        start = idx
        idx+=1
        while any(col<255 for col in page[idx]):
            idx+=1
        end = idx-1
        lines.append((start,end))

    idx+=1


image_count = 1

for l in lines:
    (start,end) = l
    page_line_rows = page[start:end+1]
    col = 0

    while col<len(page[0]):
        if any(x<100 for x in page_line_rows[:,col]):
            beg = col
            while any(x<124 for x in page_line_rows[:,col]) or (
                sum(x<=156  for x in page_line_rows[:,col])>=2 and 
                sum(x<=124  for x in page_line_rows[:,col])>=1):
                col+=1


            s,e = 0,end-start
            while not any(col<255 for col in page_line_rows[s,beg:col]):
                    s+=1
            while not any(col<255 for col in page_line_rows[e,beg:col]):
                    e-=1
            imwrite('letters/character'+str(image_count).zfill(4)+'.png' ,page_line_rows[s:e+1,beg:col])
            image_count+=1
       
        col+=1

