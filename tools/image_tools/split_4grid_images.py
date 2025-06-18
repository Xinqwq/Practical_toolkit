import os
from PIL import Image

# 获取当前脚本所在文件夹
folder_path = os.path.dirname(os.path.abspath(__file__))

# 创建输出文件夹 splits
output_folder = os.path.join(folder_path, 'splits')
os.makedirs(output_folder, exist_ok=True)

# 支持的图片格式
image_extensions = ('.jpg', '.jpeg', '.png', '.webp')

# 遍历当前文件夹中的所有图片
for filename in os.listdir(folder_path):
    if filename.lower().endswith(image_extensions):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with Image.open(file_path) as img:
                width, height = img.size  # 获取图像尺寸

                mid_w = width // 2
                mid_h = height // 2

                # 切割成四部分
                top_left = img.crop((0, 0, mid_w, mid_h))
                top_right = img.crop((mid_w, 0, width, mid_h))
                bottom_left = img.crop((0, mid_h, mid_w, height))
                bottom_right = img.crop((mid_w, mid_h, width, height))

                # 获取文件名和扩展名
                name, ext = os.path.splitext(filename)

                # 生成保存路径
                top_left.save(os.path.join(output_folder, f'{name}_top_left{ext}'))
                top_right.save(os.path.join(output_folder, f'{name}_top_right{ext}'))
                bottom_left.save(os.path.join(output_folder, f'{name}_bottom_left{ext}'))
                bottom_right.save(os.path.join(output_folder, f'{name}_bottom_right{ext}'))

                print(f"已分割并保存：{filename}")
        except Exception as e:
            print(f"处理图片失败：{filename}，错误信息：{e}")
