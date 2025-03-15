# Puzzle Piece Matcher 🧩  

This script finds a puzzle piece in a background image using edge detection and template matching with OpenCV. This is useful for solving Captchas on chinese e-commerce sites such as Taobao.

## Requirements  

Install dependencies:  

```bash
pip install opencv-python numpy
```

## How It Works  

1. Loads a background and a puzzle piece image.  
2. Extracts edges using Laplacian operator.
3. Matches the puzzle piece in the background.
4. Highlights the match with a red rectangle.  

## Usage  

1. Place your images in:  
   - Background: `./samples/background/cat_head.jpg`  
   - Puzzle Piece: `./samples/piece/cat_head.png`  
2. Run:  

```bash
python detect.py
```

3. The script will display the matched result and print:  

```
Top-left corner of the puzzle piece: (x, y)
```
