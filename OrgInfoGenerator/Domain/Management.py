# coding=utf-8
class Management(object):
    """
    Management post and name
    """
    def __init__(self, management):
        if management is not None:
            self.name = management['name']
            if management['post'] is not None:
                self.post = management['post']
            else:
                self.post = 'Директор'
