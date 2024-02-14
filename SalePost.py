from Post import Post


# this class represent a sale post, inheritance from Post class
class SalePost(Post):
    def __init__(self, product, price, place):
        self.product = product
        self.price = price
        self.place = place
        self.is_active = True
        self.likers = []
        self.comments = []

    # user can sell an item. he needs to give the password in order to do that
    def sold(self, password):
        if self.user.password == password:
            if self.is_active:
                self.is_active = False
                print(f"{self.user.name}'s product is sold")

    # user can make a discount on item. he needs to give the password and percentage in order to do that
    def discount(self, percentage, password):
        if self.user.password == password:
            self.price = ((100 - percentage) / 100) * self.price
            print(f"Discount on {self.user.name} product! the new price is: {self.price}")

    def __str__(self):
        print(f"{self.user.name} posted a product for sale:")
        if self.is_active:
            return f"For sale! {self.product}, price: {self.price}, pickup from: {self.place}\n"
        if not self.is_active:
            return f"Sold! {self.product}, price: {self.price}, pickup from: {self.place}\n"
