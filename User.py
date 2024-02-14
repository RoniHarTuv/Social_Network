from PostFactory import *

# this class represen a User in the Social Network:
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.isConnected = True
        self.notifications = []
        self.followers = []
        self.posts = []

    # each user can follow other users
    def follow(self, user):
        user.followers.append(self)  # add the new follower to the list
        print(f"{self.name} started following {user.name}")

    # each user can unfollow other users
    def unfollow(self, user):
        if self in user.followers:
            user.followers.remove(self)  # remove the follower from the list
            print(f"{self.name} unfollowed {user.name}")

    # each user receive a notifications in 3 cases:
        # 1) someone like\comment on his post
        # 2) someone that he is followed after published a new post
    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for x in self.notifications:
            print(f"{x}")

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}"

    # each user can publis a post. there is 3 types of posts: test, image, sale.
    def publish_post(self, post_type, *args, **kwargs):
        if self.isConnected:
            new_post = PostFactory.create_post(post_type, *args, *kwargs)  # send the new post to postFactory in order to create the post
            new_post.set_user(self)
            self.posts.append(new_post)  # add the new post to the user posts
            for x in self.followers:  # send notifications to all my followers
                x.notifications.append(f"{self.name} has a new post")
            print(new_post.__str__())
            return new_post



