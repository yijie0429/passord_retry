# 密碼重設程式(自己)
x = 2
password = 'a123456'
while x <= 2 and x >= 0:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    elif x == 0:
        print('請稍後再試')
    elif pwd != ('a123456'):
        print('密碼錯誤!還有', x, '次機會')
    x = x - 1

# 密碼重設程式(老師)
i = 3
password = 'a123456'
while i > 0:
    i = i - 1
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        print('密碼錯誤!')
        if i > 0:
            print('還有', i, '次機會')
        else:
            print('沒機會嘗試了，要鎖帳號了!')
        