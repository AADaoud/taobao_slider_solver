import cv2
import numpy as np

background_path = './samples/background/cat_head.jpg'
puzzle_piece_path = './samples/piece/cat_head.png'

background = cv2.imread(background_path, cv2.IMREAD_GRAYSCALE)
puzzle_piece_rgba = cv2.imread(puzzle_piece_path, cv2.IMREAD_UNCHANGED)

alpha = puzzle_piece_rgba[:, :, 3]
puzzle_piece_bgr = puzzle_piece_rgba[:, :, :3]

puzzle_piece_gray = cv2.cvtColor(puzzle_piece_bgr, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(alpha, 1, 255, cv2.THRESH_BINARY)

puzzle_piece_gray = cv2.bitwise_and(puzzle_piece_gray, puzzle_piece_gray, mask=mask)

laplacian_puzzle = cv2.Laplacian(puzzle_piece_gray, cv2.CV_64F, ksize=3)
laplacian_puzzle = cv2.convertScaleAbs(laplacian_puzzle)
laplacian_puzzle = cv2.bitwise_and(laplacian_puzzle, laplacian_puzzle, mask=mask)
laplacian_background = cv2.Laplacian(background, cv2.CV_64F, ksize=3)
laplacian_background = cv2.convertScaleAbs(laplacian_background)

# Threshold the Laplacian images to create binary images
_, thresh_puzzle = cv2.threshold(laplacian_puzzle, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, thresh_background = cv2.threshold(laplacian_background, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


result = cv2.matchTemplate(thresh_background, thresh_puzzle, cv2.TM_CCOEFF_NORMED)

# Find the best match location
_, max_val, _, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = thresh_puzzle.shape

# Draw a rectangle around the matched region
bottom_right = (top_left[0] + w, top_left[1] + h)
background_color = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)
cv2.rectangle(background_color, top_left, bottom_right, (0, 0, 255), 2)

# Display the result
cv2.imshow('Matched Outline', background_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Top-left corner of the puzzle piece in the background: {top_left}")