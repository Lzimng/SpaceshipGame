There are two programs in this repo. The program in SpaceshipGameClassic performs the same behavior as the demo, while the program in SpaceShipGame2D allows the spaceship to move in 2D space (left, right, up, and down) and display its trajectory. 

To run the program, nevigate to the SpaceshipGameClassic/SpaceShipGame2D, enter command:
 'python game.py -l 80  -h 30  -d easy' or 'python game.py --canvasLen 80  --canvasHig 30  --diff hard'

where,
-l/--canvasLen:    represents the length of the canvas, it is clipped in range [20, 120].
-h/--canvasHig:   represents the height of the canvas, it is clipped in range [20, 40].
-d/--diff:             represents the difficulty of the game, it can take 'easy', 'medium', or 'hard'.

Hope you enjoy it!