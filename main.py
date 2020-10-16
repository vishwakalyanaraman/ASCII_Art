import cv2
import numpy as np

def main():
    CHAR_LIST = '@%#*+=-:. '
    num_chars = len(CHAR_LIST)
    
    print("Enter number of columns")
    num_cols = int(input())

    image = cv2.imread('images/test.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, width = image.shape

    cell_width = width / num_cols
    cell_height = cell_width *2
    num_cols = int(width/cell_width)

    num_rows = int(height/cell_height)

    output_image = open('images/out.txt', 'w')

    for i in range(num_rows):
        for j in range(num_cols):
            output_image.write(
                CHAR_LIST[min(int(np.mean(image[int(i * cell_height):min(int((i + 1) * cell_height), height),
                                          int(j * cell_width):min(int((j + 1) * cell_width),
                                                                  width)]) * num_chars / 255), num_chars - 1)])
        output_image.write("\n")
    output_image.close()


main()
