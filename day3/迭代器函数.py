lis = [1,2,3,4,5,6,7,8,9,10]
s = sorted(lis)#升序
b = sorted(lis, reverse=True)#降序
print(s)
print(b)

#反转
s = reversed(lis)
print(type(s))
print(list(s))

#zip打包函数
a = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
zipe = zip(a,lis)



#enumerate函数
h = enumerate(a, 2)
print(tuple(h))

#all
k = None
print(all(lis))

#next
print(next(iter(lis)))

#filter
def kj(um):
    return 1
f=filter(kj,range(10))
print(list(f))

#map
def kv(w):
    return w.upper()
ff=map(kv,a)
print(list(ff))
c=0

#属性的设置
class facc:
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender



    @property
    def gender(self):
       return self.__gender

    @gender.setter
    def gender(self,val):
        self.__gender=val
aa = facc("kk","male")
print(aa.name)
aa.gender="男"
print(aa.gender)

#多态