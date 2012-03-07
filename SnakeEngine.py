class square(object):
    state = '';
    def __init__(self, state):
        self.state = state
    def __repr__(self, *args, **kwargs):
        if self.state == 'SNAKE':
            return 'S'
        elif self.state == 'APPLE':
            return 'X'
        else:
            return 'U'
        
def move(board):