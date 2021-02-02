import requests
import os

# 参考这个网站https://sc.ftqq.com/获取自己的sckey，如果cookie失效会通过server酱提示
sckey = os.environ["ServerChan_SCKEY"]
Cookie = os.environ["V_Cookie"]

# sckey = 'SCU60462T11c3c21ad120e4deae2ec672509b94e55d79b474e8dc0'
send_url = "https://sc.ftqq.com/%s.send" % (sckey)
# https://access.video.qq.com/user/auth_refresh
# Cookie = '_ga=GA1.2.1737263331.1539846482; pgv_pvid=5971493714; pgv_pvi=5310209024; RK=ARA4vTwgEG; ptcz=6f8e32350aa451a09ebdae38e95e0f478b8b501f89540deaafa1dd37a8315755; pac_uid=1_673308817; tvfe_boss_uuid=04691c7181424191; XWINDEXGREY=0; gr_user_id=8b2dadab-75fc-4bce-9438-ddd32e263529; grwng_uid=55ccf35f-93a9-4b70-ab7d-be75b496ead9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170153d90aec6e-08f9af188fdee3-39617b0f-2073600-170153d90afcbc%22%2C%22%24device_id%22%3A%22170153d90aec6e-08f9af188fdee3-39617b0f-2073600-170153d90afcbc%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; AMCV_248F210755B762187F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18298%7CMCMID%7C76116237142692787250663465248528106673%7CMCAAMLH-1571216664%7C11%7CMCAAMB-1580904356%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1570619064s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.3.0; pt_sms_phone=185******13; Qs_lvt_323937=1568880072%2C1589433246; Qs_pv_323937=3830025412850878500%2C4054250852665839600; ied_qq=o0673308817; video_platform=2; video_guid=53141063c58c27b4; sd_userid=95921602224781555; sd_cookie_crttime=1602224781555; iip=0; ptui_loginuin=673308817; LW_uid=a1j6W1D196K2I760t7P1i6B8r0; eas_sid=y1M621J1r6l2P7b0i7a158s7h7; LW_sid=01V6r1s1g6F2S7K1w5Y7h4s6U4; pgv_info=ssid=s2054814796; appid=wxa75efa648b60994b; _video_qq_appid=wxa75efa648b60994b; main_login=wx; _video_qq_main_login=wx; access_token=41_DK8lfY5DnnX8NQfy2p5llBomrYVj_uRuygZfoUcWLcc8Ewj_JL3pf3hzIjIh4hoWmeLMNMbxjtdsxpN-rJzcbQ; _video_qq_access_token=41_DK8lfY5DnnX8NQfy2p5llBomrYVj_uRuygZfoUcWLcc8Ewj_JL3pf3hzIjIh4hoWmeLMNMbxjtdsxpN-rJzcbQ; openid=oXw7q0HdfNdailul55o3xmpT5HBQ; _video_qq_openid=oXw7q0HdfNdailul55o3xmpT5HBQ; refresh_token=40_4MX8NEU3JZIrKMM_KrfLMZLIyi-TSzLkoGHwqg0tSugB9a0GEV1vsGisjOD-IdEsfL9QevrQ2mkrcUFELG730gmVdgKdKcXp8RqJ5HYFoEY; _video_qq_refresh_token=40_4MX8NEU3JZIrKMM_KrfLMZLIyi-TSzLkoGHwqg0tSugB9a0GEV1vsGisjOD-IdEsfL9QevrQ2mkrcUFELG730gmVdgKdKcXp8RqJ5HYFoEY; vuserid=81110397; _video_qq_vuserid=81110397; vusession=lhUxXI4vCK6p3skyuVED4A..; _video_qq_vusession=lhUxXI4vCK6p3skyuVED4A..; _video_qq_version=1.1; login_time_init=1612173902; next_refresh_time=6587; _video_qq_login_time_init=1612173902; _video_qq_next_refresh_time=6587; login_time_last=2021-2-1 18:5:5'
# Referer = 'https://film.qq.com/x/autovue/grade/'
Agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
headers = {
    'User-Agent': Agent,
    'Cookie': Cookie,
    'Referer': 'https://v.qq.com'
}
# 测试一个签到请求
login = requests.get(
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=Zepto1582368297765 ', headers=headers)
# 如果请求返回信息包含no login说明cookie已经失效
if login.content.decode("utf-8").__contains__("no login"):
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
    response = requests.get(url=url, headers=headers)
    responseContent = response.content.decode("utf-8")
    print(responseContent)
    resultContent += responseContent + '\n\n'

params = {'text': '腾讯视频V力值任务签到结果通知', 'desp': resultContent}
requests.post(send_url, params=params)
print('已通知到 server 酱')
