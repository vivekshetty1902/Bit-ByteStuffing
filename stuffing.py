def split(word):
    return [char for char in word]

def ByteStuffing():
    #Sender
    x = input("Enter binary data to be sent :")
    flag = '@'
    esc = '$'
    list = split(x)
    print("The given sequence: ")
    print(list)
    i=0
    while(i<len(list)):
        if list[i]==flag or list[i]==esc:
            list.insert(i,esc)
            i+=1
        i+=1

    list.insert(0,flag)
    list.append(flag)
    print("after stuffing(sender):")
    print(list)

    #Receiver
    del list[0]
    del list[len(list)-1]

    i=0
    while(i<len(list)):
        if list[i]==esc:
            del list[i]
            i+=1
        i+=1
    i=0
    print("after unstuffing(receiver):")
    print(list)

def BitStuffing():
    #sender
    y = input("Enter binary data to be sent :")
    list1 = split(y)
    count = 0
    print(list1)
    for i in range(len(list1)):
        if list1[i] == '1':
            count = count + 1
        else:
            count = 0
        if count == 5:
            list1.insert(i + 1, '0')

    flag1=['0','1','1','1','1','1','1','0']
    for i in range(0,8):
        list1.insert(0,flag1[i])
        list1.append(flag1[i])
    print("after stuffing(sender):")
    print(list1)

    #Receiver
    for i in range(0,8):
        del list1[0]
        list1.pop()
    count = 0
    for i in range(len(list1)-1):
        if list1[i] == '1':
            count = count + 1
        else:
            count = 0
        if count == 5:
            del list1[i + 1]


    print("after unstuffing(receiver):")
    print(list1)

for i in range(0,2):
    z = int(input("enter 1 for Byte stuffing\nenter 2 for bit stuffing \n"))
    if z==1:
        ByteStuffing()
    elif z==2:
        BitStuffing()
    else:
        print("enter a valid input")

