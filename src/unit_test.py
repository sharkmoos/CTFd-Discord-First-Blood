import pytest
from solve_handler import SolveHandler

solver = SolveHandler()


def test_solve_handler():

    assert type(solver.identify_first_bloods()) == dict
    solver.solved_challenges.pop(228)
    # print(solver.identify_first_bloods())
    assert solver.identify_first_bloods() == {'test_user': {'id': 228, 'type': 'standard', 'name': 'Test challenge', 'value': 0, 'solves': 1, 'solved_by_me': True, 'category': 'test', 'tags': [], 'template': '/plugins/challenges/assets/view.html', 'script': '/plugins/challenges/assets/view.js'}}
    
    solver.solved_challenges.pop(228)
    solver.solved_challenges.pop(156)

    assert len(solver.identify_first_bloods()) == 2


def test_api_handler():
    # A valid request should return set: bool & usernmame
    assert solver.api.get_challenge_solver(228) == (True, "test_user")
    
    # request to non existant challenge should return False and does not exist
    assert "exist" in solver.api.get_challenge_solver(0)[1]
    assert solver.api.get_challenge_solver(0)[0] is False


def test_discord_webhook():
    solver.solved_challenges.pop(228)
    new_solves = solver.identify_first_bloods()
    for solve in new_solves:

        solve_message = solver.generate_blood_message(solve, new_solves[solve])
        assert solver.api.send_to_discord(solve_message) is True
    
    solver.solved_challenges.pop(228)
    solver.solved_challenges.pop(156)
    new_solves = solver.identify_first_bloods()
    for solve in new_solves:

        solve_message = solver.generate_blood_message(solve, new_solves[solve])
        assert solver.api.send_to_discord(solve_message) is True
