import os
import shutil

def copy_dir(src, dst):
    """
        递归复制目录及其内容
        使用该插件可以递归地复制源目录及其所有子目录和文件到目标目录。
        如果目标目录不存在，插件会自动创建。
        同时，该插件只会复制尚未存在或大小不同的文件，已经存在且大小相同的文件将不会被复制
    """
    for file_name in os.listdir(src):
        src_path = os.path.join(src, file_name)
        dst_path = os.path.join(dst, file_name)

        if os.path.isdir(src_path):
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
            copy_dir(src_path, dst_path)
        else:
            dst_dir = os.path.dirname(dst_path)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            if not os.path.exists(dst_path) or (
                    os.path.exists(dst_path) and os.path.getsize(src_path) != os.path.getsize(dst_path)):
                shutil.copy2(src_path, dst_path)
