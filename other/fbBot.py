from fbchat.models import *
import time
from fbchat import log, Client
import getpass

f = open('badword.txt', 'r')
l = f.read().split('\n')

class ResponseBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        s = message_object.text

        for i in l:
            if len(i) > 0 and i in s and author_id != self.uid:
                print(i)
                self.sendRemoteImage('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/MUTCD_R1-1.svg/2000px-MUTCD_R1-1.svg.png', message=Message(text='That was offensive! Please choose other word choice!'), thread_id=thread_id, thread_type=thread_type)

email = input("Please enter your FaceBook email.\n")
client = ResponseBot(email, getpass.getpass())
client.listen()
