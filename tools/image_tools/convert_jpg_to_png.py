import os
from PIL import Image

# 获取当前文件夹路径
folder_path = os.getcwd()

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.lower().endswith('.jpg'):  # 只处理 .jpg 文件
        # 获取文件的完整路径
        jpg_path = os.path.join(folder_path, filename)
        
        # 打开 .jpg 文件
        with Image.open(jpg_path) as img:
            # 获取文件名和扩展名
            name, _ = os.path.splitext(filename)
            
            # 设置输出文件路径（转换为 PNG 格式）
            output_path = os.path.join(folder_path, name + '.png')
            
            # 保存为 PNG 格式
            img.save(output_path, 'PNG')

            print(f'已转换：{filename} 到 PNG 格式')
