try:   
 a=int(input("请输入分数"))
except ValueError:
 print("输入无效")
else: 
 if a<0 or a>100:
    print("输入无效")
 elif a>=90:
     print("优秀")
 elif a>60:
     print("及格")
 else:
     print("不及格")           