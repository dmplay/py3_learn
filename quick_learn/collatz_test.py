def collatz(number):
    if number%2==0:
        number=number//2
    else:
        number=number*3+1
    print(number)
    return number

if __name__=="__main__":
    while(True):
        try:
            number = collatz(int(input("输入一个数字:")))
            break
        except ValueError:
            print('Error: 请输入正整数.')

    while(number!=1):
        number = collatz(number)