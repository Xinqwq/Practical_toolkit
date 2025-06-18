import os
from PIL import Image

# 设置输入和输出文件夹路径（这里是同一个文件夹）
folder_path = os.getcwd()

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.lower().endswith('.webp'):  # 只处理 .webp 文件
        # 获取文件的完整路径
        webp_path = os.path.join(folder_path, filename)
        
        # 打开 .webp 文件
        with Image.open(webp_path) as img:
            # 获取文件名和扩展名
            name, _ = os.path.splitext(filename)
            
            # 设置输出文件路径（转换为 PNG 格式）
            output_path_png = os.path.join(folder_path, name + '.png')
            
            # 保存为 PNG 格式
            img.save(output_path_png, 'PNG')

            print(f'已转换：{filename} 到 PNG 格式')
