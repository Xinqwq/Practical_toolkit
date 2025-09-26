# Practical Toolkit: Image Tools 🖼️🛠️

<details>
<summary>🇺🇸 English</summary>

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

### 5. **Remove Background from pics**: `remove_bg_png.py` 🖼️➡️🖼️🖼️🖼️
   - Removes the background from images, keeping only the main subject. You can choose from models for human images or models for objects images. Set different parameters to get your own results!


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
│       ├── split_4grid_images.py
│       └── remove_bg_png.py
└── README.md
```
### ⚠️ Notes
Make sure the images you want to process are in the same directory as the script or provide the appropriate paths in the scripts.

These tools work on .jpg, .png, .webp image formats, but you can modify the scripts if you need to support other formats.

Regarding tool `#5` - `remove_bg_png.py`, additional dependencies `rembg` and `onnxruntime` are required, make sure they are installed before running.

### 🤝 Contributions
Feel free to contribute to this project! You can open issues for bugs or feature requests, or fork the repository to add new tools.

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

</details>

<details open> 
<summary>🇨🇳 中文</summary>
欢迎来到 **Practical Toolkit**！  
本仓库包含一组使用 **Pillow** 库编写的 Python 脚本，用于各种图像处理任务。所有与图像相关的工具都存放在 `tools/image_tools` 目录下。

该工具集可以帮助你自动化图像格式转换、批量处理、去除背景，以及高效地切分图片。以下是包含的实用工具：

## 🛠️ 工具概览

以下工具包含在 `image_tools/` 目录下：

### 1. **JPG 转 PNG**: `convert_jpg_to_png.py` 🖼️➡️🖼️
   - 将目录下所有 `.jpg` 图片转换为 `.png` 格式。

### 2. **WebP 转 PNG**: `convert_webp_to_png.py` 🌐➡️🖼️
   - 将目录下所有 `.webp` 图片转换为 `.png` 格式。

### 3. **镜像图片**: `photos_mirrored.py` ←🔄→
   - 对目录下的所有图片进行水平镜像翻转。

### 4. **四宫格切图**: `split_4grid_images.py` 🖼️➡️🖼️🖼️🖼️
   - 将矩形图片（横向或纵向）切分为 4 张小图。  
   - 自动保存到 `splits/` 文件夹中，得到左上、右上、左下、右下四个等份。

### 5. **去除图片背景**: `remove_bg_png.py` 🪄
   - 去除图片背景，仅保留主体。你可以选择 **人物模型** 或 **物体模型** 来处理，并通过不同参数调整获得理想效果。

## 🚀 快速开始

这些工具作为独立的 Python 脚本使用，可以进行批量处理，使用方法非常简单。

### 📦 前置条件

要运行这些脚本，你需要安装 **Python** 以及以下依赖：

1. 从官网下载并安装 Python: https://www.python.org/downloads/  
2. 安装必要的库：
```bash
pip install pillow rembg onnxruntime
```
💡 使用方法
以下是每个工具的使用示例：

1.  JPG 转 PNG:
```bash
python tools/image_tools/convert_jpg_to_png.py
```

2.  WebP 转 PNG:

```bash
python tools/image_tools/convert_webp_to_png.py
```
3.  镜像翻转:

```bash
python tools/image_tools/photos_mirrored.py
```

4.  四宫格切图:
```bash
python tools/image_tools/split_4grid_images.py
```
5.  去除图片背景:

```bash
python tools/image_tools/remove_bg_png.py
```
根据需要选择人像模型或物体模型，选好参数模式或者自定义参数脚本会自动应用。

🗂️ 目录结构
```
Practical_toolkit/
├── tools/
│   └── image_tools/
│       ├── convert_jpg_to_png.py
│       ├── convert_webp_to_png.py
│       ├── photos_mirrored.py
│       ├── split_4grid_images.py
│       └── remove_bg_png.py
└── README.md
```
⚠️ 注意
确保要处理的图片和脚本在同一目录，或者在脚本里指定路径。

这些工具支持 `.jpg, .png, .webp`等格式，如果需要支持其他格式，可以自行修改脚本。

`remove_bg_png.py` 需要额外依赖 `rembg` 和 `onnxruntime`，运行前请确保已安装。

🤝 贡献
欢迎对本项目进行贡献！你可以提交 `issue` 报告 `bug` 或提出新功能，也可以 `fork` 本仓库来添加新工具。

📄 许可证
本项目使用 `MIT License` - 详见 `LICENSE` 文件。
</details>
