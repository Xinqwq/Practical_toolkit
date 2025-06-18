# Practical Toolkit: Image Tools 🖼️🛠️

Welcome to **Practical Toolkit**! This repository contains a collection of Python scripts designed for various image processing tasks using the **Pillow** library. All of the image-related tools are stored in the `tools/image_tools` directory.

This toolkit allows you to automate image format conversions, perform batch operations, and split images efficiently. Here are some of the most useful tools included.

## 🛠️ Tools Overview

The following tools are included in the `image_tools/` directory:

### 1. **Convert JPG to PNG**: `convert_jpg_to_png.py` 🖼️➡️🖼️
   - Converts all `.jpg` images in the directory to `.png` format.

### 2. **Convert WebP to PNG**: `convert_webp_to_png.py` 🌐➡️🖼️
   - Converts all `.webp` images in the directory to `.png` format.

### 3. **Mirror Images**: `photos_mirrored.py` ←🔄→
   - Applies a horizontal flip to all images in the directory.

### 4. **Split 4-Grid Images**: `split_4grid_images.py` 🖼️➡️🖼️🖼️🖼️
   - Splits rectangular images (both landscape and portrait) into 4 smaller images.
   - Automatically saves them in the `splits/` folder, ensuring you get 4 equal parts: top-left, top-right, bottom-left, and bottom-right.

## 🚀 Getting Started

These tools are meant to be used as standalone Python scripts. They can process images in bulk and are very easy to use.

### 📦 Prerequisites

To use these scripts, you need to have **Python** and **Pillow** installed:

1. Install Python from the official website: https://www.python.org/downloads/
2. Install the **Pillow** library. You can install it using pip:

```bash
pip install pillow
```

###  💡Usage
Here’s how you can use each of these tools in your local environment.

1. Convert JPG to PNG:
```bash
python tools/image_tools/convert_jpg_to_png.py
```
This will convert all .jpg images in the directory to .png format.

2. Convert WebP to PNG:
```bash
python tools/image_tools/convert_webp_to_png.py
```
This script will convert all .webp images to .png format.

3. Mirror Images:
```bash
python tools/image_tools/photos_mirrored.py
```
This will horizontally flip all images in the directory and save them with _mirrored appended to their names.

4. Split 4-Grid Images:
```bash
python tools/image_tools/split_4grid_images.py
```
This will split all images in the directory into 4 parts: top-left, top-right, bottom-left, and bottom-right. The new images will be saved in a splits/ folder.

### 🗂️ Directory Structure
```
Practical_toolkit/
├── tools/
│   └── image_tools/
│       ├── convert_jpg_to_png.py
│       ├── convert_webp_to_png.py
│       ├── photos_mirrored.py
│       └── split_4grid_images.py
└── README.md
```
### ⚠️ Notes
Make sure the images you want to process are in the same directory as the script or provide the appropriate paths in the scripts.

These tools work on .jpg, .png, .webp image formats, but you can modify the scripts if you need to support other formats.

### 🤝 Contributions
Feel free to contribute to this project! You can open issues for bugs or feature requests, or fork the repository to add new tools.

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.