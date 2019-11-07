
def build_base64_str():
    base64_str = []
    # 构造base64字符表
    for i in range(65, 91):
        base64_str.append(chr(i))
    for i in range(97, 123):
        base64_str.append(chr(i))
    for i in range(48, 58):
        base64_str.append(chr(i))
    base64_str.append('+')
    base64_str.append('/')
    return base64_str
base64_str = build_base64_str()


def baseEncode(string):
    ordstr = ''
    newstr = []
    en_str = ''
    # 转换为二进制去掉b八位一组，不足的前面补齐0
    for i in string:
        ordstr += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))
    for i in range(0, len(ordstr),6):
        newstr.append('{:<06}'.format(ordstr[i:i+6]))
    for i in range(0, len(newstr)):
        en_str += base64_str[int(newstr[i], 2)]
    if(len(ordstr) % 3 == 1):
        en_str += '=='
    elif(len(ordstr) % 3 == 2):
        en_str += '='
    return en_str


