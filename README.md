# CSF101-CAP2-CAP3-Tshewang_Dorji
*Description(How it works)
Imports and Set Up: The script imports necessary modules like unittest, pygame, and relevant classes (PlayerVehicle, Vehicle). It also includes MagicMock and patch from unittest.mock for mocking objects during testing.

Test Class: TestRetroHighwayGame is a subclass of unittest.TestCase, containing multiple test methods.

Test Cases:
test_player_vehicle_initialization: Checks the initial position of the player's vehicle.
test_vehicle_initialization: Tests the initialization and positioning of a generic vehicle object.
test_player_initial_position: Rechecks the player's initial position.
test_vehicle_creation: Validates the creation and placement of a vehicle.
test_collision_detection: Verifies collision detection between player and vehicle.
test_player_movement_left/right: Tests player movement left and right.
test_speed_increase: Assesses if game speed increases correctly after a certain score.
test_score_increment: Checks the score increment functionality.
test_exit_game_on_quit: Simulates game exit upon user input 'n'.
test_restart_game_on_quit: Simulates game restart upon 'y' input and a QUIT event.
Initialization and Tear Down:

setUpClass and tearDownClass handle the initialization and cleanup of the Pygame environment.
setUp and tearDown manage specific test setups and teardowns.
Execution: The script ensures that if executed directly, the tests will run using unittest.main().

This suite aims to thoroughly test various aspects of the game, from initializations and movements to collision handling, speed increments, user inputs for quitting and restarting the game, and scoring mechanisms.

The use of mock objects allows controlled testing by substituting certain game functionalities, ensuring specific scenarios are tested accurately without affecting the actual game environment. Overall, these tests help ensure the game functions as expected under different conditions and inputs.

*Resources used to developed this test:

unittest Framework: Python's built-in unittest library is utilized for writing and running the tests. It provides classes and methods to set up test cases, assertions, and fixtures.

Pygame Library: The game seems to be built using Pygame, a popular library for game development in Python. It provides functionalities for handling graphics, input events, and game logic. The tests involve Pygame-specific functionalities like event handling, collision detection, and object initialization.

Mocking with MagicMock and patch: The unittest.mock module is used for creating mock objects. MagicMock allows the creation of mock objects with "magical" methods and attributes that can manipulate during testing. patch is used to replace certain functionalities or objects with mocks, enabling control over their behavior.

Test Setup and Teardown Methods: The setUpClass, tearDownClass, setUp, and tearDown methods are part of the unittest framework and are used to initialize the testing environment before running test cases and clean up after their execution.

Assertions: The test cases contain assertions (self.assertEqual, self.assertTrue) to verify expected outcomes. These assertions check whether the actual results match the expected values.

To develop these tests, the primary resources include knowledge of Python's unittest framework, understanding Pygame's functionalities for game development, and familiarity with mocking techniques to control behaviors during testing.

Overall, the tests aim to validate various aspects of the game's functionality, such as object initialization, movement, collision detection, score increment, and user input handling, ensuring that the game behaves as intended under different scenarios.
