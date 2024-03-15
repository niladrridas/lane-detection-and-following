import cv2

def detect_lines(edges):
    """
    Detect lines in the edge-detected image using Hough transform.

    Args:
        edges (numpy.ndarray): Edge-detected image.

    Returns:
        list: List of lines detected in the image.
    """
    # Apply Hough transform to detect lines
    lines = cv2.HoughLinesP(edges, 1, cv2.cv.CV_PI / 180, 50, minLineLength=50, maxLineGap=100)
    
    return lines
