# ytdlp-tgbot
## docker
拉取
```
qimooo/ytdlp-tgbot:latest
```
设置环境变量 BOT_TOKEN
默认保存位置 /Downloads
## 直接运行
拉取
```
git clone https://github.com/qi-mooo/ytdlp-tgbot
```
安装依赖
```
cd ytdlp-tgbot && pip install -r requirements.txt
```
设置环境变量
```
export BOT_TOKEN=token
```
运行
```
python app.py
```
可选，修改下载目录，编辑 app.py
```
SAVE_DIR = "/Downloads"
```
