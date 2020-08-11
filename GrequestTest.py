import json

import grequests
import time
import requests
import rsa
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
import binascii
urls = [
    'http://39.99.205.9:50100/resource/php/item/downLoadUrl?skuExternalId=P00001-01-978-7-121-32708-7-Epub',
    # 'https://docs.python.org/2.7/library/dl.html',
    # 'http://www.iciba.com/partial',
    # 'http://2489843.blog.51cto.com/2479843/1407808',
    # 'http://blog.csdn.net/woshiaotian/article/details/61027814',
    # 'https://docs.python.org/2.7/library/unix.html',
    # 'http://2489843.blog.51cto.com/2479843/1386820',
    # 'http://www.bazhuayuddd.com/tutorial/extract_loop_url.aspx?t=0',
]


def method1():
    t1 = time.time()
    for url in urls:
        res = requests.get(url)
    t2 = time.time()
    print('method1', t2 - t1)


def method2():
    tasks = [grequests.get(u) for u in urls]
    t1 = time.time()
    res = grequests.map(tasks, size=3)
    print(res)
    t2 = time.time()
    print('method2', t2 - t1)


def exception_handler(request, exception):
    print(request, exception)


# {"Success":true,"Code":200,"Description":"","Data":{"ExternalAddress":"http:\/\/39.99.205.9:50100\/item\/P00001-01-978-7-121-32708-7-Epub.txt","InternalAddress":"http:\/\/172.26.121.245:50100\/item\/P00001-01-978-7-121-32708-7-Epub.txt"}}
def method3():
    tasks = [grequests.get(u) for u in urls]
    t1 = time.time()
    res = grequests.map(tasks, size=1, exception_handler=exception_handler, gtimeout=2000)
    dic = res[0].text
    text = json.loads(dic)
    url = text['Data']['ExternalAddress']
    tasks1 = [grequests.get(url)]
    res = grequests.map(tasks1, size=1, exception_handler=exception_handler, gtimeout=2000)
    text = res[0].text
    rsa_decrypt(text,"AZy*$8Fto6ImXMuN")
    t2 = time.time()
    print('method3', t2 - t1)


def rsa_decrypt(crypto, privkey):
    # 解密
    content = rsa.decrypt(crypto, privkey)
    # 解码
    content = content.decode('utf-8')
    print('解密结果', content)

def decrypt(private_key, hex_data):
    '''解密方法'''
    try:
        private_key = RSA.import_key(private_key)
        cipher_rsa = PKCS1_v1_5.new(private_key)

        en_data = binascii.unhexlify(hex_data.encode('utf-8'))
        data = cipher_rsa.decrypt(en_data, None).decode('utf-8')

        return {'state': "success", 'message': data}
    except Exception as err:
        return {'state': "fail", 'message': str(err)}


if __name__ == '__main__':
    # method1()
    # method2()
    method3()
