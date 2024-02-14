from ImagePost import ImagePost
from TextPost import TextPost
from Post import Post
from SalePost import SalePost

# this class represent a factory that match the type of the post to the correct constructor:
# using FACTORY design patterns

class PostFactory(Post):
    @staticmethod
    def create_post(post_type, *args, **kwargs):
        if post_type == "Text":
            return TextPost(*args)
        if post_type == "Image":
            return ImagePost(*args)
        elif post_type == "Sale":
            return SalePost(*args, **kwargs)
