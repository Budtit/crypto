

def baseEncode(string):
    ordstr = ''
    sixstr = []
    base = ''
    base64_str = []
    # 构造base64字符表
    for i in range(65, 91):
        base64_str.append(chr(i))
    for i in range(97, 123):
        base64_str.append(chr(i))
    for i in range(48,58):
        base64_str.append(chr(i))
    base64_str.append('+')
    base64_str.append('/')
    for i in string:
        ordstr += '{:08}'.format(int(str(bin(ord(i))).replace('b', '')))
    for i in range(0, len(ordstr),6):
        sixstr.append('{:<06}'.format(ordstr[i:i+6]))
    for i in range(0, len(sixstr)):
        base += base64_str[int(sixstr[i], 2)]

    if(len(ordstr) % 3 == 1):
        base += '=='
    elif(len(ordstr) % 3 == 2):
        base += '='
    return base


