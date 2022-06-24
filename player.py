class Player(object):
    """Implements a player of the partner game withot any person"""
    def __init__(self,stones_per_win: int,win_numbers: list[int]) -> None:
        # set attributes
        self.stones=8
        self.stones_per_win=stones_per_win
        self.win_numbers=win_numbers
    def checkWin(self,number: int):
        # checks if the player won
        if number in self.win_numbers:
            # if yes, the method onWinning() will be called
            self.onWinning()
    def onWinning(self):
        # this is the method containing the action that happens when a player won
        self.stones-=self.stones_per_win
    def checkFinished(self):
        # this is a addition which checks if the player has 0 stones
        return self.stones==0