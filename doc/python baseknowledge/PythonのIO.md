## **PythonのI/O（入力と出力）**

PythonのI/O（Input/Output）とは、データの入出力を指します。主に以下のような処理を行います。

1. **標準入力（キーボード入力）**
2. **標準出力（画面への出力）**
3. **ファイルI/O（ファイルの読み書き）**
4. **JSONやCSVなどのデータ形式の読み書き**

------

## **1. 標準入力（キーボードからの入力）**

### **① `input()` を使った入力**

```
name = input("あなたの名前を入力してください: ")
print(f"こんにちは、{name}さん！")
```

📌 `input()` はユーザーが入力した値を **文字列（str）** として返します。

### **② 数値として処理したい場合**

```
age = int(input("年齢を入力してください: "))
print(f"来年は {age + 1} 歳ですね！")
```

📌 `int()` や `float()` で型変換しないと、計算時にエラーになります。

------

## **2. 標準出力（画面への出力）**

### **① `print()` を使う**

```
print("こんにちは、Python！")
```

### **② 複数の値を出力**

`print()` は **カンマ（,）区切りで複数の値を出力** できます。

```
name = "Anna"
age = 25
print("名前:", name, "年齢:", age)
```

📌 `,` を使うと **スペースが自動で入る**。

### **③ `sep` と `end` の使い方**

```
print("A", "B", "C", sep="-")  # A-B-C
print("Hello", end="")         # 改行なし
print(" World")                # Hello World
```

📌 `sep="-"` → 出力の間を `-` で区切る
📌 `end=""` → 改行なしで次の `print()` を続ける

------

## **3. ファイルI/O（ファイルの読み書き）**

Pythonでは、`open()` を使ってファイルの読み書きができます。

### **① ファイルの書き込み (`write()`)**

```
with open("sample.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")
```

📌 `"w"` モードは「書き込み専用」。**既存の内容を上書き** する。

### **② ファイルの追記 (`append`)**

```
with open("sample.txt", "a") as f:
    f.write("追加のテキスト\n")
```

📌 `"a"` モードは **ファイルの末尾に追記** する。

### **③ ファイルの読み込み (`read()`)**

```
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
```

📌 `"r"` モードは **読み込み専用**。

### **④ 行単位で読み込む**

```
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())  # `.strip()` で改行を削除
```

📌 `readline()` → 1行ずつ読む
📌 `readlines()` → すべての行をリストで取得

------

## **4. JSONデータの読み書き**

JSON形式は、辞書（`dict`）に似た構造を持つデータ形式です。

### **① JSONデータの書き込み**

```
import json

data = {"name": "Anna", "age": 25, "city": "Tokyo"}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # `indent=4` で見やすくする
```

### **② JSONデータの読み込み**

```
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)  # {'name': 'Anna', 'age': 25, 'city': 'Tokyo'}
```

📌 **JSONはAPI通信などでよく使われる！**

------

## **5. CSVデータの読み書き**

CSV（カンマ区切りファイル）は、データの保存や交換によく使われます。

### **① CSVの書き込み**

```

import csv

data = [["名前", "年齢", "都市"], ["Anna", 25, "Tokyo"], ["John", 30, "Osaka"]]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### **② CSVの読み込み**

```

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

📌 `newline=""` を指定しないと **Windows環境では空行が入る** ことがある。

------

## **6. バイナリファイルの扱い**

### **① 画像ファイルの読み込み**

```
with open("image.jpg", "rb") as f:  # "rb" = バイナリ読み込み
    data = f.read()
```

### **② 画像ファイルの書き込み**

```
with open("copy.jpg", "wb") as f:  # "wb" = バイナリ書き込み
    f.write(data)
```

📌 バイナリファイル（画像・動画など）は `"rb"`（読み込み）・`"wb"`（書き込み）を使う。

------

## **7. I/Oの例外処理**

ファイルI/Oはエラーが発生しやすいので、`try-except` を使うのが安全です。

```
try:
    with open("non_existent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("ファイルが見つかりません！")
```

------

## **8. まとめ**

| **操作**                     | **方法**                |
| ---------------------------- | ----------------------- |
| **標準入力**                 | `input()`               |
| **標準出力**                 | `print()`               |
| **ファイル書き込み**         | `open("file.txt", "w")` |
| **ファイル読み込み**         | `open("file.txt", "r")` |
| **JSONの書き込み**           | `json.dump()`           |
| **JSONの読み込み**           | `json.load()`           |
| **CSVの書き込み**            | `csv.writer()`          |
| **CSVの読み込み**            | `csv.reader()`          |
| **バイナリファイル読み書き** | `open("file", "rb/wb")` |

📌 **`with open()` を使えば、ファイルを自動で閉じるので安全！**
📌 **JSONやCSVの入出力も `json` / `csv` モジュールで簡単！**