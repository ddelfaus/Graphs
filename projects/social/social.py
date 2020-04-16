import random
from util import Stack, Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        count = 0
        count = count + 1
        print("added friends ", count)
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Write a for loop that calls create user the right amount of times

        for i in range(num_users):
            self.add_user(f"User {i+1}")
        # Hint 1: To create N random friendships, you could create a list with all possible friendship combinations
        # , shuffle the list, then grab the first N elements from the list.
        # You will need to import random to get shuffle.
        # Create friendships

        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        # create n friendships where n = avg_friendships * num_users// 2
        #avg_friendships = total_friendships / num_users
        #total_friendships = avg_friendships * num_users

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # implement BFS where id is the destination
        print("start of paths")
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        if user_id not in self.friendships:
            return visited
        qq = Queue()
        qq.enqueue([user_id])

        # While queue is not empty:
        while qq.size() > 0:
            # dequeue the first vertex
            path = qq.dequeue()
            v = path[-1]
            # check if it is visited
            # if not visited
            if v not in visited:

                visited[v] = path
            # enqueue all neighbors
                for friend in self.friendships[v]:

                    path_copy = path.copy()
                    path_copy.append(friend)
                    qq.enqueue(path_copy)

                # enqueue the copy

        return visited
    print("end of paths")


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 1)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
