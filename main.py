import webapp2
import random


class Home(webapp2.RequestHandler):
    """A GET Request Handler"""

    def get(self):
        """Receives a GET request"""

        self.response.write('Hello, Developers!')


class RockPaperScissors(webapp2.RequestHandler):
    """A POST Request Handler"""

    def post(self):
        """Receives a POST request"""

        move = self.request.get('text')
        play_rock_paper_scissors(move, handler=self)


def play_rock_paper_scissors(move, handler):
    """this plays rock paper scissors"""

    comp = random.choice(['rock', 'paper', 'scissors'])
    move = move.lower()

    game = {
            "rock": {
                    'rock'      : "I chose Rock too. We Tie",
                    'paper'     : "I chose Paper. You Lose",
                    'scissors'  : "I chose Scissors. You Win",
                    },
            "paper": {
                    'paper'     : "I chose Paper too. We Tie",
                    'scissors'  : "I chose Scissors. You Lose",
                    'rock'      : "I chose Rock. You Win",
                    },
            "scissors": {
                    'scissors'  : "I chose Scissors too. We Tie",
                    'rock'      : "I chose Rock. You Lose",
                    'paper'     : "I chose Paper. You Win",
                    },
        }

    if move not in game.keys():
        handler.response.write('{} is not a valid move'.format(move))
    else:
        handler.response.write(game.get(move).get(comp))


app = webapp2.WSGIApplication([
                        (r'/', Home),
                        (r'/rockpaperscissors', RockPaperScissors)
                        ],
                        debug=True)


def main():
    """Runs webservice"""

    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()
