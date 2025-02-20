Decorator

**デコレータ（Decorator）** は、関数やメソッドに **追加の機能を付与するための関数** です。Pythonでは、デコレータを使うことで、既存の関数の振る舞いを変更したり、拡張したりできます。デコレータは通常、関数の前に `@` 記号を付けて使用します。

------

### **1. デコレータの基本的な仕組み**

デコレータは、**他の関数を引数として受け取り、その関数をラップして新しい関数を返す** 関数です。新しく返される関数は、元の関数の前後で何らかの処理を追加することができます。

### **2. デコレータの基本構文**

```
def decorator_function(original_function):
    def wrapper_function():
        print("追加機能を実行")
        return original_function()
    return wrapper_function

@decorator_function
def some_function():
    print("元の関数を実行")
```

- `decorator_function` がデコレータで、`original_function`（元の関数）を引数として受け取り、その周囲にラップした処理（`wrapper_function`）を追加します。
- `@decorator_function` を関数の前に付けることで、その関数がデコレータに渡され、ラップされた新しい関数が実行されるようになります。

------

### **3. デコレータの例**

#### **① 基本的なデコレータ**

```
def decorator_function(original_function):
    def wrapper_function():
        print("デコレータで機能を追加")
        original_function()
        print("デコレータで機能を終了")
    return wrapper_function

@decorator_function
def display():
    print("元の関数が実行されました")

# 実行
display()
```

**出力結果:**

```

デコレータで機能を追加
元の関数が実行されました
デコレータで機能を終了
```

- `display()` 関数が呼び出されると、元の関数の前後でデコレータが実行され、追加の処理が挿入されます。

------

#### **② 引数を持つ関数のデコレータ**

引数を受け取る関数をデコレートする場合、`wrapper_function` も引数を受け取れるようにする必要があります。

```
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("デコレータで機能を追加")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display(message):
    print(f"メッセージ: {message}")

# 実行
display("こんにちは")
```

**出力結果:**

```
デコレータで機能を追加
メッセージ: こんにちは
```

- `display()` 関数は引数 `message` を受け取るため、`wrapper_function` も `*args, **kwargs` を使ってそれらを渡します。

------

#### **③ 返り値を変更するデコレータ**

デコレータは、関数の返り値を変更することもできます。

```
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return f"デコレータで変更: {result}"
    return wrapper_function

@decorator_function
def greet(name):
    return f"こんにちは, {name}!"

# 実行
print(greet("山田"))
```

**出力結果:**

```
デコレータで変更: こんにちは, 山田!
```

- デコレータで元の関数の返り値を加工して、新しい返り値を返しています。

------

### **4. 複数のデコレータを使う**

デコレータは複数使うこともできます。デコレータは上から順番に適用されます。

```
def decorator_one(original_function):
    def wrapper():
        print("デコレータ1開始")
        original_function()
        print("デコレータ1終了")
    return wrapper

def decorator_two(original_function):
    def wrapper():
        print("デコレータ2開始")
        original_function()
        print("デコレータ2終了")
    return wrapper

@decorator_one
@decorator_two
def say_hello():
    print("こんにちは!")

# 実行
say_hello()
```

**出力結果:**

```

デコレータ1開始
デコレータ2開始
こんにちは!
デコレータ2終了
デコレータ1終了
```

- `@decorator_two` が先に適用され、次に `@decorator_one` が適用されます。この順番が実行順序になります。

------

### **5. デコレータの実用例**

デコレータは様々な場面で活用できます。

#### **① ロギング機能の追加**

```
def log_function(original_function):
    def wrapper(*args, **kwargs):
        print(f"{original_function.__name__} が呼び出されました")
        return original_function(*args, **kwargs)
    return wrapper

@log_function
def add(a, b):
    return a + b

# 実行
print(add(3, 5))
```

**出力結果:**

```
add が呼び出されました
8
```

#### **② パフォーマンス計測**

```
import time

def time_function(original_function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        print(f"{original_function.__name__} の実行時間: {end_time - start_time}秒")
        return result
    return wrapper

@time_function
def slow_function():
    time.sleep(2)

# 実行
slow_function()
```

**出力結果:**

```
slow_function の実行時間: 2.002345秒
```

------

### **6. まとめ**

- **デコレータ（Decorator）** は、関数の前に `@` を付けて、その関数の振る舞いを変更したり拡張したりするものです。
- デコレータは **関数の引数や返り値に変更を加える** ことができます。
- **ログ出力、計測、認証** など、さまざまな用途に使われる強力なツールです。