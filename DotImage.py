from sys import argv
import cv2

def scale_image(img, scale_percent): 
    height, width = img.shape[:2] # Get height and width from the image
    width = int(width* scale_percent / 100) # Calculate the new width base on scale_percent
    height = int(height * scale_percent / 100) # Calculate the new height base on scale_percent
    dim = (width, height)

    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

def create_dot_image(img, limiar=100):
    height, width = img.shape[:2] # Get height and width from the image

    dot_image = ''

    for y in range(height): # For each line
        for x in range(width): # For each column
            if img[y][x] > limiar: # If the pixel > limiar, add . to dot image
                dot_image += '.'
            else: # Else, add (space) to dot image
                dot_image += ' '
        dot_image += '\n'
    
    return dot_image

def main(file):
    img = cv2.imread(file) # Read image

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to gray scale

    img_gray_scaled = scale_image(img_gray, 20) # Resize the image

    print(create_dot_image(img_gray_scaled, int(argv[1]) if len(argv) > 1 else 100)) # Create the dot image. The Limiar is 100 by default.

if __name__ == '__main__':
    main('./wazowski.jpg')
