import random

def ranMAC():
    return [ random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0x7f),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff)]
def print_Mac(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))

if __name__=='__main__':
    print("Random Mac Adress >> "+print_Mac(ranMAC()))

