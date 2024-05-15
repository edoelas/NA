from Managers.GameDirector import GameDirector
from Bots import RandomBot, AlexPastorBot, EdoBot, AdrianHerasBot

bots_configs = [[RandomBot.RandomBot, AlexPastorBot.AlexPastorBot, EdoBot.EdoBot, AdrianHerasBot.AdrianHerasBot]]
games_to_play = 10


def main():
    for bots in bots_configs:
        game_director = GameDirector(bots = bots)
        victories = []
        for i in range(games_to_play):
            print('......')
            game_director.game_start(i + 1)
            last_round = list(game_director.trace_loader.current_trace["game"].values())[-1]
            last_turn = list(last_round.values())[-1]
            victories.append(list(last_turn["end_turn"]["victory_points"].values()))
        print('------------------------')
        print(victories)


    game_director.trace_loader.export_every_game_to_file()

    # print percentage of wins of each bot
    trace = game_director.trace_loader.all_games_trace
    


if __name__ == '__main__':
    main()
