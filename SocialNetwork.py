from User import User


class SocialNetwork:
    _network = None

    # create a new Social Network
    # using "singleton" design patterns in order to create only one Social Network each program
    def __new__(cls, name):
        if cls._network is None:
            cls._users = {}
            cls._network = super(SocialNetwork, cls).__new__(cls)
            cls._network.__init__(name)
            cls.name = name
            print(f"The social network {name} was created!")
        return cls._network

    # this function sign up a new user to the network,
    # the new user need to give a name(that no already in the network) and a legal password
    def sign_up(self, name, password):
        if name not in self._users:  # make sure that the name is new
            if 8 > len(password) > 4:
                new_user = User(name, password)  # create new user
                self._users[name] = new_user  # add the user to the users list
                return new_user

    # this function log out the user:
    def log_out(self, name):
        if self._users.get(name).isConnected:  # check if the user is connected
            self._users.get(name).isConnected = False
            print(f"{name} disconnected")

    # this function log in the user, the user need to write his password in order to sign in:
    def log_in(self, name, password):
        if self._users.get(name).password == password:
            if not self._users.get(name).isConnected: # check if the user is connected
                self._users.get(name).isConnected = True
                print(f"{name} connected")

    def __str__(self):
        print(f"{self.name} social network:")
        for x in self._users:
            print(self._users.get(x))
        return ''
