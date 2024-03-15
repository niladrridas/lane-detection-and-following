# Example usage script for Lane Detection and Following module

# Import necessary modules
import cv2
from src import edge_detection, hough_transform, lane_detection, lane_tracking, lane_following, visualization

# Load test image
image_path = 'data/testing_images/test_image.jpg'
image = cv2.imread(image_path)

# Preprocess image (if needed)
# image = preprocess_image(image)

# Perform edge detection
edges = edge_detection.detect_edges(image)

# Apply Hough transform
lines = hough_transform.detect_lines(edges)

# Detect lanes
lane_markers = lane_detection.detect_lanes(lines)

# Track lanes
lane_markers = lane_tracking.track_lanes(lane_markers)

# Follow lanes
result = lane_following.follow_lanes(image, lane_markers)

# Visualize result
visualization.visualize_result(image, result)
