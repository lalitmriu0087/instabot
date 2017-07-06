from datetime import datetime
class Spy:


    def __init__(self,name,saluatation,age,rating):
        self.name = name
        self.salutation = saluatation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('Lalit', 'Mr.', 21, 4.7)

friend_one = Spy('Kunal', 'Mr.', 4.9, 22)
friend_two = Spy('Himanshu', 'Mr.', 4.39, 21)
friend_three = Spy('No', 'Hr.', 4.95, 24)

friends = [friend_one, friend_two, friend_three]
