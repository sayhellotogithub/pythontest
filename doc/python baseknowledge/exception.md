Pythonの例外（Exception）について説明します。

## **1. 例外とは？**

Pythonプログラム実行中に発生するエラーのことを「例外（Exception）」と呼びます。例外が発生すると、通常プログラムはクラッシュしますが、適切に処理すればプログラムを正常に動作させ続けることができます。

------

## **2. 例外の基本的な処理**

Pythonでは `try-except` 構文を使って例外を処理できます。

### **基本構文**

```
try:
    # 例外が発生する可能性のあるコード
    x = 10 / 0  # ゼロ除算エラー
except ZeroDivisionError:
    # 例外が発生した場合の処理
    print("ゼロで割ることはできません。")
```

**出力:**

```
ゼロで割ることはできません。
```

------

## **3. 例外の種類**

Pythonには多くの組み込み例外があります。よく使われるものをいくつか紹介します。

| 例外名              | 説明                                     |
| ------------------- | ---------------------------------------- |
| `ZeroDivisionError` | 0で除算したとき                          |
| `ValueError`        | 不正な値を受け取ったとき                 |
| `IndexError`        | リストなどのインデックスが範囲外のとき   |
| `KeyError`          | 辞書に存在しないキーを参照したとき       |
| `TypeError`         | データ型のミス（例：数値と文字列の演算） |
| `FileNotFoundError` | 指定したファイルが見つからないとき       |

------

## **4. `except` で複数の例外を処理**

複数の例外をキャッチする場合、以下のように書けます。

```
try:
    num = int("abc")  # 文字列を整数に変換（ValueError）
except (ZeroDivisionError, ValueError) as e:
    print(f"エラー発生: {e}")
```

**出力:**

```
エラー発生: invalid literal for int() with base 10: 'abc'
```

------

## **5. `finally` で後処理**

`finally` ブロックを使うと、例外の有無にかかわらず必ず実行されるコードを記述できます。

```
try:
    f = open("test.txt", "r")  # ファイルを開く
except FileNotFoundError:
    print("ファイルが見つかりません。")
finally:
    print("処理終了。")  # ここは必ず実行される
```

------

## **6. `raise` を使って例外を発生させる**

自分で例外を発生させることもできます。

```
def check_age(age):
    if age < 0:
        raise ValueError("年齢は0以上でなければなりません。")

try:
    check_age(-5)
except ValueError as e:
    print(f"エラー: {e}")
```

**出力:**

```
エラー: 年齢は0以上でなければなりません。
```

------

## **7. 独自の例外を定義**

Pythonでは独自の例外クラスを作成できます。

```
class CustomError(Exception):
    pass

try:
    raise CustomError("これはカスタム例外です。")
except CustomError as e:
    print(f"エラー発生: {e}")
```

**出力:**

```
エラー発生: これはカスタム例外です。
```

------

## **まとめ**

- `try-except` を使って例外をキャッチする。
- `except` に複数の例外を指定できる。
- `finally` を使えば後処理を必ず実行できる。
- `raise` を使えば自分で例外を発生させられる。
- 独自の例外クラスも作成可能。