
# coding: utf-8

# In[ ]:


# import modules
import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import socket
import json


# In[ ]:


# create credential variables
consumer_key = 'Reb5ziZMMLe1fAMDpkAYiBFNG'
consumer_secret = 'ZfXePZ4p1DjV0n5O0UTmVFzPMand3xfm1mApqfGDmcpwezAWwc'
access_token = '3284470063-LQ2tYbdwq7i18RJftmouDsm1Fpmch34MfCpy6D5'
access_secret = 'dqYTkWZeWTPysS9tfVJiajg6b4IQmFlJThNkyYdC0RLK2'


# In[ ]:


# create a class that listens to tweets

class TweetListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket
        
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print('Error', e)
        return True
    
    def on_error(self, status):
        print(status)
        return True


# In[ ]:


# create a function that operate on streamed data
def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetListener(c_socket))
    # set a filter to track tweets with a string in the filter set
    # twitter_stream.filter(track=['2018','HNY','Happy New Year','สวัสดีปีใหม่'])
    twitter_stream.filter(track=['#BNK48'])
    


# In[ ]:


if __name__ == '__main__':
    s = socket.socket()
    # set the host to be a localhost
    host = '127.0.0.1' 
    # set the connection port to be 5555
    port = 5555
    s.bind((host, port))
    
    print('listening on port:', port)
    
    s.listen()
    c, addr = s.accept()
    
    sendData(c)

