import config
from requests import Session, post, get
import json


class ApiSession(Session):
    # host: str
    def __init__(self):
        """
        Define the headers and concatenate the API endpoint.
        """
        super().__init__()
        self.headers.update({
            "Authorization": f"Token {config.api_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.host: str = config.host
        self.endpoint: str = self.host[:-1] + "/api/v1/" if (self.host[-1] == "/") else self.host + "/api/v1/"

    def get(self, url: str, params: any = None, **kwargs: any):
        """
        Versatile API requesting
        """
        url: str = self.endpoint + url
        return super().get(url, params=params, **kwargs)

    def get_solved_challenges(self) -> dict:
        """
        Query the challenges endpoint to identify challenges. 
        that have at least 1 solve.
        Returns a dictionary of solved challenges.
        """
        solved_challenges: dict = {}
        challenges: list = self.get("challenges").json()["data"]
        for challenge in challenges:
            # trying to parse data from hidden challenge throws errors
            if challenge["type"] == "hidden":
                continue
            elif challenge["solves"] <= 0:
                continue
            else:
                solved_challenges[challenge["id"]] = challenge
        return solved_challenges

    def get_challenge_solver(self, challenge_id: int) -> (bool, str):
        """ 
        For a given (solved) challenge, identify the solver.
        """
        challenge_solves = self.get(f"challenges/{challenge_id}/solves")

        if challenge_solves.status_code == 404:
            return False, "Challenge does not exist"
        elif challenge_solves.status_code == 200:
            return True, challenge_solves.json()["data"][0]["name"]
        else:
            return False, "Something went wrong"

    def send_to_discord(self, content: str) -> bool:
        data = json.loads(get(config.webhook_url).content.decode())
        data["content"] = content
        response = post(config.webhook_url, data=data, headers={})
        return True if response.status_code == 204 else False
