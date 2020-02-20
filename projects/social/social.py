import copy
import random

from util import Queue


class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
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

    def get_friends(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.friendships[vertex_id]

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
        for i in range(num_users):
            self.add_user(f"User {i + 1}")

        # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle the list
        random.shuffle(possible_friendships)
        # grab the 1st N friendship total_friendships pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        
        # avg_friendships = total_friendships/ num_users
        # total_friendships = avg_friendships * num_users
        # N = total_friendships // 2 (because each friendship creates 2 edges)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # loop over all of user_id's friends
        for i in sg.friendships[user_id]:
            
            # create an empty queue
            q = Queue()

            # add the starting vertex to the queue
            q.enqueue([user_id])

            # Create an empty set to store visited nodes
            visited_friends = set()

            # while queue is not empty:
            while q.size() > 0:
                # dequeue first vertex
                v = q.dequeue()
                # grab last vertex from path
                last_path = v[-1]
                # CHECK IF IT'S THE TARGET
                if last_path == i:
                    # IF SO, RETURN THE PATH
                    visited[i] = v
                # Check if it's been visited
                if last_path not in visited_friends:
                # If it has not been visited...
                    # Mark it as visited
                    visited_friends.add(last_path)
                # Then add A PATH TO all neighbors to the back of the queue
                for friend in self.get_friends(last_path):
                    v_copy = copy.copy(v)
                    v_copy.append(friend)
                    q.enqueue(v_copy)


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships[1])
    # connections = sg.get_all_social_paths(1)
    # print(connections)
    #print(sg.users)
    sg.get_all_social_paths(1)
