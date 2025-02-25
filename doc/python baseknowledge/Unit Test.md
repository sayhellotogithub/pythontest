## **Unit Test（単体テスト）とは？**

Unit Test（単体テスト）とは、プログラムの最小単位（関数やクラス）が正しく動作するかを確認するテストのことです。
Pythonでは `unittest` モジュールを使ってテストを作成できます。

------

## **1. `unittest` を使った基本的なテスト**

### **① テスト対象の関数**

まず、以下のような `math_operations.py` というファイルを作成します。

```
# math_operations.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("ゼロで割ることはできません")
    return a / b
```

------

### **② `unittest` を使ってテストを書く**

次に、テストコードを `test_math_operations.py` に書きます。

```
import unittest
from math_operations import add, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, 2), -3)

        # ゼロ除算のテスト
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()
```

### **③ テストの実行**

ターミナルで次のコマンドを実行します。

```
python -m unittest test_math_operations.py
```

**出力例:**

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

✅ **2つのテストが成功しました！**

------

## **2. `unittest` の基本的なアサーション**

`unittest` では、さまざまなアサーションメソッドを使ってテストを行えます。

| メソッド                               | 説明                                                |
| -------------------------------------- | --------------------------------------------------- |
| `assertEqual(a, b)`                    | `a == b` であることを確認                           |
| `assertNotEqual(a, b)`                 | `a != b` であることを確認                           |
| `assertTrue(x)`                        | `x` が `True` であることを確認                      |
| `assertFalse(x)`                       | `x` が `False` であることを確認                     |
| `assertIsNone(x)`                      | `x` が `None` であることを確認                      |
| `assertIsNotNone(x)`                   | `x` が `None` ではないことを確認                    |
| `assertRaises(Exception, func, *args)` | `func(*args)` が `Exception` を発生させることを確認 |

------

## **3. `setUp()` と `tearDown()` の活用**

`setUp()` と `tearDown()` を使うと、テスト前後に特定の処理を実行できます。

```
class TestExample(unittest.TestCase):

    def setUp(self):
        """ 各テストの前に実行される """
        self.num1 = 10
        self.num2 = 5

    def tearDown(self):
        """ 各テストの後に実行される """
        print("テスト完了")

    def test_addition(self):
        self.assertEqual(self.num1 + self.num2, 15)

if __name__ == "__main__":
    unittest.main()
```

------

## **4. Mock（モック）を使ったテスト**

`unittest.mock` を使うと、外部APIやデータベースの代わりに仮のオブジェクトを作成できます。

```
from unittest.mock import MagicMock

# ダミーの関数を作成
mock_func = MagicMock(return_value="テストデータ")

# 呼び出し
print(mock_func())  # "テストデータ"
```

✅ **外部の依存関係を気にせずテストができる！**

------

## **5. `pytest` を使ったユニットテスト**

`unittest` の代わりに `pytest` を使うと、よりシンプルにテストを書けます。

### **① `pytest` のインストール**

```
pip install pytest
```

### **② `pytest` でのテスト例**

```
# test_math_operations.py
from math_operations import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)
```

### **③ `pytest` の実行**

```
pytest
```

✅ **シンプルで見やすい！**

------

## **まとめ**

| 方法       | 特徴                                        |
| ---------- | ------------------------------------------- |
| `unittest` | Python標準、堅牢なテスト機能                |
| `pytest`   | シンプルで柔軟、エラーメッセージが見やすい  |
| `mock`     | 外部APIやDBの代わりに仮のオブジェクトを作成 |