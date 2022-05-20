# str_01=input("Enter the input")
# str_02= list(str_01)

# str_01=str_01[0:1].upper() + str_01[1:len(str_01)-1] +str_01[len(str_01)-1:len(str_01)].upper()
# print(str_01)

ch=input("Enter the String:")
# j=0
str=list(ch)
str+='\0'
for i in range(len(str)):
    if i==0 or str[i-1]==' ':
        str[i]=str[i].upper()
    elif str[i]==' ' or str[i]=='\0':
        str[i-1] = str[i-1].upper()

print("Your String is:", "".join(str))