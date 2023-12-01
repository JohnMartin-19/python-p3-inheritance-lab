#!/usr/bin/env python
#imported the class to be inherited
from user import User

class Student(User):
    def __init__(self, first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge =[]

    def learn(self,word):
        return self.knowledge.append(word)

        