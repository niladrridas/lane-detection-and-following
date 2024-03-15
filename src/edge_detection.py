import cv2

def detect_edges(image):
    """
    Detect edges in the input image using Canny edge detection.

    Args:
        image (numpy.ndarray): Input image.

    Returns:
        numpy.ndarray: Image with detected edges.
    """
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Perform Canny edge detection
    edges = cv2.Canny(blurred_image, 50, 150)
    
    return edges
