import requests
from api_handler import API_Session 
import json
import logging
import config

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
log = logging.getLogger()

class Solve_Handler:
    # host: str
    
    def __init__(self):
        """
        - Establish the API session
        - Create a dictionary of solved challenges.
        """
        self.api = API_Session()
        self.solved_challenges = self.api.get_solved_challenges()
        log.debug(f"{len(self.solved_challenges)} challenges have been sovled")

    def identify_first_bloods(self) -> list:
        """
        - Query the CTFd challenge endpoint and compare the results 
        with the base dictionary
        - If new challenges have been solved, identify the solver(s) and
        return a list of them
        """
        solved_challenges = self.api.get_solved_challenges()
        new_solvers = {}

        while len(solved_challenges) > len(self.solved_challenges):
            # find which challenges are new
            for challenge in solved_challenges.keys():
                if challenge not in self.solved_challenges.keys():
                    # identify who solved the challenge
                    identified, solver = self.api.get_challenge_solver(challenge)
                    if identified:
                        new_solvers[solver] = solved_challenges[challenge]
                        # add the new challenge to the base scoreboard dict
                        self.solved_challenges[challenge] = solved_challenges[challenge]
                        log.debug(f"{solver} has got a first blood")
                    else:
                        log.warning(f"Something went wrong querying a solver. Error: {solver}")
                        return None
                else:   pass
        return new_solvers

    def generate_blood_message(self, user: str, challenge: dict) -> str:
        """
        Generate the message to be sent to Discord 
        """
        message =  f"🩸 Congrats to {user} for first blood on {challenge['name']} in the {challenge['category']} category"
        log.debug(message)
        return message

