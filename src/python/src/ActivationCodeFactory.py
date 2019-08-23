from rsa import common, transform, pkcs1, newkeys, PrivateKey
import base64

class ActivationCodeFactory(object):
    def __init__(self):
        self._private_key = None

    # 创建密钥文件
    def create_key_pair(self):
        (pubkey, privkey) = newkeys(2048)
        pub = pubkey.save_pkcs1()
        pubfile = open('public.pem', 'w+')
        pubfile.write(pub.decode())
        pubfile.close()

        pri = privkey.save_pkcs1()
        prifile = open('private.pem', 'w+')
        prifile.write(pri.decode())
        prifile.close()

    def _load_key_file(self, file):
        # 从.pem文件中读取key
        try:
            with open(file) as f:
                p = f.read()
                self._private_key = PrivateKey.load_pkcs1(p.encode())
        except Exception as error:
            raise error
    # 加密生成激活码
    def encrypt(self, message, file):
        self._load_key_file(file)
        keylength = common.byte_size(self._private_key.n)
        padded = pkcs1._pad_for_signing(bytes(message, encoding="utf-8"), keylength)

        payload = transform.bytes2int(padded)
        encrypted = self._private_key.blinded_encrypt(payload)
        block = transform.int2bytes(encrypted, keylength)
        return base64.urlsafe_b64encode(block).decode("utf-8")

    # 将激活码保存至文本文件中
    def save_code(self, code, file):
        with open(file, "w+") as f:
            f.write(code)


# 生成激活码运行实例
if __name__ == "__main__":
    try:
        # 创建密钥仓库
        factory = ActivationCodeFactory()
        factory.create_key_pair()

        # 生成激活码
        code = factory.encrypt("54-AA-AD-B4-26-94&2019-10-21", "private.pem")
        # 保存激活码至指定路径txt文件，
        factory.save_code(code, "ActivationCode.txt")
        print("激活码已保存")
    except:
        print("异常发生")

