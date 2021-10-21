
with open("data.txt") as f:
    data=f.readlines()
    # print(a)
# for item in enumerate(data):
#     print(item)
currencydict={}
for cun in data:
    data2=cun.split('\t')
    currencydict[data2[0]]=data2[1]
# print(currencydict)
    # break
amount=int(input("Enter a amount:\n"))
print("Enter the name of currency and this avialable currency in dictionary:\n")
[print(item)  for item in currencydict.keys()]
currency=input("Enter a currency:\n")
print(f"{amount} INR is equal to {amount*float(currencydict[currency])} {currency}")
# print(currencydict[currency])