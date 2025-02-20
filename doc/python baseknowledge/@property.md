`@property` は、Python の **プロパティ (property)** を定義するためのデコレーターで、クラスのメソッドを「ゲッター (getter)」として扱えるようにします。これにより、通常のインスタンス変数のようにアクセスしながら、内部的にはメソッドを実行できるため、カプセル化 (encapsulation) を維持しつつ柔軟なデータ操作が可能になります。

------

## **1. `@property` の基本的な使い方**

通常、クラスの属性を取得するには `self.attribute` を直接アクセスしますが、`@property` を使うと、**メソッドを属性のように呼び出すことができます**。

### **例: `@property` を使ったゲッター**

```
class Person:
    def __init__(self, name, age):
        self._name = name  # プライベート変数
        self._age = age    # プライベート変数

    @property
    def name(self):
        """名前を取得するプロパティ"""
        return self._name

    @property
    def age(self):
        """年齢を取得するプロパティ"""
        return self._age

# インスタンスの作成
p = Person("Anna", 25)

# プロパティを使ってアクセス
print(p.name)  # 出力: Anna
print(p.age)   # 出力: 25

# 直接代入しようとするとエラー
# p.age = 30  # AttributeError: can't set attribute 'age'
```

### **ポイント**

- `@property` を付けると、メソッドを **属性のように** 使うことができます。
- `p.age()` のように **メソッドとしてではなく、p.age のように** 呼び出せます。
- `@property` を使うと、**値の変更（セッター）ができなくなる** ため、データを安全に管理できます。

------

## **2. `@property` を使ったセッター（@メソッド名.setter）**

上記の例では、`age` に値を設定しようとするとエラーになります。
これを解決するには、`@メソッド名.setter` を使って **セッターメソッドを定義** します。

### **例: `@property` + `@メソッド名.setter`**

```
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        """年齢を取得するプロパティ"""
        return self._age

    @age.setter
    def age(self, value):
        """年齢を設定するプロパティ（バリデーション付き）"""
        if value < 0:
            raise ValueError("年齢は0以上である必要があります")
        self._age = value

# インスタンス作成
p = Person("Anna", 25)

# age を変更
p.age = 30  # OK
print(p.age)  # 出力: 30

# 不正な値を設定しようとするとエラー
# p.age = -5  # ValueError: 年齢は0以上である必要があります
```

### **ポイント**

- `@age.setter` を定義すると、 `p.age = 30` のように値を設定できるようになります。
- セッターメソッド内で **バリデーション（値のチェック）** を行うことで、データの整合性を確保できます。

------

## **3. `@property` を使ったデリーター（@メソッド名.deleter）**

`@メソッド名.deleter` を使うと、`del` キーワードでプロパティを削除できるようになります。

### **例: `@property` + `@メソッド名.deleter`**

```
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年齢は0以上である必要があります")
        self._age = value

    @age.deleter
    def age(self):
        """年齢を削除するプロパティ"""
        print("年齢情報を削除しました")
        del self._age

# インスタンス作成
p = Person("Anna", 25)

# age を削除
del p.age  # 出力: 年齢情報を削除しました

# 削除後にアクセスするとエラー
# print(p.age)  # AttributeError: 'Person' object has no attribute '_age'
```

### **ポイント**

- `@age.deleter` を使うと、 `del p.age` でプロパティを削除できます。
- 削除後に `p.age` にアクセスすると `AttributeError` になります。

------

## **4. `@property` を使うメリット**

1. **データのカプセル化**
   - 直接属性を操作せず、メソッドを通じてアクセスするため、データの整合性を保ちやすい。
2. **バリデーションが簡単**
   - `setter` でバリデーションを追加できるため、不正なデータを防ぐことができる。
3. **シンプルな記述で可読性向上**
   - `@property` を使うと、メソッドのように `()` を書かなくても、通常の属性のようにアクセスできる。
4. **ゲッター/セッターの統一**
   - `p.age` のようにシンプルに使えるため、OOP の原則を守りつつ、直感的なコードが書ける。

------

## **5. `@property` の応用例**

例えば、`@property` を使って、温度の単位変換を自動化することもできます。

```
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """摂氏温度を取得"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """摂氏温度を設定"""
        if value < -273.15:
            raise ValueError("絶対零度以下にはできません")
        self._celsius = value

    @property
    def fahrenheit(self):
        """華氏温度を取得（変換）"""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """華氏温度を設定（変換）"""
        self._celsius = (value - 32) * 5/9

# インスタンス作成
temp = Temperature(25)

# 摂氏温度の取得
print(temp.celsius)  # 出力: 25

# 華氏温度の取得
print(temp.fahrenheit)  # 出力: 77.0

# 華氏温度を変更（摂氏に変換）
temp.fahrenheit = 212
print(temp.celsius)  # 出力: 100.0
```

------

## **6. まとめ**

✅ `@property` を使うと、メソッドを属性のように呼び出せる
✅ `@プロパティ名.setter` を使うと、バリデーション付きのセッターを作成できる
✅ `@プロパティ名.deleter` を使うと、`del` キーワードで属性を削除できる
✅ データのカプセル化とバリデーションがしやすくなり、コードの可読性と安全性が向上する

Python でプロパティを適切に活用することで、より直感的で管理しやすいクラス設計ができます！

