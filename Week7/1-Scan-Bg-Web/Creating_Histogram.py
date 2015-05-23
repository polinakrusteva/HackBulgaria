from Crawling import Histogram
import matplotlib.pyplot as plt


h = Histogram()

with open("servers.txt", "r") as f:
    data = f.read().split("\n")

for info in data:
    for server in ["Apache", "nginx", "Oracle", "lighttpd", "Microsoft-IIS"]:
        if server in info:
            h.add(server)

keys = list(h.get_dict().keys())
X = list(range(len(keys)))
values = list(h.get_dict().values())

for key, count in h.items():
        print("{}: {}".format(key, count))

plt.bar(X, list(values), width=1)
plt.xticks(X, keys)
plt.xlabel("Server")
plt.ylabel("Count")
ax = plt.subplot(111)
plt.title("Most used severs for BG sites")
plt.savefig("histogram.png")
