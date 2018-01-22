


#if condition: #必須要有:不然會錯誤
    # do something if 之後的內容要縮排
#elif other condition:
    # do something
#else:
    # do something





if __name__ =='__main__':
    score = 60
    if score >= 60:
        print('你及格')
    elif score < 60 and score >= 30:
        print('可以補考')
    else:
        print('死當')

