import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
  plt.figure(figsize = (8, 8))
  if len(image.shape) == 2:
    plt.imshow(image, cmap = 'gray')
  else:
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  plt.title(title)
  plt.axis('off')
  plt.show()

def interactive_edge_detection(image_path):
  image = cv2.imread(image_path)
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  if image is None:
    print('Error loading image')
    return

  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  display_image("original grayscale image", gray_image)

  print("Select an option: ")
  print("1. Sobal Edge Detection")
  print("2. Canny Edge Detection")
  print("3. Laplacian Edge Detection")
  print("4. Gaussian Smoothing")
  print("5. Median Filtering")
  print("6. Exit")

  while True:
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
      sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize = 3)
      sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize = 3)
      combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
      display_image("Sobel Edge Detection", combined_sobel)
    elif choice == '2':
      print("adjustable thresholds for Canny (default: 100 and 200)")
      lower_thres = int(input("Enter lower threshold: "))
      upper_thres = int(input("Enter upper threshold: "))
      edges = cv2.Canny(gray_image, lower_thres, upper_thres)
      display_image("Canny Edge Detection", edges)
    elif choice == '3':
      laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
      abs_lap = np.abs(laplacian).astype(np.uint8)
      display_image("Laplacian Edge Detection", abs_lap)
    elif choice == '4':
      print("adjust kernel size for Gaussian blur (must be odd, default:5)")
      kernel_size = int(input("Enter kernel size (odd number): "))
      blurred = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
      display_image("Gaussian Smoothed Image", blurred)
    elif choice == '5':
      print("adjust kernel size for Median blur (must be odd, default:5)")
      kernel_size = int(input("Enter kernel size (odd number): "))
      median_filtering = cv2.medianBlur(image, kernel_size)
      median_display_tuple = ('Median Filtered Image', median_filtering)
      display_image(median_display_tuple[0], median_display_tuple[1]) # call display_image function correctly
    elif choice == '6':
      print('Exiting....')
      break
    else:
      print('Invalid choice. Please select a number between 1 and 6 (No other datatypes)')

interactive_edge_detection('apple.jpg')