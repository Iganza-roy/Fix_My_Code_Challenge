#!/usr/bin/python3
"""
User class
"""


class User:
    """ Represent the user """

    def __init__(self):
        """ inititalizing the user class"""
        self.__email = None

    @property
    def email(self):
        """ getting the email """
        return self.__email

    @email.setter
    def email(self, value):
        """ setting the email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
