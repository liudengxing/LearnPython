str1 = "test"
str2 = "test"

print(str1 == str2)
print(str1 is str2)


str3 = "testA"
str4 = str1 + 'A'

print(str3 == str4)
print(str3 is str4)

str5 = str("test")
str6 = str("test")
print(str6 == str5)
print(str6 is str5)

str7 = str("test" * 10000)
str8 = str("test" * 10000)
print(str7 == str8)
print(str7 is str8)
