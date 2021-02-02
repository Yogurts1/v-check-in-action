import requests
import os

# 参考这个网站https://sc.ftqq.com/获取自己的sckey，如果cookie失效会通过server酱提示
sckey = os.environ["SERVERCHAN_SCKEY"]
send_url = "https://sc.ftqq.com/%s.send" % (sckey)

# https://access.video.qq.com/user/auth_refresh 获取 cookie
login_cookie = os.environ["V_COOKIE_LOGIN"]
signin_cookie = os.environ["V_COOKIE_SIGNIN"]
auth_refresh_url = os.environ["V_AUTH_REFRESH_URL"]
Referer = 'https://v.qq.com'
Agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
headers_login = {
  'User-Agent': Agent,
  'Cookie': login_cookie,
  'Referer': Referer
}

# 测试一个签到请求
login = requests.get(auth_refresh_url, headers=headers_login)
cookie = requests.utils.dict_from_cookiejar(login.cookies)
# 如果请求返回信息包含no login说明cookie已经失效
if not cookie:
    print("auth_refresh error")
    params = {'text': '腾讯视频V力值签到通知', 'desp': '获取Cookie失败，Cookie失效'}
    requests.post(send_url, params=params)
urls = [
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7&_=1582364733058&callback=Zepto1582364712694',
    # 下载签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=6&_=1582366326994&callback=Zepto1582366310545',
    # 赠送签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=1555060502385&callback=Zepto1555060502385',
    # 签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=Zepto1582368297765 ',
    # 弹幕签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=1&_=1582997048625&callback=Zepto1582997031843',
    # 观看60分钟签到
]
count = 0
resultContent = ''
for url in urls:
    count += 1
    if (count == 1):
        print("发送每日下载任务请求")
    elif (count == 2):
        print("发送每日赠片任务请求")
    elif (count == 3):
        print("发送每日签到任务请求")
    elif (count == 4):
        print("发送每日弹幕任务请求")
    elif (count == 5):
        print("发送每日观影60分钟任务请求")
    refresh_cookie = cookie['vusession']
    headers_signin = {
      'User-Agent': Agent,
      'Cookie': signin_cookie + refresh_cookie + ';_video_qq_vusession=' + refresh_cookie + ';',
      'Referer': Referer
    }
    response = requests.get(url=url, headers=headers_signin)
    responseContent = response.content.decode("utf-8")
    print(responseContent)
    resultContent += responseContent + '\n\n'

params = {'text': '腾讯视频V力值任务签到结果通知', 'desp': resultContent}
requests.post(send_url, params=params)
print('已通知到 server 酱')
