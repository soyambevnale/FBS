###  1) Numeric

#1 int
var=10
print(type(var))

#2 float
var=3.14
print(type(var))

#3 complex
var=10+3j
print(type(var))

###  2) Text

#1 str
var='Firstbit Solutions'
print(type(var))
var='Firstbit "Solutions" '
print(type(var))
var="Firstbit Solutions"
print(type(var))
var="Firstbit's Solutions"
print(type(var))
var="""Firstbit's Solutions
Hello World"""
print(type(var))
var='''Firstbit's Solutions
Hello World'''
print(type(var))

### 3) Sequential

#1 list
var=[10,20,30]
print(type(var))

#2 tuple
var=(10,20,30)
print(type(var))

#3 range
var=range(1,11)
print(type(var))

### 4) Set Type

#1 set
var={10,20,30}
print(type(var))

#2 frozenset
var=frozenset({10,20,30})
print(type(var))

### 5) Mapping

#1 dict
var={'id':101,'name':'xyz'}
print(type(var))

### 6) Others

#1 Boolean
var=True
print(type(var))

#2 NoneType
var=None
print(type(var))

