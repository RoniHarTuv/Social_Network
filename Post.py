from abc import ABC, abstractmethod


# this class represent a Post:
class Post(ABC):

    def __init__(self, user):
        self.user = user
        self.likers = []
        self.comments = []

    # each post had a owner
    def set_user(self, user):
        self.user = user

    # each post can be liked from a user
    def like(self, user_liker):
        if self.user is not user_liker:
            self.likers.append(user_liker) # add the user to the post "likers"
            print(f"notification to {self.user.name}: {user_liker.name} liked your post")
            self.user.notifications.append(f"{user_liker.name} liked your post")  # add to the posts user notifications

    # each post can get a comment from users:
    def comment(self, user_commenter, text):
        self.comments.append(user_commenter)
        print(f"notification to {self.user.name}: {user_commenter.name} commented on your post: {text}")  # send to the post owner
        self.user.notifications.append(f"{user_commenter.name} commented on your post")  # add to user notifications

    @abstractmethod
    def __str__(self):
        pass
