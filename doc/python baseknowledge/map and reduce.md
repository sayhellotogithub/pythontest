map/reduce

**Map/Reduce（マップ・リデュース）** は、大量のデータを分散処理するためのプログラミングモデルです。Googleが開発し、Hadoopなどのビッグデータ処理システムでも使われています。

------

## **1. Map/Reduce の仕組み**

### **① Map（マップ）**

- **データを分割し、それぞれを並列処理するフェーズ**

- **キーと値（key-value ペア）を生成する**

- 例：単語の出現回数を数える場合

  ```
  入力: "apple banana apple"
  出力: ("apple", 1), ("banana", 1), ("apple", 1)
  ```

### **② Shuffle（シャッフル）**

- **Mapの出力データをキーごとにまとめるフェーズ**

- 上の例では、同じ単語（キー）を集約

  ```
  ("apple", [1, 1]), ("banana", [1])
  ```

### **③ Reduce（リデュース）**

- **キーごとに値を統合（集約）するフェーズ**

- 例：各単語の出現回数を合計

  ```
  ("apple", 2), ("banana", 1)
  ```

------

## **2. Map/Reduce の活用例**

- **ログ解析**（Webサーバーのアクセスログの分析）
- **単語出現頻度のカウント**（自然言語処理）
- **分散データ処理**（Hadoopでのビッグデータ解析）
- **集計・統計処理**（売上データの集計など）

------

## **3. PythonでのMap/Reduce**

### **Python の `map()` と `reduce()`**

Pythonには、組み込みの `map()` や `functools.reduce()` を使って簡単にMap/Reduceを実装できます。

```python
from functools import reduce

# Map: 各要素を2倍にする
numbers = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: x * 2, numbers))
print(mapped)  # [2, 4, 6, 8, 10]

# Reduce: 合計を求める
summed = reduce(lambda x, y: x + y, numbers)
print(summed)  # 15
```

Hadoopなどの分散システムでは、これを大規模なデータセットに適用します。

------

## **4. まとめ**

- **Map** → データを分割し、個別に処理
- **Shuffle** → 同じキーごとにデータを整理
- **Reduce** → 統合・集約処理を実施
- **大規模データの並列処理に最適**（Hadoop, Spark などで活用）