# إنشاء قاموس
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020,  # يتم تحديث القيمة إلى 2020 لأن المفاتيح يجب أن تكون فريدة
    "color": ["red", "white", "blue"]
}

# إزالة آخر عنصر في القاموس
thisdict.popitem()
print(thisdict)  # Output: {'brand': 'ford', 'model': 'mustang', 'year': 2020}

# طباعة قيمة العنصر بالمفتاح 'brand'
print(thisdict["brand"])  # Output: ford

# استخدام get() للحصول على قيمة المفتاح 'brand'
x = thisdict.get("brand")
print(x)  # Output: ford

# الحصول على قائمة بالمفاتيح والقيم
y = thisdict.keys()
z = thisdict.values()

# إضافة عنصر جديد للقاموس
thisdict["country"] = "usa"

# طباعة قائمة المفاتيح والقيم بعد التحديث
print(y)  # Output: dict_keys(['brand', 'model', 'year', 'color', 'country'])
print(z)  # Output: dict_values(['ford', 'mustang', 2020, ['red', 'white', 'blue'], 'usa'])

# طباعة طول القاموس
print(len(thisdict))  # Output: 5

# التكرار على العناصر وطباعة المفاتيح والقيم
for a, b in thisdict.items():
    print(a, b)
    # Output:
    # brand ford
    # model mustang
    # year 2020
    # color ['red', 'white', 'blue']
    # country usa

# إنشاء قاموس باستخدام dict()
mydict = dict(name="john", age=36, country="norway")

# تحديث قيمة عنصر في القاموس
mydict["name"] = "mazen"

# دمج قاموس thisdict مع mydict
mydict.update(thisdict)
print(mydict)
# Output: {'name': 'mazen', 'age': 36, 'country': 'usa', 'brand': 'ford', 'model': 'mustang', 'year': 2020, 'color': ['red', 'white', 'blue']}

# التحقق إذا كان المفتاح 'name' موجود في القاموس
if "name" in mydict:
    print("Yes")  # Output: Yes

# نسخ القاموس باستخدام copy()
mydict = thisdict.copy()
print(thisdict)  # Output: {'brand': 'ford', 'model': 'mustang', 'year': 2020, 'color': ['red', 'white', 'blue'], 'country': 'usa'}

# ملاحظات مهمة حول القواميس

# 1- الوصول إلى عنصر محدد
print(thisdict["brand"])
print(thisdict.get("brand"))

# 2- طباعة القيم في القاموس
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

# 3- تغيير قيمة عنصر محدد
thisdict["year"] = 2021

# 4- تحديث قيمة عنصر باستخدام update()
thisdict.update({"year": 2022})
thisdict.update(dict(year=2023))

# يمكن استخدام الطريقتين لإضافة عنصر جديد إذا لم يكن موجودًا

# 5- حذف عنصر بمفتاح محدد
thisdict.pop("model")
del thisdict["brand"]

# 6- حذف آخر عنصر في القاموس
thisdict.popitem()

# 7- حذف القاموس بالكامل
# del thisdict

# 8- حذف محتويات القاموس فقط
thisdict.clear()

# 9- التكرار للوصول إلى المفاتيح
for x in thisdict:
    print(x)
for x in thisdict.keys():
    print(x)

# 10- التكرار للوصول إلى القيم
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)

# 11- التكرار للوصول إلى المفاتيح والقيم
for x, y in thisdict.items():
    print(x, y)

# 12- النسخ باستخدام copy()
new_dict = thisdict.copy()

# 13- النسخ باستخدام constructor
new_dict = dict(thisdict)


#dict is orderd(3.7 python) , changable and not allow duplicate
#key in dict is write inside douple quates but in case of use constructor to make dict write as variable and use only single rounded brackts

#Access Items:
'''
1-access only one item:------->(dict_name["key_name"]) or by using get function (dict_name.get("key_name"))\
2-print data in dict 
   a- access list of keys of dict ------------->print(dict_name.keys())
   b- access list of values of dict ----------->print(dict_name.values())
   c- print list contain tuples of each pair (key , values) by using item fuction ----->print(dict_name.items())

'''

#Change Items:
'''
1-by change the value of specific item by using this syntax -------> dict_name["key_name"]=new_value
2-by adding new dict contain the same key_name and new_value this will overwrite the old value
  this done by using update function:
  EX:
      a- dict1_name.update({"key_name":value_name})
      b- dict1_name.update(dict(key_name = value_name))-------> this by using constructor

NOTE: this two ways are used also to add new key and value to dict not to change items only      
'''

#Remove Items
'''
1-delete item with specific kay name:
   a- pop():remove item by specific key name ------> dict_name.pop("key_name")
   b- del :remove item by specific key name ------> del dict_name["key_name"]

2-delete last item in dict by using popitem() --------> dict_name.popitem()  (not take arguments)
  NOTE: in version before python 3.7 popitem() remove randomly

3- delete the all dict by using del

4- delete the content of dict by using clear()
'''

#Loop Through Dictionaries
'''
1-loop to access key:
    a-  for x in dict_name:
    b-  for x in dict_name.keys():

2- loop to access values:
    a- for x in dict_name: print(dict_name[x])
    b- for x in dict_name.values:

3- print key and its value this by using items() ------> for x, y in dict_name.items(): print(x, y)    
'''


# copy dictionaries
'''
1- by using copy() -------> new_dict = dict_name_old.copy()
2- by using constactor ------> new_dict = dict(old_dict)
'''