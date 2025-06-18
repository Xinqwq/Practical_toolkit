import os
from PIL import Image

# 设置输入和输出文件夹路径
folder_path = os.getcwd()

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):  # 只处理图片文件
        # 获取文件的完整路径
        img_path = os.path.join(folder_path, filename)
        
        # 打开图片文件
        with Image.open(img_path) as img:
            # 进行左右镜像对称操作
            mirrored_img = img.transpose(Image.FLIP_LEFT_RIGHT)

            # 获取文件名和扩展名
            name, ext = os.path.splitext(filename)
            
            # 设置输出文件路径
            output_path = os.path.join(folder_path, name + '_mirrored' + ext)
            
            # 保存镜像对称后的图片
            mirrored_img.save(output_path)

            print(f'已转换：{filename} 到镜像对称格式')
