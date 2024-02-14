from Post import Post


# this class represent a text post:
class TextPost(Post):

    def __init__(self, text):
        self.text = text
        self.likers = []
        self.comments = []

    def __str__(self):
        return self.user.name + " published a post:\n" f"\"{self.text}\"\n"
