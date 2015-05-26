import requests


class DirectedGraph:

    def __init__(self):
        self.net = {}

    def get_net(self):
        return self.net

    def has_node(self, node):
        if node in self.net:
            return True
        return False

    def add_node(self, node):
        if self.has_node(node):
            raise Exception("Node already in the graph!")
        self.net[node] = []

    def add_edge(self, node_a, node_b):
        if not self.has_node(node_a):
            self.add_node(node_a)
        if not self.has_node(node_b):
            self.add_node(node_b)
        if node_b not in self.net[node_a]:
            self.net[node_a].append(node_b)

    def get_neighbours_for(self, node):
        if not self.has_node(node):
            raise Exception("Node doesn't exist in the graph!")
        return self.net[node]

    def path_between(self, node_a, node_b):
        if node_b in self.net[node_a]:
            return True
        for node in self.net[node_a]:
            return self.path_between(node_a, node_b)
        return False


class Network:

    IDS = "?client_id=cb35d9d313f2c0461bba&client\
_secret=70583eae0b46facb93cf2fd96d762a36d9b67279"

    ADDRESS = "https://api.github.com/users/"

    def __init___(self, username, level):
        self.username = username
        self.level = level
        self.graph = DirectedGraph()

    def get_username(self):
        return self.username

    def get_network_info(self, user):
        info = {
               "followers": [user["login"] for user in requests.get(
                self.ADDRESS + user + "/followers" + self.IDS).json()],
               "following": [user["login"] for user in requests.get(
                self.ADDRESS + user + "/following" + self.IDS).json()],
               }
        return info

    def build_graph(self, user, level):
        q = []
        visited = set()
        q.append((1, user))
        while len(q) != 0:
            user_data = q.pop(0)
            cl, cu = user_data
            if cu not in visited:
                visited.add(cu)
                info = self.get_network_info(cu)
                for follower in info["followers"]:
                    self.graph.add_edge(follower, cu)
                    if cl + 1 <= level:
                        q.append((cl+1, follower))
                for following in info["following"]:
                    self.graph.add_edge(cu, following)
                    if cl + 1 <= level:
                        q.append((cl+1, following))

    def do_you_follow(self, user):
        return user in self.graph.get_info()[self.username]

    def do_you_follow_indirectly(self, user):
        for followed in self.graph.get_info()[self.username]:
            if user in self.graph.get_info()[followed]:
                return True
        return False

    def does_he_she_follows(self, user):
        return self.username in self.graph.get_info()[user]

    def does_he_she_follows_indirectly(self, user):
        for member in self.graph.get_info():
            if self.username in self.graph.get_info()[member] \
                    and member in self.graph.get_info()[user] \
                    and user != self.username:
                return True
        return False

    def who_follows_you_back(self):
        followers = [member for member in self.graph.get_info(
            ) if self.username in self.graph.get_info()[member]]
        followed_by_me = [user for user in self.graph.get_info()[self.username]]
        # Add if followed by me:
        result1 = [user for user in followers if user in followed_by_me]
        # Add if followed by someone I follow:
        result2 = [user for user in followers for followed in followed_by_me
                   if user in self.graph.get_info()[followed]]
        return list(set(result1 + result2))
