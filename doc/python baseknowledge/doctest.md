## **doctestとは？**

`doctest` は、Pythonのドキュメント（docstring）内にテストコードを書き、それを実行して期待通りの出力が得られるかを確認するモジュールです。
関数の説明とテストを同時に記述できるため、シンプルなテストに向いています。

------

## **1. 基本的な `doctest` の書き方**

関数の `docstring` に `>>>` を使って入力と出力を記述します。

```
def add(a, b):
    """
    2つの数を足し算する関数

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```

------

## **2. `doctest` の実行**

### **① Pythonスクリプト内で実行**

次のように `if __name__ == "__main__":` を追加すると、スクリプトを実行するだけで `doctest` を実行できます。

```
import doctest

def add(a, b):
    """
    2つの数を足し算する関数

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    doctest.testmod()
```

このスクリプトを実行すると、すべてのテストが成功すれば何も表示されません。
失敗するとエラーが表示されます。

------

### **② コマンドラインで実行**

Pythonの `-m doctest` オプションを使うと、ファイル内の `doctest` を実行できます。

```
python -m doctest your_script.py
```

エラーがなければ何も表示されず、エラーがある場合は詳細が表示されます。

------

## **3. `doctest` の詳細設定**

`doctest` は、出力が多少異なっても成功とみなすように設定できます。

### **① `NORMALIZE_WHITESPACE`（空白の違いを無視）**

```

def greet(name):
    """
    >>> greet("Anna")
    'Hello, Anna! '
    """
    return f"Hello, {name}!  "  # 余分な空白あり

if __name__ == "__main__":
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
```

✅ **空白の違いがあってもOKにする。

------

### **② `ELLIPSIS`（省略記号を許可）**

```
def get_pi():
    """
    >>> get_pi()
    3.14...
    """
    return 3.14159265

if __name__ == "__main__":
    doctest.testmod(optionflags=doctest.ELLIPSIS)
```

✅ **`3.14...` のように部分一致でチェック可能。

------

### **③ `IGNORE_EXCEPTION_DETAIL`（例外メッセージを無視）**

```
def divide(a, b):
    """
    >>> divide(1, 0)
    Traceback (most recent call last):
    ZeroDivisionError: ...
    """
    return a / b
python


CopyEdit
if __name__ == "__main__":
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
```

✅ **例外のメッセージ内容を無視してエラーの種類だけチェック。

------

## **4. `doctest` のメリット・デメリット**

| **メリット**                     | **デメリット**                         |
| -------------------------------- | -------------------------------------- |
| 関数の説明とテストを同時に書ける | 複雑なテストには向かない               |
| 外部ツールなしで実行できる       | 出力の正確な一致が必要（設定で緩和可） |
| シンプルなコードでテスト可能     | メンテナンスが難しくなる場合がある     |

------

## **5. `unittest` や `pytest` との比較**

| **機能**             | **doctest** | **unittest** | **pytest** |
| -------------------- | ----------- | ------------ | ---------- |
| シンプルなテスト     | ✅           | ❌            | ✅          |
| 出力の厳密なチェック | ✅           | ❌            | ❌          |
| 複雑なテスト         | ❌           | ✅            | ✅          |
| 外部ライブラリ不要   | ✅           | ✅            | ❌          |

------

## **6. まとめ**

✅ `doctest` はシンプルな関数のテストに最適。
✅ `unittest` や `pytest` と使い分けるのがベスト。
✅ `ELLIPSIS` や `NORMALIZE_WHITESPACE` などのオプションで使いやすくできる。

`doctest` を活用して、分かりやすい関数とテストを同時に書いていきましょう！ 🚀