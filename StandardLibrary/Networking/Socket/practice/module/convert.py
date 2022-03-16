def StrToByte(x: str = None):
    return x.encode('utf_8')

def ByteToStr(x: bytes = None):
    return x.decode('utf_8')
