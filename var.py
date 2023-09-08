"""my_var = 10
print(my_var)

my_list = 1, 2, 3
print(my_list)
print(*my_list)

my_list = [1, 2, 3]
print(my_list)
print(*my_list)

print("구슬이 서 말이라도 꿰어야 보배")

#정수
my_int = 10
print(my_int)

#부동 소수점
my_float = 3.14
print(my_float)

#복소수
my_complex = 3 + 4j
print(my_complex)

#문자
my_character = 'A'
print(my_character)

my_char = "@"
print(my_char)

#문자열
my_string = 'Hello, World!'
print(my_string)

str_name = "python"
print(str_name)

#불리언
my_bool = True
print(my_bool)

bFlag = False
print(bFlag)

#리스트
my_list = [1, 2, 'three', True]
print(my_list)
print(*my_list)

lsElement = [3.14, "b", 'two',False]
print(lsElement)
print(*lsElement)

#리스트 활용
my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)
print(*my_list)

print(my_list.__len__()) #값 6

print(my_list[3]) #3번째 순서인 9가 뜸
print(my_list[5])

list_el = my_list[2]
print(list_el) 

my_list[3] = 11 #3번째 순서인 9를 11로 바꿈
print(my_list)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)

n_add = my_list[3] + my_list[2]
print(n_add)

print(my_list[2:5])
print(my_list[:3])
print(my_list[0:3])
print(my_list[4:])

my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "World"]]
print(my_list)
print(my_list[6][1])#6번 째의 첫번째를 가져와라
print(my_list[6][2:])
print(my_list[5][2])

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)

my_list.insert(2, 4)
my_list.insert(3, "e")
print(*my_list)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list.index(3))
#print(my_list.index(4)) 4가 없기 때문에 안 뜸

my_list.append(22) #22 추가
print(*my_list)

my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list.count(8)) #8의 갯수 1
print(my_list.count(5)) #5의 갯수 0
print(my_list.count("hello"))

print(my_list)
print(my_list.pop()) #마지막 요소 삭제
print(*my_list)

my_list = [10, 3, 8, 9, 42, 8]
print(my_list)

my_list.sort()  #오름차순 정렬
print(*my_list)

my_list.reverse() #역순으로 정렬
print(*my_list)

# 두 리스트 결합하기
my_list = [10, 3, 8, 9, 42, "hello"]
list_tmp = [5, 7, "world"]
print(my_list, list_tmp)

my_list.extend(list_tmp)
print(*my_list)

# 리스트 내, value 전체 삭제
list_tmp.clear()
print(list_tmp)

# 해당 value 삭제
my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)
my_list.remove(3)
print(*my_list)

# 해당 인덱스 삭제
my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)
del my_list[2]
print(*my_list)
"""

""" 
#튜플 활용 (변경이 안되지만 참조는 가능)
my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(*my_tup)
print(my_tup.__len__())

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(my_tup[2])
print(*my_tup)

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(my_tup[2])
#my_tup[3] = 2 #튜플은 변경이 불가능하기 때문에 오류 발생
print(*my_tup)

my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)

print(my_tup[2] + my_tup[0]) #연사자는 지원됨
print(*my_tup)

n_add = my_tup[1] + my_tup[3]
print(n_add)

print(my_tup[2:5])
print(my_tup[1:4])
print(my_tup[:3])
print(my_tup[2:])

# 이중 튜플
my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
print(my_tup[6][0]) #h 출력

#인덱스 순서
my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup.index(2, 0, 3)) 
print(my_tup.index("py", 3, 5)) 
#print(my_tup.index(1, 0, 3))

print(my_tup.count(6)) #갯수세기
"""

#딕셔너리 활용
"""""
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_item = my_dict.items()
print(my_item)

idx = ("key1", "key2", "key3")
dicts = dict.fromkeys(idx, "0")
print(dicts)
"""""
"""""
my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}
print(my_dict["key1"])

my_str = my_dict.get("key2")
print(my_str)

print(my_dict.pop("key1"))
print(my_dict)
"""""
"""""
my_dict = {'key1': 'value1', 'key2': 'value2'}
dicts = my_dict.copy()
print(dicts)
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}
my_dict["key3"] = "value3"
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}
my_dict.setdefault("key3")
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.update({"key1" : "v4"})
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
del my_dict["key2"]
print(my_dict)
"""""

my_dict = {'key1': 'value1', 'key2': 'value2'}
print("key2" in my_dict)
print("key3" in my_dict)

my_list = list(my_dict.keys())
print(my_list)

my_list = list(my_dict.values())
print(my_list)

my_set = set(my_dict.keys())
print(my_set)

my_dict.clear()
print(my_dict)

