import matplotlib.pyplot as plt
import random

def rand_color(n):
    return (random.uniform(0.0, 1.0),random.uniform(0.0, 1.0),random.uniform(0.0, 1.0) )

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

lines = [line.rstrip('\n') for line in open("result.txt")]
lines.pop(0); # remove the first lines
threads1 = []
threads2 = []
threads3 = []
second1 = []
second2 = []
second3 = []
latency1 = []
latency2 = []
latency3 = []
for line in lines:
    v = line.split(",")
    if int(v[0])==1:
        threads1.append(v[1])
        second1.append(v[2])
        latency1.append(float(v[3]))
    if int(v[0])==2:
        threads2.append(v[1])
        second2.append(v[2])
        latency2.append(float(v[3]))
    if int(v[0])==3:
        threads3.append(v[1])
        second3.append(v[2])
        latency3.append(float(v[3]))

print(str(mean(latency1)))
print(str(mean(latency2)))
print(str(mean(latency3)))
# plt.plot(threads1, latency1, color=rand_color(1), label="Difficulty 1")
# plt.plot(threads2, latency2, color=rand_color(2), label="Difficulty 2")
# plt.plot(threads3, latency3, color=rand_color(3), label="Difficulty 3")
plt.plot(threads1, second1, color=rand_color(1), label="Difficulty 1")
plt.plot(threads2, second2, color=rand_color(2), label="Difficulty 2")
plt.plot(threads3, second3, color=rand_color(3), label="Difficulty 3")
plt.ylabel('Seconds')
plt.xlabel('Threads')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
plt.show()
