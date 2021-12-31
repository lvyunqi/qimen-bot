import urllib.request
import gzip
import json

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