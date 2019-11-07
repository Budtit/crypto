from Base64Encode import build_base64_str

base64_str = build_base64_str()


def base64_decode(string):
    ordstr = ""
    newstr = []
    destr = ""
    # 去掉等号，转换为二进制，六个一组
    for i in string.replace('=',''):
        ordstr += '{:06}'.format(int(str(bin(base64_str.index(i)).replace('0b', ''))))
    for i in range(0, len(ordstr), 8):
        newstr.append(ordstr[i:i+8])
    for i in range(0,len(newstr)):
        destr +=  chr(int(newstr[i], 2))
    return destr











if __name__ == '__main__':
    base64_decode("YWJjZA=")