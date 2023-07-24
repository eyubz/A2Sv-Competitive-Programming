import textwrap

def wrap(string, max_width):
    returnStr=""
    count=0
    for i in string:
        if count==max_width:
            returnStr+='\n'+i
            count=1
        else:
            returnStr+=i
            count+=1
    return returnStr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
