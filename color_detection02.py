import cv2
import pandas as pd

img_path = r'D:\PROJECTS\Color detection\python-project-color-detection\colorpic.jpg'

img =cv2.imread(img_path)

clicked = False
r = g = b = x_pos = y_pos = 0

index = ["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv',names = index,header=None)

def draw_function(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,x_pos,y_pos,clicked
        clicked = True
        x_pos = x
        y_pos = y
        b,g,r = img[y,x]
        print(b , g ,r)
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)


def get_color_name(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i,"R"])) + abs(G - int(csv.loc[i,"G"])) + abs(B - int(csv.loc[i,"B"]))
        print( R ,"-", int(csv.loc[i,"R"]) , "+", G ,"-", int(csv.loc[i,"G"]) ,"+", B ,"-", int(csv.loc[i,"B"])) 
        print(d)

        if d <= minimum:
            minimum = d
            print("Minimum", d)
            cname = csv.loc[i,"color_name"]
            print(cname)
    return cname

while True:

    cv2.imshow("image",img)

    if clicked:
        ##            image,(start ponit),(end point) ,(color ), (thickness -1)
        cv2.rectangle(img, (20,20), (750,60), (b,g,r),-1)

        text = get_color_name(r,g,b) +' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

                ## img, text, start,font, fontscale, color , thickness, lineType
                ##                            white
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2, cv2.LINE_AA)

        if r + g + b >= 600:
            #                                    Black
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()             

