number_builder=""
i=0
while i<=50:
    if i%2==0:
        number_builder +=str(i)+ " "

    i=i+1
print(number_builder)

number_builder=[]
i=0
while i<=50:
    if i%2==0:
        number_builder.append(str(i))

    i=i+1
print(" ".join(number_builder))