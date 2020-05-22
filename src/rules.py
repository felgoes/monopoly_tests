# -*- coding: utf-8 -*-
import random

from content import Players, Board


class Rules:
    def buy_rule(player, prop_item):
        """Performs the property purchase transaction"""
        if next(iter(player)) == 'impulsive':
            player['balance'] -= prop_item['price']
            prop_item['owner'] = next(iter(player))
        if next(iter(player)) == 'demanding' and prop_item.get('rent_value') > 50:
            player['balance'] -= prop_item['price']
            prop_item['owner'] = next(iter(player))
        if next(iter(player)) == 'cautious' and prop_item.get('price') - player.get('balance') >= 80:
            player['balance'] -= prop_item['price']
            prop_item['owner'] = next(iter(player))
        if next(iter(player)) == 'random':
            random_boolean = bool(random.getrandbits(1))
            if random_boolean:
                player['balance'] -= prop_item['price']
                prop_item['owner'] = next(iter(player))

    def rent_rule(payer_num, payer, owner, rent_price):
        """Performs property rental payments"""
        if payer['balance'] - rent_price > 0:
            payer['balance'] -= rent_price
            owner[0]['balance'] += rent_price
        else:
            owner[0]['balance'] += payer['balance']
            payer['balance'] = 0
            Players.players_dict.pop(payer_num)
            for item in Board.property_dict:
                item['owner'] = False if item.get('owner') == next(iter(payer)) else item.get('owner')

    def round_board_count(player, resultado_dado):
        """Moving mechanism on the board"""
        position_sum = player.get('position') + resultado_dado
        if position_sum > 20:
            player['balance'] += 100
            player['position'] = position_sum - 21
            return player['position']
        else:
            player['position'] = position_sum
            return position_sum - 1
