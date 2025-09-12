import cv2
import numpy as np

def acf(image, filter_type):
    filtered_image = image.copy()
    if filter_type == 'red_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'increase_red':
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == 'decrease_blue':
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    return filtered_image

image_path = 'apple.jpg'
image = cv2.imread(image_path)

if image is None:
    print('Error, image not found.')
else:
    filter_type = 'original'

    print("Press the following keys to apply filters:")
    print("'r' - Red Tint")
    print('"g" - Green Tint')
    print('"b" - Blue Tint')
    print('"i" - Increase Red')
    print('"d" - Decrease Blue')
    print('q - Quit')
    while True:
        filtered_image = acf(image, filter_type)
        cv2.imshow('filtered image', filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('i'):
            filter_type = 'increase_red'
        elif key == ord('d'):
            filter_type = 'decrease_blue'
        elif key == ord('q'):
            print("exiting...")
            break
        else:
            print("Invalid key, please press r, g, b, i, d, or q")

cv2.destroyAllWindows()