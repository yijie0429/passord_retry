# 密碼重設程式(自己)
x = 2
while x <= 2 and x >= 0:
    password = input('請輸入密碼: ')
    if password == 'a123456':
        print('登入成功')
        break
    elif x == 0:
        print('請稍後再試')
    elif password != ('a123456'):
        print('密碼錯誤!還有', x, '次機會')
    x = x - 1

# 密碼重設程式(老師)
i = 3
password = 'a123456'
while i > 0:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        i = i - 1
        print('密碼錯誤! 還有', i, '次機會')
        