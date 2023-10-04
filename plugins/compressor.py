import os
import shutil
import csscompressor
import jsmin
import htmlmin

def compress_and_copy_files(template_dir, output_dir):
    for root, dirs, files in os.walk(os.path.join(template_dir, 'static')):
        for file in files:
            # 只处理CSS和JS文件
            if file.endswith('.css'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, 'static', file)
                with open(input_path, 'r', encoding='utf-8') as f_in:
                    with open(output_path, 'w', encoding='utf-8') as f_out:
                        compressed_css = csscompressor.compress(f_in.read())
                        f_out.write(compressed_css)
            elif file.endswith('.js'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, 'static', file)
                with open(input_path, 'r', encoding='utf-8') as f_in:
                    with open(output_path, 'w', encoding='utf-8') as f_out:
                        compressed_js = jsmin.jsmin(f_in.read())
                        f_out.write(compressed_js)
            else:
                # 其他文件直接拷贝
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, 'static', file)
                shutil.copyfile(input_path, output_path)

def compress_html(html):
    return htmlmin.minify(html)