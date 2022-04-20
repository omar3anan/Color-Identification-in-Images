#AUTHOR: Omar Anan Abou-Romia
#3. Color Identification in Images

#Importing the required libraries
import cv2
import pandas as pd


# reading image
img_path = r"E:\Desktop\SPARK\Color-Identfication\test1.jpg" #test case number 1
#img_path = r"E:\Desktop\SPARK\Color-Identfication\test2.jpg"  #test case number 2
#img_path = r"E:\Desktop\SPARK\Color-Identfication\test3.jpg"   #test case number 3
img = cv2.imread(img_path) 
#img_resize = cv2.resize(img, (1200, ))

# declare some global variables
X = Y = r = g = b = 0
Clicked = False

#Reading the .csv file(Containing all the colors,hex,RGB components) and naming the columns

myArr = ['Color', 'ColorName', 'Hex', 'R', 'G', 'B']
csv = pd.read_csv('colors.csv', names=myArr)

#Function to get the coordinates of the mouse pointer when double clicked on the image
#Saving the RGB values on those coordinates into the variables
def draw(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONUP:
        global X, Y, r, g, b, Clicked
        Clicked = True
        X = x
        Y = y
        b, g, r = img[y, x]
        b = int(b)
        r = int(r)
        g = int(g)

#Creating the window for image
cv2.namedWindow('ColorDetector')
#Binding the draw_function to the mouse pointer
cv2.setMouseCallback('ColorDetector', draw)

#Function to compare the RGB values on (x,y) coordinates of the image
#Returning the color name
def GetColorName(R, G, B):
    min = 1000000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G -
                                                int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))

        if d <= min:
            min = d
            cname = csv.loc[i, 'ColorName']

    return cname

#Binding the draw_function to the mouse pointer
while True:
    cv2.imshow('ColorDetector', img)

    if Clicked:
        cv2.rectangle(img, (0, 20), (600, 60), (b, g, r),  -1)
        text = GetColorName(r, g, b) + ' R = ' + str(r) + \
            ' G = ' + str(g) + ' B = ' + str(b)

        if r + g + b >= 500:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, text, (50, 50), 2, 0.8,
                        (255, 255, 255), 2, cv2.LINE_AA)
    Clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
