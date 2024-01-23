import game_core
import score_analysis

#Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for game_core_v3: ', end='')
score_analysis.score_game(game_core.game_core_v3)

print('Run benchmarking for game_core_v2: ', end='')
score_analysis.score_game(game_core.game_core_v2)