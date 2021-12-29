from mycroft import MycroftSkill, intent_file_handler


class FeedTheDog(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dog.the.feed.intent')
    def handle_dog_the_feed(self, message):
        self.speak_dialog('dog.the.feed')


def create_skill():
    return FeedTheDog()

