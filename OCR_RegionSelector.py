import cv2
import random

# Define the path to your image file
path = 'E:/Downloads/Test/CamScanner 14.10.2024 09.48_1.jpg'  # Update this to the correct path on your local system

scale = 0.5
circles = []
counter = 0
counter2 = 0
point1 = []
point2 = []
myPoints = []
myColor = []

# Mouse callback function
def mousePoints(event, x, y, flags, params):
    global counter, point1, point2, counter2, circles, myColor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter == 0:
            point1 = int(x // scale), int(y // scale)
            counter += 1
            myColor = (random.randint(0, 2) * 200, random.randint(0, 2) * 200, random.randint(0, 2) * 200)
        elif counter == 1:
            point2 = int(x // scale), int(y // scale)
            type = input('Enter Type: ')
            name = input('Enter Name: ')
            myPoints.append([point1, point2, type, name])
            counter = 0
        circles.append([x, y, myColor])
        counter2 += 1

# Read and resize the image
img = cv2.imread(path)
if img is None:
    print("Error: Could not read the image file. Check the path.")
else:
    img = cv2.resize(img, (900, 900))  # Resize to 900x900 pixels
    img = cv2.resize(img, (0, 0), None, scale, scale)  # Scale the image

    while True:
        for x, y, color in circles:
            cv2.circle(img, (x, y), 3, color, cv2.FILLED)  # Draw circles at stored positions
        cv2.imshow("Original Image", img)  # Show image in a window
        cv2.setMouseCallback("Original Image", mousePoints)  # Set callback for mouse events
        if cv2.waitKey(1) & 0xFF == ord('s'):  # Wait for 's' key to stop
            print(myPoints)
            break

cv2.destroyAllWindows()  # Close all OpenCV windows
