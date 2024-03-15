import cv2

def visualize_result(image, result):
    """
    Visualize the lane detection and following result.

    Args:
        image (numpy.ndarray): Original input image.
        result (numpy.ndarray): Image with lane following overlay.
    """
    # Display original image
    cv2.imshow('Original Image', image)
    
    # Display result image
    cv2.imshow('Result with Lane Following', result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
