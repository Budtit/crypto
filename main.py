from Base64Encode import *
from Base64Decode import *


if __name__ == '__main__':
    print('*' * 50)
    print('[1]   Base64Encode')
    print('[2]   Base64Decode')
    print('*' * 50)
    get = input()
    if(get=='1'):
        print('请输出要编码字符串^.^')
        put = input()
        print(baseEncode(put))
    elif(get=='2'):
        print('请输入要解密字符串^.^')
        put = input()
        print(base64_decode(put))