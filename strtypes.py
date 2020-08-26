num1 = 200
num2 = 300
print("The value of num1 is", num1 , "and the value of num2 is", num2)




num3 = 100
num4 = 400
print("The value of num1 is {} and the value of num2 is {}".format(num3,num4))




s1 = "hello"
print(s1.upper())
print(s1.title())
print(s1.lower())



s2 = "Java, Python, Javascript"
print("Javascript" in s2)
print("Html" in s2)
print(s2.index("Python"))





s3 = "****Hello World****"
s = s3.strip("*")
print(s)
s4 = s3.lstrip("*")
print(s4)
s5 = s3.rstrip("*")
print(s5)



c = "Python"
c1 = c.center(10,"$")
print(c1)



c2 = "css, java, python, javascript"
print(c2)
c3 = c2.replace("css", "html")
print(c3)