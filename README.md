# Hangman Game

It's a game for all ages!

![Responsive](https://github.com/Adriele-lima/Hangman_Game/blob/main/images/responsive.jpg)

## Existing Features

- __Random word__

    - The game will start with a secret random word.

![Random-word](https://github.com/Adriele-lima/Hangman_Game/blob/main/images/start.jpg)

- __Guessing a correct word__

    - Player will guess a word and if it’s correct it will show the location of that word on the secret word.

![Correct-guess](https://github.com/Adriele-lima/Hangman_Game/blob/main/images/correct-word.jpg)

- __Guessing a wrong word__

    - Player will guess a word and if it’s not correct a part of the body will be hanged.

![Wrong-guess](https://github.com/Adriele-lima/Hangman_Game/blob/main/images/wrong-word.jpg)

- __Guessing an invalid word__

    - Player will guess a word and if it’s not an alphabetic word it will show an error.

![Invalid-guess](https://github.com/Adriele-lima/Hangman_Game/blob/main/images/invalid-word.jpg)

- __Winning the game__

    - Player will win when guessing all the letters in the word correctly.

![Winning](https://github.com/Adriele-lima/Hangman_Game/blob/main/images/win.jpg)

- __Losing the game__

    - Player will lose when failed to guess the correct word and all the parts of the body is hanged.

![Hangman](https://github.com/Adriele-lima/Hangman_Game/blob/main/images/hangman.jpg)

![Losing](https://github.com/Adriele-lima/Hangman_Game/blob/main/images/lose.jpg)

## Testing

I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed that are no problems.

- Given invalid inputs: numbers and wrong quantity of letters or adding the same value twice.

- Tested in my local terminal and on Heroku terminal. 

## Bugs

- __Solved Bugs__

    - When I deployed my project to Heroku I received an error because I forgot to use the Code Institute Template. After I changed all my code to a new file using the template I succeed with the deployment.

## Deployment

- On Heroku page:
    - Create a new app;
    - Create a name to your file “Must be unique” and select your region;
    - Setting the vars and add the building pack;
    - Select your project from Github on the deploy area;
    - After that it will give the link for the deployed game.

The deployed link can be found here [Hangman-Game]( https://hangmanpj3.herokuapp.com/)

## Credits

Th credits are for this video that helped me to create this game.

- [Youtube-Video]( (2) How to build HANGMAN with Python in 10 MINUTES - YouTube)