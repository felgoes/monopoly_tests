# -*- coding: utf-8 -*-
import random

from content import Players, Board
from rules import Rules


class Game:
    def start_game(self, players, props):
        """Starts the game and calls the rules... return the winner"""
        #Set data on the content
        Players.players_dict = players
        Board.property_dict = props
        #Rounds loop (1000 rounds)
        for round in range(1, 1001):
            if not len(Players.players_dict) == 1:
                #Players loop
                for player_num, player in enumerate(Players.players_dict):
                    result_dice = self.rotate_dice()
                    position = Rules.round_board_count(player, result_dice)
                    #If the property already has an owner, it makes the rent payment rule
                    if Board.property_dict[position].get('owner') and Board.property_dict[position].get('owner') != str(next(iter(player))):
                        owner = [(i) for i in Players.players_dict if next(iter(i)) == Board.property_dict[position].get('owner')]
                        rent_result = Rules.rent_rule(player_num, player, owner, Board.property_dict[position].get('rent_value'))
                    #If the property does not have an owner, enter the purchase mechanism
                    elif player.get('balance') >= Board.property_dict[position].get('price'):
                        Rules.buy_rule(player, Board.property_dict[position])

            else:
                #Ends the game when only one player remains and returns the result with the winning player type and number of rounds
                game_stats = {'winner':next(iter(Players.players_dict[0])),'round':round}
                return game_stats
        #End the game if the number of rounds reaches its limit
        game_stats = {'winner':False,'round':1000}
        return game_stats

    def rotate_dice(self):
        """Mechanism for rolling the dice"""
        return random.randint(1, 6)
