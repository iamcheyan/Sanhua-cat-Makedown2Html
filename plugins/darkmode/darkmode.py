import os
import shutil

def add_darkmode(output_dir, html_file='index.html'):
    # 合并静态文件到输出目录的 static 文件夹中
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    dest_dir = os.path.join(output_dir, 'static')
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for filename in os.listdir(static_dir):
        src_path = os.path.join(static_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        if os.path.isfile(src_path):
            if not os.path.exists(dest_path):
                shutil.copy2(src_path, dest_path)

    # 在 index.html 文件中添加 JavaScript 代码
    for filename in os.listdir(output_dir):
        if filename == html_file:
            path = os.path.join(output_dir, filename)
            with open(path, 'r+', encoding='utf-8') as f:
                content = f.read()
                new_content = content.replace('</body>', '''
                    <script src="static/js/darkmode-js.min.js"></script>
                    <script>
                        const options = {
                            bottom: '32px',
                            right: '32px',
                            time: '0.5s',
                            saveInCookies: true,
                            label: '🌓',
                            autoMatchOsTheme: true
                        };
                        const darkmode = new Darkmode(options);
                        darkmode.showWidget();
                    </script>
                    </body>
                ''')
                f.seek(0)
                f.write(new_content)
                f.truncate()