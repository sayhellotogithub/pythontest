import matplotlib.pyplot as plt

# サンプルデータ
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
temps = [22, 25, 24, 20, 23]

# 折れ線グラフ作成
plt.plot(days, temps, marker='o')
plt.title('Temperature Over the Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
