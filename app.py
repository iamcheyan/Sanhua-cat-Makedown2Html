import os
import markdown
from jinja2 import Template
import re
from flask import Flask, send_file
import configparser

# 加载看门狗
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 创建 ConfigParser 对象，读取配置文件
config = configparser.ConfigParser()
config.read('config.cfg', encoding='utf-8')

# 获取 directories 节下的参数值
content_dir = config.get('directories', 'content_dir')
output_dir = config.get('directories', 'output_dir')
template_dir = config.get('directories', 'template_dir')

# app = Flask(__name__, static_folder='html/static')
app = Flask(__name__, static_folder='html', static_url_path='')

# 插件
from plugins.compressor import compress_and_copy_files, compress_html  # 压缩html js css
from plugins.time_plugin import get_current_time    # 获取各种时间写入模版中
from plugins.copy_dir import copy_dir    # 高级复制
from plugins.darkmode.darkmode import add_darkmode  # 夜间模式

# markdown2html 主方法
def process_md_files(content_dir, template_dir, output_dir):
    for md_file in os.listdir(content_dir):
        if md_file.endswith('.md'):
            md_base_name = os.path.splitext(md_file)[0]
            html_file = os.path.join(template_dir, f'{md_base_name}.html')

            # 检查 content_dir 目录里的 md 文件是否有对应的 html 模板文件
            if os.path.exists(html_file):
                # 读取 md 文件内容
                with open(os.path.join(content_dir, md_file), 'r', encoding='utf-8') as f:
                    md_content = f.read()

                # 提取描述标记之间的内容
                matches = re.findall(r'<!--\s*(.*?)\s*-->\s*(.*?)\s*(?=<!--|$)', md_content, re.DOTALL)

                # template_content = ""
                with open(html_file, 'r', encoding='utf-8') as f:
                    template_content = f.read()

                for match in matches:
                    name = match[0].strip()
                    content = match[1].strip()

                    # 将描述内容转换为 HTML
                    html_content = markdown.markdown(content)

                    # 替换模板文件中的 {描述} 为提取的内容
                    template_content = re.sub(r'\{\s*' + re.escape(name) + r'\s*\}', html_content, template_content)

                # 渲染模板文件
                template = Template(template_content)
                rendered_html = template.render()

                # 写入到 HTML 文件
                html_output_file = os.path.join(output_dir, f'{md_base_name}.html')
                with open(html_output_file, 'w', encoding='utf-8') as f:
                    compressed_html = compress_html(rendered_html)
                    f.write(compressed_html)

                print(f'已输出{html_output_file}')
            else:
                print(f'未找到对应的HTML模板文件：{html_file}')

# 处理 Markdown 文件
process_md_files(content_dir, template_dir, output_dir)

# 夜间模式插件配置
add_darkmode(output_dir, html_file='index.html')

# 拷贝 static 目录到输出目录
compress_and_copy_files(template_dir, output_dir)   # 压缩和拷贝静态文件
copy_dir(os.path.join(content_dir, 'img'), os.path.join(output_dir, 'img'))

# 启动 Flask 应用
@app.route('/')
def index():
    # add_darkmode(output_dir)    # 添加暗黑模式插件
    return send_file('html/index.html')

if __name__ == '__main__':
    app.run(debug=True)