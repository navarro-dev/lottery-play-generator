import click
import random

@click.command()
@click.option('-g','--game', 'game', type=click.Choice(['MegaMillions', 'Powerball', 'Lotto']), required=True, help='Pick Lottery Game: MegaMillions, Powerball or Lotto')
@click.option('-p','--plays', 'plays', type=int, default=1, required=False, help='Pick number of plays')
def lotto(game, plays):
    
    print(f"------- {game} -------")
    print()
    for x in range(plays):
        print(f"------- Play {x+1}-------")
        if game == 'MegaMillions':
            playboard_numbers = random.sample(range(1, 71), 5)
            playboard_numbers.sort()
            mega_ball = random.sample(range(1, 26), 1)

            print('Playboard', end=':') 
            print(playboard_numbers)
            print('Mega Ball', end=':')
            print(mega_ball)

        elif game == 'Powerball':
            playboard_numbers = random.sample(range(1, 70), 5)
            playboard_numbers.sort()
            powerball = random.sample(range(1, 27), 1)

            print('Playboard', end=':') 
            print(playboard_numbers)
            print('Powerball', end=':')
            print(powerball)

        elif game == "Lotto":
            playboard_numbers = random.sample(range(1, 55), 6)
            playboard_numbers.sort()

            print('Playboard', end=':')
            print(playboard_numbers)
        print()

if __name__ == '__main__':
    lotto()