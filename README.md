# Channel_Post

一个用 Telegram bot api 来发布频道消息，并通过bot匹配唯一标识符来发放私密消息的管理工具

## 快速开始

* 从 [@BotFather](https://t.me/BotFather) 那里创建一个机器人，获得该机器人的bot_token，应形如：

    bot_token = "xxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxx"

    这步不会请Google。

* 动动你的小手拉取本项目的源码
```shell
apt install -y git && git clone https://github.com/adm1nSQL/channel_post.git && cd channel_post
```

* 安装依赖 Python 3.6 以上
您可以用以下命令，在当前项目目录下运行以快速安装环境：
Windows:

```
pip install pyTelegramBotAPI
```

Linux:

```
pip3 install pyTelegramBotAPI
```

* 需要修改的地方：第6-10行、第50行，已做中文注释，6-19行的信息您可以从 [@getidsbot](https://t.me/getidsbot) 得到，第50行务必修改为您自己的bot链接，将yige_bot替换为您自己的bot用户名

* 运行
```shell
python3 main.py
```

* 挂起
```shell
可以使用screen或者pm2等工具，将程序窗口挂在后台运行
```
