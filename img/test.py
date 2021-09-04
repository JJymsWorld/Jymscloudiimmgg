from quickjs import Function
import time


f = open("x-bogus.js", 'r', encoding="utf-8")
xss = f.read()

testf = Function("get_x_bogus", xss)


starttime = time.time()
print(testf("device_platform=webapp&aid=6383&channel=channel_pc_web&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F92.0.4515.159+Safari%2F537.36&browser_online=true&msToken=OldETRvRFIBzMykan4SEYdTzNTCYOEW4NwQWFNZRU8o-CZOZX77VapNpAdyqkx2AJrxmVIVHhpSDDpLXqyiUGkkV6rKmWM3g3U_MKiXS6sIbxJfxsz7ERQ==","aweme_id=7003135141946215713&type=1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"))
endtime = time.time()

print(str((endtime-starttime) * 1000) + "ms")
f.close()