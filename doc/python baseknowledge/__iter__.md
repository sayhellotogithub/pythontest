## **`__iter__` について**

`__iter__` は、Python の **イテレータ (iterator)** を定義するための特殊メソッド（マジックメソッド）です。

カスタムクラスを **イテラブル (iterable)** にするには、`__iter__` メソッドを実装する必要があります。

------

## **1. `__iter__` の基本**

`__iter__` は **オブジェクトを反復可能 (iterable) にする** ために使われます。`for` ループや `list()` などの関数でオブジェクトを使えるようにするために必要です。

### **イテラブルとは？**

**イテラブル (iterable)** とは、`for` ループで反復できるオブジェクトのことです。
Python の組み込みデータ型（`list`, `tuple`, `dict`, `set`, `str` など）はすべてイテラブルです。

------

## **2. `__iter__` の実装**

カスタムクラスをイテラブルにするには、`__iter__` メソッドを実装し、**イテレータ (iterator)** を返す必要があります。

### **① `__iter__` メソッドを実装**

```
class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        """イテレータオブジェクトを返す"""
        self.current = self.start  # イテレーション開始位置
        return self

    def __next__(self):
        """次の要素を返す"""
        if self.current > self.end:
            raise StopIteration  # イテレーション終了
        value = self.current
        self.current += 1
        return value

# イテラブルオブジェクトの作成
numbers = MyNumbers(1, 5)

# for ループで反復処理
for num in numbers:
    print(num)

# 出力:
# 1
# 2
# 3
# 4
# 5
```

### **ポイント**

✅ `__iter__` メソッド → `self` を返す
✅ `__next__` メソッド → 反復処理の **次の値を返す**
✅ `StopIteration` を `raise` するとループ終了

このように、`__iter__` を実装することで、オブジェクトを `for` ループで使えるようになります。

------

## **3. `__iter__` を `iter()` で確認**

`iter()` を使うと、オブジェクトがイテレータであるかを確認できます。

```
numbers = MyNumbers(1, 3)

# イテレータオブジェクトを取得
iterator = iter(numbers)

# `next()` で要素を取得
print(next(iterator))  # 出力: 1
print(next(iterator))  # 出力: 2
print(next(iterator))  # 出力: 3
print(next(iterator))  # StopIteration 発生
```

------

## **4. `__iter__` なしのクラス**

もし `__iter__` を実装しないと、次のようにエラーになります。

```
class NoIterable:
    def __init__(self, value):
        self.value = value

obj = NoIterable(10)

# for ループを試す
for x in obj:
    print(x)  # TypeError: 'NoIterable' object is not iterable
```

✅ `__iter__` を実装しないと、イテラブルとして扱えない。

------

## **5. `__iter__` をリストのように使う**

リストのようにカスタムクラスを扱うには、`__iter__` で `iter()` を呼び出せばOK。

```
class MyList:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        """リストのイテレータを返す"""
        return iter(self.items)  # リストのイテレータを返す

my_list = MyList([10, 20, 30, 40])

# for ループで使う
for item in my_list:
    print(item)

# 出力:
# 10
# 20
# 30
# 40
```

✅ **リストの `iter()` をそのまま返す** ことで、カスタムクラスをイテラブルにする。
✅ **`__next__` を実装しなくてもOK**（Python のリストが `__next__` を持つため）。

------

## **6. `yield` を使った `__iter__`**

ジェネレータを使うと、もっと簡単に `__iter__` を実装できます。

```
class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        """ジェネレータでイテレータを作成"""
        current = self.start
        while current <= self.end:
            yield current
            current += 1

# イテラブルオブジェクトを作成
numbers = MyNumbers(1, 5)

# for ループで使う
for num in numbers:
    print(num)

# 出力:
# 1
# 2
# 3
# 4
# 5
```

✅ `yield` を使うと、**`__next__` を自動的に実装** できる。
✅ コードがシンプルで、メモリ効率が良い（ジェネレータの利点）。

------

## **7. まとめ**

✅ **`__iter__` を実装すると `for` ループで反復可能に**
✅ **イテレータは `__iter__` (selfを返す) と `__next__` (値を返す) を実装する**
✅ **リストの `iter()` を返すことで簡単にイテラブルにできる**
✅ **ジェネレータ (`yield`) を使うと `__next__` を省略できる**

カスタムクラスを **イテレータとして動作させる** ことで、より柔軟なデータ構造を作成できます！ 🚀