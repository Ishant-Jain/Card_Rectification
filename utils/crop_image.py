from rembg import remove
import cv2
import numpy as np

def crop_image(image):
    # output_path = f'/home/ishant/bg_removed_{filename.split(".")[0]}.png'
    # image = cv2.imread(output_path, cv2.IMREAD_UNCHANGED)

    if image.shape[2] != 4:
        raise Exception("Image does not have an alpha channel!")

    # Extract alpha channel
    alpha = image[:, :, 3]

    # Create binary mask where alpha > 0
    _, thresh = cv2.threshold(alpha, 1, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assume the largest contour is the ID card
    c = max(contours, key=cv2.contourArea)

    # Approximate contour to a polygon (ideally a quadrilateral)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) != 4:
        raise Exception("Couldn't detect 4 corners. Try adjusting the approximation factor.")

    # Get the 4 corner points
    pts = approx.reshape(4, 2)

    # Sort points in order: top-left, top-right, bottom-right, bottom-left
    def order_points(pts):
        rect = np.zeros((4, 2), dtype="float32")

        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]  # Top-left
        rect[2] = pts[np.argmax(s)]  # Bottom-right

        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]  # Top-right
        rect[3] = pts[np.argmax(diff)]  # Bottom-left

        return rect

    rect = order_points(pts)

    # Compute width and height of new image
    (tl, tr, br, bl) = rect
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    # Destination points for the top-down view
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # Perspective transform
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped