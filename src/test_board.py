import unittest
from board import Game
from content import Players, Board


class BoardTest(unittest.TestCase):

    def setUp(self):
        """Initial Set Up"""
        self.game = Game()
        self.round_list = []
        self.winners_list = []

    def test_game_stats(self):
        """Returns the statistics:
        1- matches by time out
        2- average of turns
        3- percentage of gain by type of player
        4- which player wins the most"""

        #Simulation of 300 games
        for round_game in range(0,300):
            self.players = [
            {'impulsive':'player 1', 'balance':300, 'position':0},
            {'demanding':'player 2', 'balance':300, 'position':0},
            {'cautious':'player 3', 'balance':300, 'position':0},
            {'random':'player 4', 'balance':300, 'position':0},
            ]
            self.props =  [
            {'name':'São Paulo','owner':False,'price':100,'rent_value':60},
            {'name':'Osasco','owner':False,'price':95,'rent_value':59},
            {'name':'Barueri','owner':False,'price':90,'rent_value':58},
            {'name':'Carapicuiba','owner':False,'price':85,'rent_value':57},
            {'name':'Maceio','owner':False,'price':80,'rent_value':56},
            {'name':'Itapevi','owner':False,'price':75,'rent_value':55},
            {'name':'Manaus','owner':False,'price':70,'rent_value':40},
            {'name':'Porto Alegre','owner':False,'price':65,'rent_value':39},
            {'name':'Piraju','owner':False,'price':65,'rent_value':38},
            {'name':'Campinas','owner':False,'price':60,'rent_value':37},
            {'name':'Sorocaba','owner':False,'price':55,'rent_value':36},
            {'name':'Rio de Janeiro','owner':False,'price':50,'rent_value':35},
            {'name':'Taboão da Serra','owner':False,'price':45,'rent_value':20},
            {'name':'Niteroi','owner':False,'price':40,'rent_value':19},
            {'name':'Florianopolis','owner':False,'price':35,'rent_value':18},
            {'name':'Goiania','owner':False,'price':30,'rent_value':17},
            {'name':'Santana de Parnaiba','owner':False,'price':25,'rent_value':16},
            {'name':'Pirapora do Bom Jesus','owner':False,'price':20,'rent_value':15},
            {'name':'Mogi das Cruzes','owner':False,'price':15,'rent_value':10},
            {'name':'Grarulhos','owner':False,'price':10,'rent_value':9},
            ]

            round = self.game.start_game(self.players, self.props)

            self.round_list.append(round.get('round'))
            self.winners_list.append(round.get('winner'))


        #Statistics treatment
        timeout = len([round for round in self.round_list if round == 1000])
        round_average = sum(self.round_list) / 300
        impulsive = (100 / 300) * self.winners_list.count('impulsive')
        demanding = (100 / 300) * self.winners_list.count('demanding')
        cautious = (100 / 300) * self.winners_list.count('cautious')
        random = (100 / 300) * self.winners_list.count('random')
        no_winner = (100 / 300) * self.winners_list.count(False)

        count_winners_list = [impulsive, demanding, cautious, random]
        players_list = ['Impulsivo', 'Exigente', 'Cauteloso', 'Aleatório']
        biggest_winner_position = count_winners_list.index(max(count_winners_list))

        #Statistics prints
        print("Partidas por timeout: {:.2f}".format(timeout))
        print("Quantos turnos em média demora uma partida: {:.2f}".format(round_average))
        print("Qual a porcentagem de vitórias por comportamento dos jogadores: Impulsivo {:.2f}% - Exigente {:.2f}% - Cauteloso {:.2f}% - Aleatório {:.2f}%".format(impulsive, demanding, cautious, random))
        print("Qual o comportamento que mais vence: {}".format(players_list[biggest_winner_position]))

if __name__ == "__main__":
  unittest.main()
