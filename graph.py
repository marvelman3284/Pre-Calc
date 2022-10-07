import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot()

x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)


plt.plot(x, y)
# plt.title('Happiness vs Time (Day 1)')
#
# ax.set_xticks(time)
# ax.set_xticklabels(['Comp Sci', 'Math', 'Spanish', 'Study Hall', 'English', 'Gym'])
# ax.set_yticks([i for i in range(11)])
# ax.set_xlabel('Class')
# ax.set_ylabel('Happiness level (out of 10)')

plt.show()
