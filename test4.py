while True:
    NUM1 = float(input("첫번째 숫자를 입력해주세요"))
    NUM2 = float(input("두번째 숫자를 입력해주세요"))
    mode = input("사칙 연산을 입력해주세요.")

    if mode == "+" :
        print("%.2f+%.2f=%.2f" %(NUM1, NUM2, NUM1+NUM2))

    elif mode == "-" :
        print("%.2f-%.2f=%.2f" %(NUM1, NUM2, NUM1-NUM2))

    elif mode == "*" :
        print("%.2f-%.2f=%.2f" %(NUM1, NUM2, NUM1*NUM2))

    elif mode == "/" :
        try :
            print("%.2f-%.2f=%.2f" %(NUM1, NUM2, NUM1/NUM2))
        except ZeroDivisionError :
            print("0으로 나눌 수 없습니다.")
    else:
        print("error")

    final = input("진행, 계속(Y)/중지(N) : ")
    if final == "Y" or final == "y":
        continue
    else:
        break