with open('sample.txt','r',encoding='utf-8') as file:
    for line in file:
        print(line.strip())

#全行をリストで取得する
with open('sample.txt','r',encoding='utf-8') as file:
    lines= file.readlines
    print(lines)

with open('sample.txt', 'r', encoding='utf-8') as file:
    content = file.read()  # ファイル全体を1つの文字列として取得
    print(content)