import rsa
# rsa 加密
def rsa_encrypt_bytes(bytes_str, n, e):
    if not isinstance(bytes_str, bytes):
        return None

    # 导入rsa库
    import rsa.common
    pubkey = rsa.PublicKey(n, e)

    key_length = rsa.common.byte_size(n)
    max_msg_length = key_length - 11

    count = len(bytes_str) // max_msg_length
    if len(bytes_str) % max_msg_length > 0:
        count = count + 1

    cry_bytes = b''

    # rsa加密要以max_msg_length分组, 每组分别加密(加密的数据长度为key_length, 解密时每key_length长度解密然后相加)
    for i in range(count):
        start = max_msg_length * i
        size = max_msg_length
        content = bytes_str[start: start + size]

        # rsa 分组 加密
        crypto = rsa.encrypt(content, pubkey)

        cry_bytes = cry_bytes + crypto

    return cry_bytes


# rsa 解密, bytes_string是rsa_encrypt_hex, rsa_encrypt_bytes的返回值
def rsa_decrypt(bytes_string, n, e, d, p, q):
    # 导入rsa库
    import rsa.common
    pri_key = rsa.PrivateKey(n, e, d, p, q)

    key_length = rsa.common.byte_size(n)
    if len(bytes_string) % key_length != 0:
        # 如果数据长度不是key_length的整数倍, 则数据是无效的
        return None

    count = len(bytes_string) // key_length
    d_cty_bytes = b''

    # 分组解密
    for i in range(count):
        start = key_length * i
        size = key_length
        content = bytes_string[start: start + size]

        # rsa 分组 解密
        d_crypto = rsa.decrypt(content, pri_key)

        d_cty_bytes = d_cty_bytes + d_crypto

    return d_cty_bytes


# rsa 加密, 注意: 这里是传递的是16进制字符串
def rsa_encrypt_hex(hex_string, n, e):
    return rsa_encrypt_bytes(bytes.fromhex(hex_string), n, e)


# rsa 库的测试
def test_encrypt_decrypt():
    import rsa

    # 产生公钥私钥
    (pub, pri) = rsa.newkeys(256)

    # 构建新的公钥私钥
    pubkey = rsa.PublicKey(pri.n, pri.e)
    pri_key = rsa.PrivateKey(pri.n, pri.e, pri.d, pri.p, pri.q)

    message = b'\x00\x00\x00\x00\x01'
    # 加密 message
    crypto = rsa.encrypt(message, pubkey)
    # 解密
    d_crypto = rsa.decrypt(crypto, pri_key)

    print(d_crypto)


if __name__ == '__main__':
    keys = rsa.newkeys(256)
    bts_str = 'hello world 中文'.encode()
    crypto_bytes = rsa_encrypt_bytes(bts_str, keys[1].n, keys[1].e)
    d_crypto_bytes = rsa_decrypt(crypto_bytes, keys[1].n, keys[1].e, keys[1].d, keys[1].p, keys[1].q)
    print(d_crypto_bytes.decode())

    hex_str = '001122334455AAff'
    crypto_bytes = rsa_encrypt_hex(hex_str, keys[1].n, keys[1].e)
    d_crypto_bytes = rsa_decrypt(crypto_bytes, keys[1].n, keys[1].e, keys[1].d, keys[1].p, keys[1].q)
    print(d_crypto_bytes.hex())