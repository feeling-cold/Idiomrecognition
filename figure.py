#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y1 = [0.09, 0.17, 0.26, 0.35, 0.45, 0.55, 0.61, 0.71, 0.81, 0.88]
y2 = [0.01, 0.02, 0.02, 0.02, 0.03, 0.05, 0.06, 0.08, 0.08, 0.08]
y3 = [0,0,0,0,0,0,0,0,0,0]


plt.plot(x, y1, 'r',marker='*', markersize=10)
plt.plot(x, y2, 'b', marker='*',markersize=10)
plt.plot(x, y3, 'g', marker='*',markersize=10)
plt.title('Precision contrast line chart')
plt.xlabel('hits')
plt.ylabel('accuracy')
for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

plt.legend(['Integrated System', 'ASRT','DTW'])
plt.savefig('test.png')
plt.show()
