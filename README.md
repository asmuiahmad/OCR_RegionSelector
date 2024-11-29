
# OCR Region Selector

## Description
This Python program allows users to interactively annotate an image using the OpenCV library. 
It enables you to click on points within an image, create custom annotations by inputting a type and a name for the selected area, and draw circles at the clicked points. 
The program saves these annotations and allows you to visualize your selections in real-time.

## Features
- **Interactive Image Annotation**: Click anywhere on the image to place a point and create an annotation with custom data (type and name).
- **Random Circle Colors**: Each point gets a randomly generated color for visual distinction.
- **Point Tracking**: Stores points and their corresponding annotations for further use.
- **Image Scaling**: The image is automatically resized to fit the window with a customizable scaling factor.
- **Exit on Keypress**: The program runs until the user presses the 's' key to save and exit.

## Prerequisites
Before running the script, make sure you have the following:
- **Python 3.x**: Ensure Python 3 or higher is installed on your system.
- **OpenCV**: The script relies on the OpenCV library for image processing and mouse interaction.

## Installation
1. Clone the repository or download the script.
You can download the ```image_interaction.py``` script or clone it from a repository (if applicable).

2. Install dependencies.
To install OpenCV, run the following command:
```python
pip install -r requirements.txt
```

4. Update the image path.
In the script, make sure to update the path variable to point to the location of the image you want to annotate. For example:
```markdown
path = 'path/to/your/image/images-any-extensions.png/jpg/jpeg'
```
Make sure that the path is correct and points to an existing image on your local system.

## Usage
1. Run the script.
Once you have installed OpenCV and set the correct image path, you can run the script from the command line as follows:
```python
OCR_RegionSelector.py
```

3. Interact with the image.
The image will open in a new window, and you can interact with it using your mouse:
- **Click on the image:** Each click places a point on the image. The program will ask you to enter a "Type" and "Name" for the selected region.
- **Exit the program:** Press the 's' key to stop the interaction and print the list of annotated points to the console.

3. Annotate Multiple Points.
You can click multiple locations on the image, and the program will store and display each point's details (including random colors) in real-time.

## Example Output:
After clicking and annotating several points, the program will display something like this in the terminal when you exit:
```python
[[((x1, y1), (x2, y2), 'Type1', 'Name1')],
[(x3, y3), (x4, y4), 'Type2', 'Name2')]]
```

This output represents a list of annotations, each containing:

- Two points: Start point and end point (coordinates).
- A "Type" and "Name" for each annotation.
- also Type have two type : **1. text, 2. sign**

## Troubleshooting
- **Error: Could not read the image file:** If you receive an error stating that the image couldn't be read, make sure the path variable points to an existing file. Verify that the file path is correct, and the image is accessible.

- **No image window appears:** Ensure that you have OpenCV properly installed. You can verify this by running the command pip show opencv-python to check the installation.
