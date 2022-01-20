from game.die import Die


class Director:
    """
    Indidvual who directs the game for the player.

    Attributes:
        dice (List[die])
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """
        Creates a new Director.

        Args:
            self(Director): an instance of the Director.
        
        """
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)

    def start_game(self):
        """
        Starts the game by running the main game loop.

        Args:
            self(Director): an instance of Director.
        
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


    def get_inputs(self):
        """
        Asks user if they would like to roll.

        Args:
            self (Director): An instance of Director.
        
        """

        roll_dice = input('Roll Dice? (y/n)')
        self.is_playing = (roll_dice == 'y')

    def do_updates(self):
        """
        Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """

        if not self.is_playing:
            return

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points
        
        self.total_score += self.score

    def do_outputs(self):
        """
        Displays the results of the dice roll and score. Asks if the player would like to roll again.

        Args:
            self (Director): An instance of Director.
        """

        if not self.is_playing:
            return

        values = ''
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f'{die.value}'

        print(f'\nYou rolled: {values}\n')
        print(f'Your total score is: {self.total_score}')
        self.is_playing == (self.score > 0)






    

























