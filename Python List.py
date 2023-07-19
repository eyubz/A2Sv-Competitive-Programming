if __name__ == '__main__':
    N = int(input())
    number=[]
    for i in range(1,N+1):
        command=input()
        if command.startswith('insert'):
            a=list(command.split())
            number.insert(int(a[1]),int(a[2]))
        elif command=='print':
            print(number)
        elif command.startswith('remove'):
            a=list(command.split())
            number.remove(int(a[1]))
        elif command.startswith('append'):
            a=list(command.split())
            number.append(int(a[1]))
        elif command=='sort':
           number=sorted(number)
        elif command=='pop':
            number.pop()
        elif command=="reverse":
            number.reverse()
