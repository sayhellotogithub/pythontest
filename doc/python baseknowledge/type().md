## **`type()` について**

Python の `type()` 関数は、オブジェクトの型（クラス）を取得するために使われます。また、3 つの引数を渡すことで、**動的にクラスを作成する** こともできます。

------

## **1. `type()` の基本**

### **① オブジェクトの型を取得**

Python の組み込みオブジェクトの型を調べるのに使います。

```
print(type(10))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type([1, 2, 3]))# <class 'list'>
```

✅ `type(オブジェクト)` で、そのオブジェクトの型を取得できる。

------

### **② クラスの型を取得**

オブジェクトがどのクラスから作られているかも確認できます。

```
class MyClass:
    pass

obj = MyClass()

print(type(obj))    # <class '__main__.MyClass'>
print(type(MyClass)) # <class 'type'>
```

✅ `obj` の型は `MyClass`
✅ **Python のクラス自体も `type` クラスのインスタンス** になっている。

------

## **2. `type()` を使って動的にクラスを作成**

`type()` は 3 つの引数を取ることで、新しいクラスを動的に作成できます。

```
# 新しいクラスを動的に作成
NewClass = type("NewClass", (object,), {"x": 100, "greet": lambda self: "Hello"})

# インスタンスを作成
obj = NewClass()

print(obj.x)       # 出力: 100
print(obj.greet()) # 出力: Hello
print(type(obj))   # <class '__main__.NewClass'>
```

### **動的クラス作成の構文**

```
type(クラス名, 親クラスのタプル, 属性やメソッドを含む辞書)
```

| 引数                   | 説明                                                         |
| ---------------------- | ------------------------------------------------------------ |
| `クラス名`             | クラスの名前（`str` 型）                                     |
| `親クラスのタプル`     | 継承するクラス（`tuple` で指定、`(object,)` を指定すると通常のクラス） |
| `属性やメソッドの辞書` | クラスに追加する属性やメソッドを `dict` で指定               |

✅ **`type()` を使うと、通常の `class` 文を使わずにクラスを作成できる。**
✅ **メタプログラミングや、動的なクラスのカスタマイズに使われる。**

------

## **3. `isinstance()` と `type()` の違い**

`isinstance()` を使うと、オブジェクトがあるクラスまたはそのサブクラスのインスタンスかどうかを確認できます。

```
class Parent:
    pass

class Child(Parent):
    pass

obj = Child()

print(type(obj) == Child)       # 出力: True
print(type(obj) == Parent)      # 出力: False
print(isinstance(obj, Child))   # 出力: True
print(isinstance(obj, Parent))  # 出力: True
```

✅ `type(obj) == Class` → **クラスが完全一致する場合に `True`**
✅ `isinstance(obj, Class)` → **サブクラスも含めて `True`**

------

## **4. `type()` と `metaclass`**

Python のクラスは、実は `type` クラスから作られています。

```
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
```

✅ **クラス自体も `type` のインスタンス**
✅ **`type` は Python のメタクラスとして機能する**
✅ メタクラスをカスタマイズすると、新しいクラスを作成する動作を変更できる

------

## **5. まとめ**

✅ `type(オブジェクト)` → **オブジェクトの型を取得**
✅ `type(クラス名, 親クラスのタプル, 属性やメソッドの辞書)` → **動的にクラスを作成**
✅ `type()` は Python の **クラスの型 (メタクラス) でもある**
✅ `type()` と `isinstance()` の違い → `isinstance()` は **サブクラスも許可**

Python の `type()` を理解すると、メタプログラミングや動的なクラス作成がより扱いやすくなります！