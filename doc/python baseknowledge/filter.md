### **Pythonの `filter()` 関数**

`filter()` は **リストやイテラブルから特定の条件を満たす要素だけを抽出する** 関数です。

------

## **1. `filter()` の基本構文**

```
filter(function, iterable)
```

- `function`：各要素に適用される関数（`True` を返した要素だけが残る）
- `iterable`：リストやタプルなどのデータ

------

## **2. `filter()` の使用例**

### **① 偶数だけを抽出**

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 偶数を抽出
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # [2, 4, 6, 8, 10]
```

`lambda x: x % 2 == 0` は **偶数なら `True`、奇数なら `False`** を返すので、`filter()` によって偶数だけがリストに残ります。

------

### **② 空文字を除去**

```
words = ["apple", "", "banana", " ", "cherry", None, "grape"]

# 空文字やNoneを除去
filtered_words = list(filter(lambda x: x and x.strip(), words))

print(filtered_words)  # ['apple', 'banana', 'cherry', 'grape']
```

`x and x.strip()` は、`None` や空白文字 (`" "`) も除去する条件になっています。

------

### **③ リスト内の正の数を抽出**

```
nums = [-3, -2, -1, 0, 1, 2, 3]

positive_nums = list(filter(lambda x: x > 0, nums))

print(positive_nums)  # [1, 2, 3]
```

**0より大きい数だけを抽出** しています。

------

## **3. `filter()` vs `map()`**

| 関数                         | 目的                                     |
| ---------------------------- | ---------------------------------------- |
| `filter(function, iterable)` | 条件に合う要素だけを残す                 |
| `map(function, iterable)`    | 各要素に関数を適用し、新しいリストを作る |

### **例： `map()` vs `filter()`**

```
nums = [1, 2, 3, 4, 5]

# すべての数を2倍にする（map）
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8, 10]

# 偶数だけを残す（filter）
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]
```

------

## **4. `filter()` を使わずにリスト内包表記で書く**

Python では、リスト内包表記を使うと `filter()` と同じことができます。

### **偶数抽出（リスト内包表記）**

```
even_numbers = [x for x in numbers if x % 2 == 0]
```

これは `filter(lambda x: x % 2 == 0, numbers)` と同じ動作をしますが、可読性が高くなります。

------

## **5. `filter()` のメリット**

✅ **メモリ効率が良い**： `filter()` はイテレータを返すため、大量のデータを処理するときにメモリを節約できる。
✅ **条件に合う要素を簡単に抽出できる**（`if` 文を書く手間を省略）。

------

## **6. まとめ**

- `filter()` は **指定した条件を満たす要素のみを抽出する関数**。
- `lambda` 関数と組み合わせることで、短く簡潔に記述できる。
- `map()` は「変換」、`filter()` は「抽出」。
- リスト内包表記を使うと `filter()` を書かずに同じことができる。

👉 大規模データを扱うときは `filter()` がメモリ効率的に有利ですが、コードの読みやすさを重視するなら **リスト内包表記** もおすすめです！