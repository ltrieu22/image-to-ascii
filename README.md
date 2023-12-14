# Image to ascii

This Python script converts images into ASCII art. It takes an image file as input and outputs a text file representing the image in ASCII characters.

# How does it work? 
- Image Resizing: Automatically resizes the image to a specified width while maintaining aspect ratio, making it suitable for ASCII conversion.
- Grayscale Conversion: Converts the image to grayscale to simplify the process of mapping pixels to ASCII characters.
- ASCII Conversion: Maps grayscale pixels to a set of ASCII characters, creating the ASCII art.

# Usage
1. Make sure you have Python and Pillow, PIL (Python Imaging Library), installable via ```pip install Pillow```
2. Run the scipt in a Python environment
3. Enter the full path to the desired image when prompted. Giving a wrong path will result into an error and the script will ask you for the path again. Typing "quit" will exit the program


### Example
To convert an image located at `E:\pictures\example.png`, enter the path when prompted:

```bash
Please enter path to the desired image or type 'quit' to exit: 
E:\pictures\example.png
```

### Example image
![Untitled](https://github.com/ltrieu22/image-to-ascii/assets/144845781/f00fb5a8-27ae-4c1c-80fb-58ea35c51c42)
![image](https://github.com/ltrieu22/image-to-ascii/assets/144845781/39706557-be33-4504-8a24-0a827d013f3a)
