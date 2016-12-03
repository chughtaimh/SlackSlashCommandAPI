import webapp2
import random


class Home(webapp2.RequestHandler):
    """A GET Request Handler"""

    def get(self):
        """Receives a GET request"""

        self.response.write('Hello, DevelopHerDevelopHim Viewers!')


class RockPaperScissors(webapp2.RequestHandler):
    """A POST Request Handler"""

    def post(self):
        """Receives a POST request"""

        move = self.request.get('text')
        play_rock_paper_scissors(move, self)


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

    handler.response.write(game.get(move).get(comp))




    # User picks rock
    if move == "rock":
        if comp == 'rock':
            self.response.write('I chose Rock too. We tie')
        elif comp == 1:
            self.response.write('I chose Paper. You Lose')
        else:
            self.response.write('I chose Scissors. You Win')

    # User picks paper
    elif move == "paper":
        if num == 1:
            self.response.write('I chose Paper too. We Tie')
        elif num == 2:
            self.response.write('I chose Scissors. You Lose')
        else:
            self.response.write('I chose Rock. You Win')

    # User picks scissors
    elif move == "scissors":
        if num == 2:
            self.response.write('I chose Scissors too. We Tie')
        elif num == 0:
            self.response.write('I chose Rock. You Lose')
        else:
            self.response.write('I chose Paper. You Win')

    # User put in an incorrect move
    else:
        self.response.write("{}is not a valid move.".format(move))


###############################################################
# An alterative way to handle logic that is more maintainable #
    # game = {
    #         "rock": {
    #                 1: "I chose Rock too. We Tie",
    #                 2: "I chose Paper. You Lose",
    #                 3: "I chose Scissors. You Win",
    #                 },
    #         "paper": {
    #                 1: "I chose Paper too. We Tie",
    #                 2: "I chose Scissors. You Lose",
    #                 3: "I chose Rock. You Win",
    #                 },
    #         "scissors": {
    #                 1: "I chose Scissors too. We Tie",
    #                 2: "I chose Rock. You Lose",
    #                 3: "I chose Paper. You Win",
    #                 },
    #         }
    # if move not in game.keys():
    #     self.response.write("{}is not a valid move.".format(move))

    # self.response.write(game.get(move).get(num))


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
