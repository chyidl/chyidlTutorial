# Snake AI 

## Neural Network 

Each snake contains a neural network. The neural network has an input layer of 24 neurons, a hidden layers of 18 neurons, and one output layer of 4 neurons.

## Vision 

The snake can see in 8 directions. In each of these directions the snake looks for 3 things:

1. Distance to food 
2. Distance to its own body 
3. Distance to a wall 

3 x 8 directions = 24 inputs. The 4 outputs are simply the directions the snake can move. 

## Natural Selection 

Each generation a population of 2000 snakes is created. For the first generation, all of the neural nets in each of the snakes are initialized randomly. Once the entire population is dead, a fitness score is calculated for each of the snakes. Using these fitness scores, some of the best snakes are selected to reproduce. In reprpduction two snakes are selected and the neural nets of each are crossed and then the resulting childing is mutated. This is repeated to create a new population of
2000 new snakes. 

## Fitness 

A snakes fitness is dependant on how long the snake stays as well as its score. However they are not equally important,having a higher score is rewarded more than a snake who simply stays alive. There is the possiblility however that a snake may evolve a strategy where it loops in a certain pattern and never dies. Even though hiving a high score is prioritzed more, if a snake can stay alive forever then that is a clear problem. To avoid this each snake is giving 200 starting moves at the
beginning of its life. Every time it eats a piece of food, it gains 100 more moves. This means that snakes who evolve to go in loops will eventually die, and snakes who go for the food will not only have higher score, but stay alive longer. 


