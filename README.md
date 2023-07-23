# Chess.com-Web-Scraper
Reads data from Chess.com for a given player through specified years and outputs a pandas dataframe with the following information:

* Info: Raw information from Chess.com for analysis

* PGN: The raw PGN from Chess.com including time  stamps

* Target_Color: The color your target player used, 1 for white.

* Target_Wins: 1 means the player searched won the game

* Variant Game: Boolean if the game is a  nonstandard variant or not

* Stripped PGN: The PGN of the game without time stamps

* FEN: This is a notation that notes the entire board state in a given position

* Matrix: This notation represents the board  state as a 9x8 matrix, negatives representing black pieces and each piece being represented by a number. The 9th row indicates move turn and etc. The goal was to create a way to export data for a Chess AI.
