# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです。
"""

# %%
print('Hello')

# %%
a = 10
b = 14
print(a+b)

# %%
print('こんにちは。', end='')
print('はじめまして。')

#%%
print('風')
print('林')
print('火')
print('山')

#%%
print('こんにちは。')
print()
print('はじめまして。')

# %%
number = input('学籍番号を入力してください。:')
name = input('氏名を入力してください。:')
print(number, name, sep=':')
number_name = number + ':' + name
print(number_name)

# %%
height = int(input('身長[cm]を入力してください。:'))
weight = int(input('体重[kg]を入力してください。:'))
print(f"{weight / ((height /100) ** 2): .2f}")

# %%
PI = 3.14159
r = int(input('半径:'))
print(f'球の体積:{(4*r**3*PI)/3:.3f}')

# %%
time = int(input('整数を入力してください。:'))
print(f'{time}秒 = {time//3600}時間{(time%3600)//60:2}分{(time%3600)%60:2}秒')

# %%
real = float(input('実数を入力してください。:'))
if real > 0:
    print('正の実数です。')
elif real < 0:
    print('負の実数です。')
else:
    pass

# %%
blood = input('血液型を入力：')
if blood == 'A':
    print('A型の割合は40%です')
elif blood == 'O':
    print('O型の割合は30%です')
elif blood == 'B':
    print('B型ぼ割合は20%です')
elif blood == 'AB':
    print('AB型の割合は10%です')
else :
    print('不正な入力です')
    
# %%
blood = input('血液型を入力：')
match blood:
    case 'A':
        print('A型の割合は40%です')
    case 'O':
        print('O型の割合は30%です')
    case 'B':
        print('B型の割合は20%です')
    case 'AB':
        print('AB型の割合は10%です')
    case _:
        print('不正な入力です')

# %%
n = int(input('整数を入力:'))
if n <= 0:
    print("エラー")
for i in range(1, n+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(f'{i}')
        
# %%
for i in range(1, 1001):
    if i % 5 != 0:
        continue
    print(i);
    
# %%
s=0
a=0
b=0
c=0
d=0
total=0
for i in range(1, 11):
    n = int(input(f'{i}人目の得点を入力:'))
    if n<0 or n>100:
        print('エラー')
        break
    total += n
    if n >= 90:
        s += 1
    elif n >= 80 and n < 90:
        a += 1
    elif n >= 70 and n < 80:
        b += 1
    elif n >= 60 and n < 70:
        c += 1
    else:
        d += 1
else:
    print(f'Sの人数:{s}')
    print(f'aの人数:{a}')
    print(f'bの人数:{b}')
    print(f'cの人数:{c}')
    print(f'dの人数:{d}')
    
    average = total / 10
    print(f'{average:.2f}')

# %%
n = int(input('整数を入力:'))
if n < 0:
    print('エラー')
else:
    a = 1
    for i in range(1, n+1):
        a *= i
    print(f'{n}の階乗は{a}')    
    
# %%
str1 = input('文字列を入力:')
str2 = input('文字列を入力:')
if str1 == str2:
    print(str1, str2)
else:
    str3 = str1 + str2
    print(str3)        
        
# %%
str1 = input('文字列を入力:')
if len(str1) <= 10:
    print(str1)
else:
    print(str1[10:])
    
# %%
str1 = input('文字列を入力:')
for char in reversed(str1):
    print(char)
    
# %%
str1 = input('文字列を入力:')
for char in reversed(str1):
    print(char)
    
# %%
str1 = input('文字列を入力:')
str2 = ''.join('o'if i % 2 == 1 else ch for i, ch in enumerate(str1))
print(str2)

# %%
str1 = input('文字列を入力:')
str2 = input('文字列を入力:')
s1 = str1.capitalize()
s2 = str2.capitalize()
s = s1 + '-' + s2
print(s)
print(s.upper())
print(s.replace('A', 'X'))

# %%
lst = [3,5,1,6,8]
total = sum(lst)
ave = total/len(lst)
print('合計:',total)
print('平均値:',ave)

# %%
fruit1 = ['パイナップル','オレンジ','リンゴ','サクランボ','パパイア','ブルーベリー']
fruit2 = fruit1 + ['グループフルーツ','桃']
n = input('果物の名前を入力:')
if n in fruit2:
    print('〇')
else:
    print('×')
long_fruit = [fruit for fruit in fruit2 if len(fruit) >= 4]
print('4文字以上の果物:',long_fruit)

# %%
lst = []
for i in range(5):
    n = float(input(f'{i+1}個目の正の実数を入力:'))
    if n < 0:
        print('エラー')
        break
    lst.append(n)
else: 
    print('最大値:',max(lst))
    print('最小値',min(lst))
    print('合計:',sum(lst))
    
# %%
while True:
    x = int(input('正の整数を入力:'))
    if x <= 0:
        print('正の整数ではない')
    else:
        break
history = [x]
while x != 1:
    if x % 2 == 0:
        x //= 2
    else:
        x = x * 3 + 1
    history.append(x)
print(history)

# %%
list1 = [x for x in range(1,101) if x % 3 == 0 and x % 5 == 0]
list2 = [x**2 for x in list1]
list3 = list(zip(list1,list2))
print(list3)
for a, b in list3:
    print(f'{a}の二乗は{b}です')
    
# %%
n = input('二進数を入力:')
a = 0
for index, bit in enumerate(reversed(n)):
    if bit not in ('0', '1'):
        print('エラー')
        break
    a += int(bit) * (2 ** index)
else:
    print(f'十真数の変換結果:{a}')

# %%
while True:
    try:
        x = int(input('正の整数を入力:'))
        if x <= 0:
            print('エラー')
            continue
        break
    except ValueError:
        print('エラー')
nlist = []
while x > 0:
    nlist.append(str(x % 2))
    x //= 2
result = ''.join(reversed(nlist))
print(f'二進数の変換結果:{result}')

# %%
rgb = {'red': '赤', 'green': '緑'}
for x in rgb:
    print(x)
    
# %%
s = {'前橋', '高崎', '伊勢崎'}
print('高崎' not in s)

# %%
def func(x):
    for i, v in enumerate(x):
        if i % 2 == 0:
            x[i] = 0
        return
x = [5, 10, 3, 19, 14]
func(x)
print(x)

# %%
kansai = {'大阪':'大阪', '京都':'京都', '兵庫':'神戸', '奈良':'奈良'}
print(f"兵庫県の県庁所在地は{kansai['兵庫']}市です")
print(f"京都府の県庁所在地は{kansai['京都']}市です")
kansai |= {'滋賀':'大津'}
print(kansai)
kansai |= {'和歌山':'和歌山'}
print(kansai)
kansai.pop('大阪')
print(kansai)
print(len(kansai))

# %%
kanto = {'東京':'東京', '埼玉':'さいたま', '千葉':'千葉', '神奈川':'横浜', '茨城':'水戸', '栃木':'宇都宮', '群馬':'高崎'}
kanto['群馬'] = '前橋'
tupule = ('東京', '埼玉', '千葉', '神奈川', '茨城', '栃木', '群馬')
list = ['東京', 'さいたま', '千葉', '横浜', '水戸', '宇都宮', '前橋']
for key, value in kanto.items():
    print(key, value)
kanto.clear()
print(kanto)

# %%
s = {1, 5, 3, 9}
s.add(8)
s.add(5)
print(s)
s2 = {4, 5, 3, 2, 9}
print(s | s2)
print(s & s2)
if 1 in s:
    print("1は含まれている")
else:
    print("1は含まれていない")
list_n = sorted(s, reverse=True)
print(list_n)

# %%
def func(n):
    return [num for num in n if num % 2 == 0]
list_n = {10, 25, 7, 32, 14, 5, 3, 50, 6, 8}
list2 = func(list_n)
print(list2)

# %%
def func(a, b, c, x):
    return a * x * x + b * x + c
def sign(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
a = int(input('aの値を入力:'))
b = int(input('bの値を入力:'))
c = int(input('cの値を入力:'))
x = int(input('xの値を入力:'))
n = func(a, b, c, x)
if n >= 0:
    print(f'{n:.3f}')
else:
    print(f'{abs(n):.3f}')

# %%
x=1
y=2
print(x, y, end=':')

# %%
def func(n):
    z=1
    for _ in range(n):
        z *= -n
    return True if z > 0 else False
x=[1, 2, 3, 4]
y=filter(func, x)
print(f'y={list(y)}')

# %%
def evaluate(x):
    if x[1] < 0 or x[1] > 100:
        return (x[0], '-')
    elif x[1] >= 90:
        return (x[0], 'S')
    elif 80 <= x[1] < 90:
        return (x[0], 'A')
    elif 70 <= x[1] < 80:
        return (x[0], 'B')
    elif 60 <= x[1] < 70:
        return (x[0], 'C')
    else:
        return (x[0], 'D')
x = [('前橋', 87), ('高崎', 92), ('群馬', 125)]
print(list(map(evaluate, x)))

# %%
def funct(x, y=60):
    return x*y
n = int(input('整数を入力:'))
if n < 30:
    print(f'{funct(n, 50)}')
else:
    print(f'{funct(n)}')
    
# %%
def dis(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
x = [5, 2, -3, 0, 10, -1, 0, -6, 8, 5]
y = map(dis, x)
print(f'{list(y)}')

# %%
def funct(n):
    if n >= 10:
        return str(n)
    else:
        return '-'
numbers = []
while True:
    v = int(input('整数を入力:'))
    if v < 0:
        break
    numbers.append(v)
mapped_list = list(map(funct, numbers))
filtered_list = list(filter(lambda x:x >= 10, numbers))
print(mapped_list)
print(filtered_list)

# %%
def dis_pos(x):
    return x > 0
def fun(x):
    return bin(n)[2:]
n = []
print('10個の整数を入力:')
for _ in range(10):
    num = int(input(f'{_+1}個目:'))
    n.append(n)
pos_num = filter(dis_pos, n)
fun_num = list(map(fun,pos_num))
print(fun_num)

# %%
class Triangle:
    def __init__(self,base,height):
        '''
        コンストラクタ：底辺と高さを受け取り、インスタンス変数を初期化
        :param base:三角形の底辺
        :param height:三角形の高さ
        '''
        self.base = base
        self.height = height
    
    def calculate_area(self):
        '''
        三角形の面積を計算し、小数点第二位までを返す
        '''
        area = (self.base * self.height) / 2
        return round(area,2)
triangle1 = Triangle(10,5)
triangle2 = Triangle(7,3)
triangle3 = Triangle(6,5)
print(f'三角形１の面積:{triangle1.calculate_area()}')
print(f'三角形2の面積:{triangle2.calculate_area()}')
print(f'三角形3の面積:{triangle3.calculate_area()}')
# %%
import math
class QuadraticEquation:
    def __init__(self,a,b,c):
        '''
        コンストラクタ:二次方程式の係数を受け取り、インスタンス変数を初期化
        :param a:二次の係数
        :param b:一次の係数
        :param c:定数項
        '''
        self.a = a
        self.b = b
        self.c = c
        
    def solve(self):
        '''
        二次方程式の解を求め、リストで返す
        :return:二次方程式の解のリスト
        '''
        discriminant = self.b**2-4*self.a*self.c
        if discriminant < 0:
            return [None,None]
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-self.b - sqrt_discriminant) / (2*self.a)
        root2 = (-self.b - root1*(2*self.a)) / self.a
        return [round(root1,2),round(root2,2)]
eq1 = QuadraticEquation(1,-3,2)
eq2 = QuadraticEquation(1,-2,-3)
print(f'二次方程式１の解:{eq1.solve()}')
print(f'二次方程式2の解:{eq2.solve()}')
# %%
import math
angles = [x for x in range(0, 361, 10)]

class TrigonometricValues:
    def __init__(self,angle):
        '''
        コンストラクタ:角度をラジアンに変換し、インスタンス変数に格納
        '''
        self.angle = angle
        self.radians = math.radians(angle)
        
    def calculate(self):
        '''
        sin,cos,tanの値を計算し、リストで返す
        小数点第八位までを求める
        '''
        sin_x = round(math.sin(self.radians),8)
        cos_x = round(math.cos(self.radians),8)
        tan_x = round(math.tan(self.radians),8)if not math.isclose(cos_x,0,abs_tol = 1e-8) else None
        return [sin_x, cos_x, tan_x]
    
for angle in angles:
    trig_values = TrigonometricValues(angle)
    values = trig_values.calculate()
    print(f'{angle:3d}°:[{values[0]},{values[1]},{values[2]}]')
# %%
import math 
import random

class Circle:
    def __init__(self,radius):
        '''
        コンストラクタ:半径を受け取り、インスタンス変数を初期化
        面積を計算し、保存
        '''
        self.radius = radius
        self.area = self.calculate_area()
        
    def calculate_area(self):
        '''
        円の面積を計算し、返す
        小数点第三位まで求める
        '''
        return round(math.pi * (self.radius ** 2),3)
    
    def display_area(self):
        '''
        面の面積を表示
        '''
        print(f'{self.area}')
        
radi_list = [random.uniform(0,100) for _ in range(100)]
circles = [Circle(radius for radius in radi_list)]
for circle in circles:
    if circle.area >= 5000:
        circle.display_area()
    else:
        print('---')
# %%
class Student:

    def __init__ (self, affiliation: str, no: str, name: str, mathematics: int, phyics: int, chemistry: int):
        self.affiliation  = affiliation
        self.no = no
        self.name = name
        self.mathematics = mathematics
        self.phyics = phyics
        self.chemistry = chemistry

    def to_csv(self):
        '''
        コンマ区切りの文字列を生成するメソッド
        '''
        return f'(self.affiliation), (self.no), (self.name), (self.mathematics), (self.phyics), (self.chemistry)'

student_list = []
student_list.append(Student('情報システムプログラム', 'mib22001','前橋太郎',68,72,59)) 
student_list.append(Student('情報システムプログラム', 'mib22002','高崎次郎',88,65,73))
student_list.append(Student('情報システムプログラム', 'mib22003','太田三郎',53,62,60))
student_list.append(Student('情報システムプログラム', 'mib22004','桐生四郎',90,86,88))
student_list.append(Student('情報システムプログラム', 'mib22005','沼田五郎',78,80,66))
file_name = input('ファイル名を入力してください')

if not file_name.endswith('.csv'):
    file_name += '.csv'

with open(file_name, mode="w", encoding="utf-8") as file:
    for student in student_list:
        file.write(student.to_csv() + '\n')

print (f'データが(file_name]に保存されました。')
# %%
class Student:
    def _init__(self, affiliation, student_id, name, math_score, physics_score, chemistry_score):
        self.affiliation = affiliation
        self.no = no
        self.name = name
        self.mathematics = mathematics
        self.physics = physics
        self.chemistry = chemistry

    def to_csv(self):
        '''
        コンマ区切りの文字列を生成するメソッド
        '''
        return f'{self.affiliation},{self.no},{self.name},{self.mathematics},{self.physics},{self.chemistry}'

#引数として受け取った文字列を整数に変換する関数
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return value

#student_list.append(Student('情報システムプログラム', 'mib22001','前橋太郎',68,72,59)) 
#student_list.append(Student('情報システムプログラム', 'mib22002','高崎次郎',88,65,73))
#student_list.append(Student('情報システムプログラム', 'mib22003','太田三郎',53,62,60))
#student_list.append(Student('情報システムプログラム', 'mib22004','桐生四郎',90,86,88))
#student_list.append(Student('情報システムプログラム', 'mib22005','沼田五郎',78,80,66))

file_name = input('読み込むファイル名を入力してください:')

students = []

with open(file_name, mode = 'r', encoding = 'utf-8') as file:
    while True:
        line = file.readline() #1行を読み込む
        if not line: #読み込むデータがなくなったら終了
            break
        line = line.replace('\n', '') #改行文字を除去
        data = line.split(',') #コンマで分割してリストに変換
        
# %%
class Car:
    def __init__(self, manufacturer, model, price, discount_rate): 
        self.__manufacturer = manufacturer 
        self.__model = model 
        self.__price = price 
        self.__discount_rate = discount_rate
        
    def __calculate_sale_price(self):
        sale_price = self.__price * (1 - self.__discount_rate / 100) 
        return round(sale_price, 2) 
    def display_info(self): 
        sale_price = self.__calculate_sale_price() 
        print(f"Manufacturer: {self.__manufacturer}") 
        print(f"Model: {self.__model}") 
        print(f"Sale Price: ¥{sale_price}") # 3種類の自動車のインスタンスを生成 
        
car1 = Car("トヨタ", "プリウス", 3200000, 10) 
car2 = Car("ホンダ", "フィット", 1700000, 15) 
car3 = Car("日産", "ノート", 2290000, 5) 

# メーカー、車種、販売価格を表示 
car1.display_info() 
print() 
car2.display_info() 
print() 
car3.display_info()

# %%
class Student: 
    def __init__(self, program, student_id, name, math_score, physics_score, chemistry_score): 
        self.__program = program 
        self.__student_id = student_id 
        self.__name = name 
        self.__math_score = math_score 
        self.__physics_score = physics_score 
        self.__chemistry_score = chemistry_score 
        self.__average_score = self.__calculate_average() 
        
    def __calculate_average(self): 
        return round((self.__math_score + self.__physics_score + self.__chemistry_score) / 3, 2) 
    
    def get_average_score(self): 
        return self.__average_score 
    
    def get_math_score(self): 
        return self.__math_score 
    
    def set_math_score(self, score): 
        self.__math_score = score 
        self.__average_score = self.__calculate_average() 
        
    def get_physics_score(self): 
        return self.__physics_score 
    
    def set_physics_score(self, score): 
        self.__physics_score = score 
        self.__average_score = self.__calculate_average() 
        
    def get_chemistry_score(self): 
        return self.__chemistry_score 
    
    def set_chemistry_score(self, score): 
        self.__chemistry_score = score 
        self.__average_score = self.__calculate_average() 
        
    def __str__(self): 
        return f"{self.__program}, {self.__student_id}, {self.__name}, {self.__math_score}, {self.__physics_score}, {self.__chemistry_score}" 
    
# 動作確認用スクリプト 
student1 = Student("情報システムプログラム", "mib22001", "前橋太郎", 68, 72, 59)  
student2 = Student("情報システムプログラム", "mib22002", "高崎次郎", 88, 65, 73)
student3 = Student("情報システムプログラム", "mib22003", "太田三郎", 53, 62, 60)
student4 = Student("情報システムプログラム", "mib22004", "桐生四郎", 90, 86, 88)
student5 = Student("情報システムプログラム", "mib22005", "沼田五郎", 78, 80, 66)

# 学生の情報と平均点を表示 
print(student1) 
print(f"Average Score: {student1.get_average_score()}") 
print() 

print(student2) 
print(f"Average Score: {student2.get_average_score()}") 
print() 

print(student3) 
print(f"Average Score: {student3.get_average_score()}") 
print() 

print(student4) 
print(f"Average Score: {student4.get_average_score()}") 
print() 

print(student5) 
print(f"Average Score: {student5.get_average_score()}") 
print() 

# スコアの変更と再表示 
student1.set_math_score(75) 
print(student1) 
print(f"Updated Average Score: {student1.get_average_score()}") 
print()
# %%
class Circle:
    PI = 3.1415926
    
    def __init__(self, radius):
        self.radius = float(radius) if radius >= 0 else 0.0
    
    def calc(self):
        circumference = 2 * self.PI ** self.radius
        area = self.PI * self.radius ** 2
        return [circumference, area]
    
    @property
    def circumference(self):
        return self.calc()[0]
    
    @property
    def area(self):
        return self.calc()[1]

Circle.PI = 3.14
a = Circle(5)
b = Circle(10)
print(f"PI (Circle.PI): {Circle.PI}")
print(f"a (a.calc()): {a.calc()}")
print(f"b (b.calc()): {b.calc()}")
Circle.PI = 3.1415926
print(f"PI (Circle.PI): {Circle.PI}")
print(f"a (a.calc()): {a.calc()}")
print(f"b (b.calc()): {b.calc()}")
# %%
class Circle:
    PI = 3.14

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("半径は正の値")
        self.radius = radius

    def calc_circumference(self):
        return 2 * self.PI * self.radius

    def calc(self):
        return self.PI * self.radius ** 2

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        if height <= 0:
            raise ValueError("高さは正の値")
        self.height = height

    def calc_circumference(self):
        return 2 * self.PI * self.radius * self.height

    def calc(self):
        return 2 * self.PI * self.radius * (self.radius + self.height)

Circle.PI = 3.14
a = Cylinder(5, 5)
b = Cylinder(10, 10)
print(f"PI = {Circle.PI}")
print(f"a = {a.calc}")
print(f"b = {b.calc}")
Circle.PI = 3.1415926
print(f"PI = {Circle.PI}")
print(f"a = {a.calc}")
print(f"b = {b.calc}")

# %%
class Circle:
    PI = 3.14

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("半径は正の値")
        self.radius = radius

    def calc_circumference(self):
        return 2 * self.PI * self.radius

    def calc_area(self):
        return self.PI * self.radius ** 2

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        if height <= 0:
            raise ValueError("高さは正の値")
        self.height = height

    def calc_volume(self):
        return self.PI * self.radius ** 2 * self.height

if __name__ == "__main__":
    Circle.PI = 3.14
    a = Cylinder(5, 5)
    b = Cylinder(10, 10)
    print(f"PI = {Circle.PI}")
    print(f"a = {a.calc_volume()}")
    print(f"b = {b.calc_volume()}")
    Circle.PI = 3.1415926
    print(f"PI = {Circle.PI}")
    print(f"a = {a.calc_volume()}")
    print(f"b = {b.calc_volume()}")
# %%
import statistics

class my_statistics:
    def basic(self, data):
        try:
            numbers = [float(x) for x in data if isinstance(x, (int, float))]

            count = len(numbers)
            max_value = max(numbers)
            min_value = min(numbers)
            total = sum(numbers)
            mean = round(statistics.mean(numbers), 2)
            median = round(statistics.median(numbers), 2)
            std_dev = round(statistics.stdev(numbers), 2)

            return [count, max_value, min_value, total, mean, median, std_dev]
        except ValueError:
            return "不正な値が含まれています"

a = [10.14, 5.3, 8.16, 3.22, 7.4, 18.6, 11.2, 2.9, 14.3, 11.12]
b = my_statistics.basic(a)
print(b)
a = [10.14, 5.3, 8.16, 3.22, 7.4, 18.6, 11.2, 2.9, 14.3, '課題']
b = my_statistics.basic(a)
print (b)
# %%
import statistics 

class my_statistics: 
    def basic(self, data): 
        try:
            numbers = [] 
            for x in data: 
                if isinstance(x, (int, float)): 
                    numbers.append(float(x)) 
                elif isinstance(x, str) and x.replace('.', '', 1).isdigit(): 
                    numbers.append(float(x))
            count = len(numbers) 
            max_value = max(numbers) 
            min_value = min(numbers) 
            total = sum(numbers) 
            mean = round(statistics.mean(numbers), 2) 
            median = round(statistics.median(numbers), 2) 
            std_dev = round(statistics.stdev(numbers), 2) 
        
            return [count, max_value, min_value, total, mean, median, std_dev] 
        except ValueError: 
            return "不正な値が含まれています" 

a = [10.14, 5.3, 8.16, 3.22, 7.4, 18.6, 11.2, 2.9, 14.3, 11.12]  
b = my_statistics().basic(a) 
print(b)
a = [10.14, 5.3, 8.16, 3.22, 7.4, 18.6, 11.2, 2.9, 14.3, '課題'] 
b = my_statistics() .basic(a) 
print(b)
# %% 
import statistics 
class my_statistics: 
    def basic(self, data): 
        try: 
            numbers = [] 
            for x in data: 
                if isinstance(x, (int, float)): 
                    numbers.append(float(x)) 
                else: 
                    try: 
                        numbers.append(float(x)) 
                    except ValueError: 
                        return "不正な値が含まれています: {}".format(x) 
                
            if not numbers:
                return "データに有効な数値がありません" 
    
            count = len(numbers)
            max_value = max(numbers) 
            min_value = min(numbers) 
            total = sum(numbers) 
            mean = round(statistics.mean(numbers), 2) 
            median = round(statistics.median(numbers), 2) 
            
            if count > 1: 
                std_dev = round(statistics.stdev(numbers), 2) 
            else: 
                std_dev = "標準偏差を計算するのに十分なデータがありません" 
                
            return [count, max_value, min_value, total, mean, median, std_dev]
        
        except Exception as e: 
            return f"エラーが発生しました: {str(e)}" 
        
a = [10.14, 5.3, 8.16, 3.22, 7.4, 18.6, 11.2, 2.9, 14.3, 11.12] 
b = my_statistics().basic(a) 
print(b) 
a = [10.14, 5.3, 8.16, 3.22, 7.4, 18.6, 11.2, 2.9, 14.3, '課題'] 
b = my_statistics().basic(a) 
print(b)