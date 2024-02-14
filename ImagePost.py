from Post import Post
# from matplotlib.image as mpimg


class ImagePost(Post):

    def __init__(self, image_name):
        self.image_name = image_name
        self.likers = []
        self.comments = []

    def __str__(self):
        return f"{self.user.name} posted a picture\n"

    @staticmethod
    def display():
        # image = mpimg.imread(self.image_name)
        # plt.imshow(image)
        # plt.axis('off')
        # plt.show()
        print("Shows picture")
