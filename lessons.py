def main():
    a=open('lessons.txt','r')
    s=[]
    for line in a:
        s.append(line)
    return s


def Monday():
    a=main()
    s=a[1]+a[2]+a[3]+a[4]
    return s

def Tuesday():
    a=main()
    s=a[6]+a[7]+a[8]+a[9]
    return s

def Wendsday():
    a=main()
    s=a[11]+a[12]+a[13]
    return s

def Tursday():
    a=main()
    s=a[15]+a[16]
    return s

def Friday():
    a=main()
    s=a[18]+a[19]+a[20]+a[21]
    return s

def Saturday():
    a=main()
    s=a[23]+a[24]
    return s