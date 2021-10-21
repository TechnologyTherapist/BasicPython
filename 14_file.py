#Read file 

# def read():
#     r=open("sample.txt",'r')#by default read
#     # data=f.read()
#     data=r.readline()
#     print(data)
#     data=r.readline()
#     print(data)
#     r.close()
# read()

#Write Mode append mose also used
# def write():
#   u=input("Enter a data:")
#   w=open("sample.txt",'a')
#   w.write(u)
#   w.close()
# write()

# with statement
# def with1():
#     with open("sample.txt",'r') as r:
#      data=r.read()
#      print(data)
# with1()


#problem set
# def read():
#      with open("sample.txt",'r') as r:
#       data=r.read()
#      if 'twinkle' in data:
#       print("this is present in your data")
#      else:
#       print("This word is not present your data")
     
# read()


# def game():
#     u=int(input("Enter a high new score:"))
#     return u

# score=game()
# r=open("score.txt",'r')
# high=(r.read())
# if high=='':
#     with open("score.txt",'w') as w:
#         w.write(str(score))
# elif int(high)<score:
#     with open("score.txt",'w') as w:
#         w.write(str(score))
 
# for i in range(2,21):
#    with open(f"tables{i}.txt",'w') as f:
#        for j in range(1,11):
#            f.write(f"{i}*{j}={i*j}")
#            if j!=10:
#                  f.write('\n')
           
# words=["Twinkle",'dark','twinkle']
# with open("sample.txt",'r') as r:
#     cont=r.read()
    
# for word in words:
#     cont=cont.replace(word,"donkey")
#     with open("simple.txt",'w') as w:
#         w.write(cont)
# 
# 
# 
# 
# content=True
# i=1
# with open("log.txt",'r') as r:
#     while content:
#         content=r.readline()
#         if 'python' in content:
#             print(content)
#             print("yes its present a data")
#             print(i)
#         i+=1


# import os
# oldfile="sample.txt"
# newfile="python.txt"
# with open(oldfile) as o:
#     content=o.read()
# with open(newfile,'w') as n:
#     n.write(content)
#     os.remove(oldfile)