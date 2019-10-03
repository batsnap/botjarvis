def chif(s):
    chifri='0123456789+-'
    itog=''
    for i in range(len(s)):
        if s[i] in chifri:
            itog+=s[i]
        if s[i]==',' or s[i]=='.':
            itog+='.'
    return itog