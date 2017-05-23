def collatz(number):
    if number%2==0:
        number=number//2
    else:
        number=number*3+1
    print(number)
    return number

if __name__=="__main__":
    flag=1
    while(flag==1):
        try:
            number = collatz(int(input("输入一个数字:")))
            flag=2
        except ValueError:
            print('Error: Invalid argument.')

    while(number!=1):
        number = collatz(number)