var4=(15,78,57,15,22,15,35,95,74)
var5=[15,78,57,15,22,15,35,95,74]
var6={15,78,57,15,22,15,35,95,74}

print(var4)
print(var5)
print(var6)

#tuple
print(var4.count(15))
print(var4.index(57))


#set

var6.add(76)
print(var6)
var6.pop()
print(var6)
var6.remove(78)
print(var6)
var6.clear()
print(var6)


#list
var5.append(78)
print(var5)
var5.insert(2,98)
print(var5)
print(var5.index(98))
print(var5.count(15))
var5.pop()
print(var5)
var5.remove(98)
print(var5)
var5.reverse()
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5)


#boolean
var7=True
print(var7)


#dictionary

var8={
    'name':"harsika",
    'company':"hhh",
    'mobile':"1234567890",
    'email':"h@gmail.com",

}

print(var8.get('name'))
print(var8.items())
print(var8.keys())
print(var8.values())
var8['city']="madurai"
print(var8)