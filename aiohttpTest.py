import asyncio,aiohttp
import base64
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

async def fetch_async(url,client):
    print(url)
    # async with aiohttp.ClientSession() as session: #协程嵌套，只需要处理最外层协程即可fetch_async
    async with client.get(url) as resp:
        print(resp.status)
        print(aesDecrypt('AZy*$8Fto6ImXMuN',await resp.text())) #因为这里使用到了await关键字，实现异步，所有他上面的函数体需要声明为异步async

def aesDecrypt(key, data):
    '''
    :param key: 密钥
    :param data: 加密后的数据（密文）
    :return:明文
    '''
    key = key.encode('utf8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)

    # 去补位
    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    return text_decrypted
urls=['http://39.99.205.9:50100/item/P00001-01-978-7-121-10736-8-Epub.txt','http://39.99.205.9:50100/item/P00001-01-978-7-121-32805-3-Epub.txt']
# tasks = [fetch_async('http://39.99.205.9:50100/item/P00001-01-978-7-121-10736-8-Epub.txt'), fetch_async('http://39.99.205.9:50100/item/P00001-01-978-7-121-32805-3-Epub.txt')]
tasks = []
async def main():
    async with aiohttp.ClientSession() as client:
       tasks = []
       # for url in range(6):
       for url in urls:
           tasks.append(fetch_async(url,client))
       await asyncio.wait(tasks)
event_loop = asyncio.get_event_loop()
# results = event_loop.run_until_complete(asyncio.gather(*tasks))
results = event_loop.run_until_complete(main())
event_loop.close()

