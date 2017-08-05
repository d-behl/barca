"""Information about FC Barcelona's games."""

from bs4 import BeautifulSoup
import click
import requests
from termcolor import colored, cprint


class RequestHandler:
    """Handles requests for getting the information.

    Gets information from the 'SkySports' website about the latest FCB 
    games (recent results, fixtures, and the current league table."""

    BASE_URL = "http://www.skysports.com/"

    def show_results(self, limit=5):
        """Shows recent FCB results."""
        url = self.BASE_URL + "barcelona-results"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        teams_box = soup.findAll("span", class_="swap-text__target")
        teams = [team.text.strip() for team in teams_box]
        del teams[0]  # Extra (unimportant) team name.
        limit = len(teams)

        scores_box = soup.findAll("span", class_="matches__teamscores-side")
        scores = [score.text.strip() for score in scores_box]

        dates_box = soup.findAll("h4", class_="fixres__header2")
        dates = [date.text.strip() for date in dates_box]

        competitions_box = soup.findAll("h5", class_="fixres__header3")
        competitions = [competition.text.strip()
                        for competition in competitions_box]

        for i in range(0, min(limit, len(teams)), 2):
            print("\n", colored(competitions[i // 2].upper(), "cyan", "on_white",
                                attrs=["reverse"]).center(88),
                  "\n", colored(dates[i // 2], "yellow").center(78),
                  "\n", colored(teams[i], "cyan").rjust(40) + "  "
                  + colored(scores[i] + " - " + scores[i + 1],
                            "red", attrs=["reverse"]) + "  "
                  + colored(teams[i + 1], "green") + "\n")

        cprint("\n\n*All dates stated according to BST.\n", "red")

    def show_fixtures(self, limit=5):
        """Shows recent FCB fixtures."""
        url = self.BASE_URL + "barcelona-fixtures"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        teams_box = soup.findAll("span", class_="swap-text__target")
        teams = [team.text.strip() for team in teams_box]
        del teams[0]  # Extra (unimportant) team name.

        dates_box = soup.findAll("h4", class_="fixres__header2")
        dates = [date.text.strip() for date in dates_box]

        competitions_box = soup.findAll("h5", class_="fixres__header3")
        competitions = [competition.text.strip()
                        for competition in competitions_box]

        time_box = soup.findAll("span", class_="matches__date")
        time = [timing.text.strip() for timing in time_box]

        for i in range(0, min(limit, len(teams)), 2):
            print("\n", colored(competitions[i // 2].upper(), "cyan", "on_white",
                                attrs=["reverse"]).center(88),
                  "\n", colored(dates[i // 2], "yellow").center(78),
                  "\n", colored(teams[i], "cyan").rjust(40)
                  + f"  {time[i//2]}  "
                  + colored(teams[i + 1], "green") + "\n")

        cprint("\n\n*All dates and kick-off times stated according to"
               " BST.\n", "red")


@click.command()
@click.option("--results", "-r", is_flag=True, help="Show recent resuts.")
@click.option("--fixtures", "-f", is_flag=True, help="Show upcoming fixtures.")
def main(results, fixtures):
    """FCB match details."""
    x = RequestHandler()

    if results:
        x.show_results()

    elif fixtures:
        x.show_fixtures()


if __name__ == "__main__":
    main()
