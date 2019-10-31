from Base64Encode import *

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
