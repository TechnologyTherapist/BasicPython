
class calculator:
    def userinput(self):
        sum = 0
        itemlist=[]
        pricelist=[]
        while(True):
               item=input("Enter a item name:")
               price = input("Enter a item price:")
               if(item!='q' or price != 'q'):
                    itemlist.append(item)
                    pricelist.append(price)
                    sum = sum+int(price)
                    print(f"your item is:{itemlist},your total bill is: {sum}")

               else:
                    
                    for i,item1 in enumerate(itemlist):
                        # for item2 in range(pricelist):
                            # print("Index Item Price")
                            # print(item2)
                            print(i+1,item1)
                    print(f"Thank you coming my shop your total bill is {sum} and your total list of your item{itemlist}")
                    break

cal = calculator()
cal.userinput()
