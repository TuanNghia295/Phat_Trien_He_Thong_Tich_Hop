a = 2
if(a > 2):
    print (True)

elif(a < 2):
    print ("Hello")
else:
    print("Dung roi")

arrays = [1,2,3,4]

for index in arrays:
    print("so thu" ,index)

soLon = 10
soBe = 3
while soBe < soLon:
    soBe = soBe + 1
    
print (soBe)


# Functions
def Sum(a, b):
    return a + b

result = Sum(1, 2)
print(result)

def ageofFiveYearsAgo(a,b =5):
    return a -b
age =   ageofFiveYearsAgo(15)
print(age) 


# String Processing (xử lý chuỗi)
firstName = "Nguyen Tuan "
lastName = "Nghia"
print(firstName + lastName) 
print(firstName[0]) 
# Tạo chuỗi con thông qua toán tử lấy khoản [start:end] 
# create a child String by interval operator
print(lastName[0:2]) 
# Độ dài chuỗi 
print(len(firstName))



