import aiohttp
import asyncio
from datetime import datetime
import base64
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


async def fetch(url,client):

    print(client)
    async with client.get(url) as resp:
        print(resp.status)
        # print(aesDecrypt(print(aesDecrypt('AZy*$8Fto6ImXMuN',await resp.text()))))
        return resp.text()

urls=['http://39.99.205.9:50100/item/P00001-01-978-7-121-10736-8-Epub.txt','http://39.99.205.9:50100/item/P00001-01-978-7-121-32805-3-Epub.txt']
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
async def main():
    async with aiohttp.ClientSession() as client:
       tasks = []
       # for url in range(6):
       for url in urls:
           tasks.append(asyncio.ensure_future(fetch(url,client)))
       await asyncio.wait(tasks)

loop = asyncio.get_event_loop()

start = datetime.now()

# loop.run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
end = datetime.now()
print("aiohttp版爬虫花费时间为：")
print(end - start)