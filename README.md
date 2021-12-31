# QImen-Bot

#### 介绍
此项目基于 Nonebot 和 go-cqhttp 开发的QQ群娱乐机器人

#### 关于
本项目目前还是个半成品（qwq

#### 声明
此项目仅用于学习交流，请勿用于非法用途！

#### 安装教程

```
# 配置go-cqhttp
在 https://github.com/Mrs4s/go-cqhttp 下载Releases最新版本，运行后选择反向代理，
  然后将go-cqhttp的配置文件config.yml中的universal改为universal: ws://127.0.0.1:8080/ws
最后运行并登录go-cqhttp
# 获取代码
git clone https://gitee.com/QimenIDC/qimen-bot.git
# 进入目录
cd qimen_bot
# 安装依赖
pip install -r requirements.txt
# 基础配置
1、在config.py文件中
     SUPERUSERS = {123456}   # 填写你的QQ
     NICKNAME = {'小明', '明明'}   #修改为bot的称呼
# 开始运行
python bot.py
```

#### 已实现的功能
- [x] 天气查询

#### 使用说明

目前只有一个查询天气功能，只要发送的消息中包含“天气”就会自动恢复！
####示例
```
#今天南京天气怎么样？
#今天天气怎么样？
#小明，今天天气怎么样？

#/天气 南京
```