def main():
    a = int(input())
    b = int(input())
    if a>b:
        print('Second integer can\'t be less than the first.')
    while a<=b:
        print(a, end=' ')
        a =a+5
        
main()

