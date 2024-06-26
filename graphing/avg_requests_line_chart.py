# Plotting a line graph for the given data
import matplotlib.pyplot as plt

# Data
x = [2, 3, 4, 5, 6]
y = [5000, 3333, 2500, 2000, 1667]

# Create line graph
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Servers')
plt.ylabel('Number of Requests')
plt.title('Average Number of Requests against Number of Servers')

#plt.show()
plt.savefig('avg_req_line_chart.png')