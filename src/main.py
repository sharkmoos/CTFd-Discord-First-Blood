#!/usr/bin/env python3
import logging
from time import sleep
from solve_handler import SolveHandler
import config


def main():
    """ 
    1. Use CTFd REST API to identify a first blood.
    2. Generate a message to send to Discord
    3. Send POST to Discord Web Hook
    Loop. Ad infinitum 
    """
    logging.basicConfig()
    # logging.getLogger().setLevel(logging.INFO)
    log = logging.getLogger()
    solve_handler = SolveHandler()

    while True:
        new_solves: dict = solve_handler.identify_first_bloods()
        for solve in new_solves:
            solve_message = solve_handler.generate_blood_message(solve, new_solves[solve])
            log.debug(solve_message)
            solve_handler.api.send_to_discord(solve_message)
            sleep(config.sleep_time)


if __name__ == "__main__":
    main()
