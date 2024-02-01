import unittest
from main import determine_winner

class TestGame(unittest.TestCase):
    def test_rock_scissors(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'user')

    def test_rock_paper(self):
        self.assertEqual(determine_winner('rock', 'paper'), 'computer')

    def test_rock_rock(self):
        self.assertEqual(determine_winner('rock', 'rock'), 'tie')

    def test_rock_lizard(self):
        self.assertEqual(determine_winner('rock', 'lizard'), 'user')

    def test_rock_spock(self):
        self.assertEqual(determine_winner('rock', 'spock'), 'computer')

    def test_paper_rock(self):
        self.assertEqual(determine_winner('paper', 'rock'), 'user')

    def test_paper_scissors(self):
        self.assertEqual(determine_winner('paper', 'scissors'), 'computer')

    def test_paper_paper(self):
        self.assertEqual(determine_winner('paper', 'paper'), 'tie')

    def test_paper_lizard(self):
        self.assertEqual(determine_winner('paper', 'lizard'), 'computer')

    def test_paper_spock(self):
        self.assertEqual(determine_winner('paper', 'spock'), 'user')

    def test_scissors_paper(self):
        self.assertEqual(determine_winner('scissors', 'paper'), 'user')

    def test_scissors_rock(self):
        self.assertEqual(determine_winner('scissors', 'rock'), 'computer')

    def test_scissors_scissors(self):
        self.assertEqual(determine_winner('scissors', 'scissors'), 'tie')

    def test_scissors_lizard(self):
        self.assertEqual(determine_winner('scissors', 'lizard'), 'user')

    def test_scissors_spock(self):
        self.assertEqual(determine_winner('scissors', 'spock'), 'computer')

    def test_lizard_rock(self):
        self.assertEqual(determine_winner('lizard', 'rock'), 'computer')

    def test_lizard_paper(self):
        self.assertEqual(determine_winner('lizard', 'paper'), 'user')

    def test_lizard_scissors(self):
        self.assertEqual(determine_winner('lizard', 'scissors'), 'computer')

    def test_lizard_lizard(self):
        self.assertEqual(determine_winner('lizard', 'lizard'), 'tie')

    def test_lizard_spock(self):
        self.assertEqual(determine_winner('lizard', 'spock'), 'user')

    def test_spock_rock(self):
        self.assertEqual(determine_winner('spock', 'rock'), 'user')

    def test_spock_paper(self):
        self.assertEqual(determine_winner('spock', 'paper'), 'computer')

    def test_spock_scissors(self):
        self.assertEqual(determine_winner('spock', 'scissors'), 'user')

    def test_spock_lizard(self):
        self.assertEqual(determine_winner('spock', 'lizard'), 'computer')

    def test_spock_spock(self):
        self.assertEqual(determine_winner('spock', 'spock'), 'tie')

if __name__ == '__main__':
    unittest.main()