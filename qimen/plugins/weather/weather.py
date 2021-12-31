from nonebot import on_command, CommandSession
import urllib.request
import gzip
import json


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    city = session.current_arg_text.strip()
    # 如果除了命令的名字之外用户还提供了别的内容，即用户直接将城市名跟在命令名后面，
    # 则此时 city 不为空。例如用户可能发送了："天气 南京"，则此时 city == '南京'
    # 否则这代表用户仅发送了："天气" 二字，机器人将会向其发送一条消息并且等待其回复
    if not city:
        city = (await session.aget(prompt='你想查询哪个城市的天气呢？')).strip()
        # 如果用户只发送空白符，则继续询问
        while not city:
            city = (await session.aget(prompt='要查询的城市名称不能为空呢，请重新输入')).strip()
    # 获取城市的天气预报
    weather_report = await get_weather_data(city)
    # 向用户发送天气预报
    await session.send(weather_report)


async def get_weather_data(city: str) -> str:
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(f'{city}')  #带后缀的url链接
    weather_data = urllib.request.urlopen(url1).read()  #获取数据
    weather_data = gzip.decompress(weather_data).decode('utf-8') #调整编码形式
    weather_dict = json.loads(weather_data)
    forecast = weather_dict.get('data').get('forecast')
    city1 = weather_dict.get('data').get('city') + '的天气情况：'
    type = '天气：' + forecast[0].get('type')
    wendu = '温度：' + weather_dict.get('data').get('wendu')+'℃ '
    wind = '风向：' + forecast[0].get('fengxiang')
    high = '高温：' + forecast[0].get('high')
    low = '低温：' + forecast[0].get('low')
    date = '日期：' + forecast[0].get('date')
    tip = 'Tip~：' + weather_dict.get('data').get('ganmao')
    temp = city1 + '\n' + '\t' + type + '\n' + '\t' + wendu + '\n' + '\t' + wind + '\n' + '\t' + high + '\n' + '\t' + low + '\n' + '\t' + date + '\n' + tip
    return temp