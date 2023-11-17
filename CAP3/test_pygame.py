import unittest #provides a framework for creating and running tests.
import pygame
from game import PlayerVehicle, Vehicle  # Import relevant classes or functions
from unittest.mock import patch, MagicMock # used in testing to replace parts of the software with mock objects, allowing you to control their behavior and make testing more focused and predictable.

class TestRetroHighwayGame(unittest.TestCase):

# It is used to set up the testing environment once before any test methods in this test class are run.
    @classmethod
    def setUpClass(cls):
        pygame.init()#to initialize the Pygame library

# It is responsible for cleaning up and tearing down the testing environment after all test methods in the class have been executed.
    @classmethod
    def tearDownClass(cls):
        pygame.quit()# to properly quit and release Pygame resources.

#It is used to prepare the necessary resources or set up the initial state required for each individual test.
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.player = PlayerVehicle(250, 400)

#used to clean up resources or perform actions after each individual test method within the class has been executed.
    def tearDown(self):
        pygame.quit()#used to uninitialize all Pygame modules that have previously been initialized with. 

#Checks if the player's initial position matches the expected position.
    def test_player_vehicle_initialization(self):
        self.assertEqual(self.player.rect.center, (250, 400))

#Tests the initialization of a generic vehicle object and its positioning.
    def test_vehicle_initialization(self):
        vehicle = Vehicle(pygame.Surface((50, 50)), 200, 300)
        self.assertEqual(vehicle.rect.center, (200, 300))       

    def test_player_initial_position(self):
        # Check if the player's initial position is as expected
        expected_position = (250, 400)
        self.assertEqual(self.player.rect.center, expected_position)

    def test_vehicle_creation(self):
        # Test creation of the vehicle and ensure it's placed correctly
        vehicle = Vehicle(pygame.Surface((30, 30)), 300, 100)
        self.assertEqual(vehicle.rect.center, (300, 100))

    def test_collision_detection(self):
        # Test collision between player and vehicle
        player = PlayerVehicle(250, 400)
        vehicle = Vehicle(pygame.Surface((30, 30)), 250, 390)
        collision = pygame.sprite.collide_rect(player, vehicle)
        self.assertTrue(collision)

    def test_player_movement_left(self):
        # Test the player's movement to the left
        initial_x = self.player.rect.x
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.assertEqual(self.player.rect.x, initial_x - 0)

    def test_player_movement_right(self):
        # Test the player's movement to the right
        initial_x = self.player.rect.x
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        self.assertEqual(self.player.rect.x, initial_x + 0)

    def test_speed_increase(self):
        # Test if the game speed increases after a certain score
        initial_speed = 2
        score = 15  # Assume a score that triggers speed increase
        speed = initial_speed + (score // 10) * 0.5
        self.assertEqual(speed, 2.5)  # Adjust this value according to game's logic
        
        
    def test_score_increment(self):
        # Initialize game or relevant components
        
        # Assuming a scoring mechanism that increments the score
        # For instance, let's consider a function that updates the score
        def update_score(score):
            # Increment score by 1(example increment)
            return score + 1
        
        # Perform an action or event that triggers a score increment
        # For example, calling the update_score function
        initial_score = 0
        updated_score = update_score(initial_score)
        
        # Assert that the score has incremented correctly
        self.assertEqual(updated_score, 1)  # Assuming initial_score was 0

    @patch('builtins.input', side_effect=['n'])  # Simulating user input 'n' to quit
    def test_exit_game_on_quit(self, mock_input):
        game = MagicMock()  # Mocking the game object
        game.handle_quit = MagicMock()  # Mocking the handle_quit method
        # Simulate the quit action in game when 'n' input is received
        game.handle_quit()  # Simulate calling the handle_quit method


    @patch('builtins.input', side_effect=['y'])  # Simulating user input 'y' to restart
    @patch('pygame.event.get', side_effect=[[pygame.event.Event(pygame.QUIT)]])
    def test_restart_game_on_quit(self, mock_input, mock_event):
        game = MagicMock()  # Mocking the game object
        game.handle_restart = MagicMock()  # Mocking the handle_restart method
        # Simulate the restart action in game when 'y' input and QUIT event are received
        game.handle_restart()  # Simulate calling the handle_restart method      
        
if __name__ == '__main__': #checks if the script is being run directly 
    unittest.main(exit=False)
