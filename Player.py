import random
from scipy import stats

class player():
    def __init__(self, dices=None):
        self.dice_in_hand = []
        if dices is None:
            for i in range(5):
                self.dice_in_hand.append(random.randint(1,6))
        else:
            self.dice_in_hand = dices
    def choice(self,choice,num,point):
        if choice == 0:
            print('开')
        elif choice == 1:
            print('{:d}个{:d}'.format(num,point))
        else:
            print('error')
    def print_dice_in_hand(self):
        print(self.dice_in_hand)
    def technical_analysis(self,player_num,game_dice_num,game_point_chosen,is_one_out=False):
        dice_in_hand_point_count = [0,0,0,0,0,0]
        for dice in self.dice_in_hand:
            dice_in_hand_point_count[dice-1] += 1
        point_in_hand_max_count = dice_in_hand_point_count.index(max(dice_in_hand_point_count))+1
        if not is_one_out:
            one_in_hand_count = dice_in_hand_point_count[0]
            if point_in_hand_max_count == 1:
                # Choice 1: choose the point is next to 1
                temp_dice_in_hand_point_count = dice_in_hand_point_count.copy()
                temp_dice_in_hand_point_count[temp_dice_in_hand_point_count.index(max(temp_dice_in_hand_point_count))] = 0
                new_point_in_hand_max_count = temp_dice_in_hand_point_count.index(max(temp_dice_in_hand_point_count))+1
                dice_num_added = 1
                print('{:d}个{:d}'.format((game_dice_num) + dice_num_added,new_point_in_hand_max_count))
                print('{:.2%}'.format(round(1-stats.binom.cdf((game_dice_num-1) + dice_num_added - dice_in_hand_point_count[new_point_in_hand_max_count-1]-one_in_hand_count, (player_num-1) * dice_num_per_player, 2 / 6),4)))
                # Choice 2: choose 1 as the point
                print('{:d}个{:d}'.format((player_num),1))
                print('{:.2%}'.format(round(1-stats.binom.cdf((player_num-1)  - one_in_hand_count, (player_num-1) * dice_num_per_player, 1 / 6),4)))

            else:
                # Choice 1: add dice num while not changing dice point
                dice_num_added = 1
                print('{:d}个{:d}'.format((game_dice_num) + dice_num_added,game_point_chosen))
                # print('{:.2%}'.format(round(1-stats.binom.cdf((game_dice_num + dice_num_added - dice_in_hand_point_count[game_point_chosen-1]-one_in_hand_count) * 2 - 1, (player_num-1) * dice_num_per_player, 1 / 6),4)))
                print('{:.2%}'.format(round(1-stats.binom.cdf((game_dice_num-1) + dice_num_added - dice_in_hand_point_count[game_point_chosen-1]-one_in_hand_count, (player_num-1) * dice_num_per_player, 2 / 6),4)))

                # Choice 2: add dice num and change dice point
                dice_num_added = 1
                print('{:d}个{:d}'.format((game_dice_num) + dice_num_added,point_in_hand_max_count))
                print('{:.2%}'.format(round(1-stats.binom.cdf((game_dice_num-1) + dice_num_added - dice_in_hand_point_count[point_in_hand_max_count-1]-one_in_hand_count, (player_num-1) * dice_num_per_player, 2 / 6),4)))
        else:
            # Choice 1: add dice num while not changing dice point
            dice_num_added = 1
            print('{:d}个{:d}'.format((game_dice_num) + dice_num_added,game_point_chosen))
            print('{:.2%}'.format(round(1-stats.binom.cdf((game_dice_num-1) + dice_num_added - dice_in_hand_point_count[game_point_chosen-1], (player_num-1) * dice_num_per_player, 1 / 6),4)))

            # Choice 2: add dice num and change dice point
            dice_num_added = 1
            print('{:d}个{:d}'.format((game_dice_num) + dice_num_added,point_in_hand_max_count))
            print('{:.2%}'.format(round(1-stats.binom.cdf((game_dice_num-1) + dice_num_added - dice_in_hand_point_count[point_in_hand_max_count-1], (player_num-1) * dice_num_per_player, 1 / 6),4)))
