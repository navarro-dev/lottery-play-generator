import click
import random

from rich.console import Console
from rich.table import Table

@click.command()
@click.option('-g','--game', 'game', type=click.Choice(['MegaMillions', 'Powerball', 'Lotto']), required=True, help='Pick Lottery Game: MegaMillions, Powerball or Lotto')
@click.option('-p','--plays', 'plays', type=int, default=1, required=False, help='Pick number of plays')
def lotto(game, plays):
    
    console = Console()

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column(game)
    table.add_column("Numbers", justify="right")

    if game == 'MegaMillions':
        table.add_column("Mega Ball", justify="right")

        for x in range(plays):
            playboard_numbers = random.sample(range(1, 71), 5)
            playboard_numbers.sort()
            mega_ball = random.sample(range(1, 26), 1)

            table.add_row(f"play {x+1}", " ".join(map(str,playboard_numbers)), f"[red]{mega_ball[0]}[/red]")
    
    elif game == 'Powerball':
        table.add_column(game, justify="right")

        for x in range(plays):
            playboard_numbers = random.sample(range(1, 70), 5)
            playboard_numbers.sort()
            powerball = random.sample(range(1, 27), 1)

            table.add_row(f"play {x+1}", " ".join(map(str,playboard_numbers)), f"[red]{powerball[0]}[/red]")
    
    elif game == 'Lotto':

        for x in range(plays):
            playboard_numbers = random.sample(range(1, 55), 6)
            playboard_numbers.sort()

            table.add_row(f"play {x+1}", " ".join(map(str,playboard_numbers)))

    console.print(table)

if __name__ == '__main__':
    lotto()