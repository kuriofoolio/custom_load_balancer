import matplotlib.pyplot as plt

OUTPUT_DIR='img'

# # Data
# servers = ['Server 1', 'Server 2', 'Server 3']
# requests = [3047, 3695,3258]

# # Create bar chart
# plt.figure(figsize=(10, 6))
# plt.bar(servers, requests, color=['blue', 'green', 'red'])
# plt.xlabel('Servers')
# plt.ylabel('Number of Requests')
# plt.title('Distribution of 10000 Requests Across 3 Servers')
# #plt.show()
# plt.savefig(f'{OUTPUT_DIR}/bar_chart_3_servers.png')

# Plotting a line graph for the given data

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
plt.savefig(f'{OUTPUT_DIR}/avg_req_line_chart.png')