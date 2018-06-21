**********************************

            BASHGAMMON

**********************************

	by Jordan Balk Schaer

BASHGAMMON is a Python/text version of the classic game Backgammon.  It is played with the rules that I know.  
There are two teams, represented as X and O.  O starts in the upper right side and X starts in the lower right.  X wants to move to its home board in the upper right and O wants to move to its home board in the lower right.  
If the two die rolled are equal (are doubles) then you have twice as many moves, otherwise you have the sum of the two rolls to move.
If a piece is alone, the opposing team can jump it and send it to jail.  If a piece is in jail, you cannot move until you first free your piece from jail.
The team that gets all of its pieces off of the board first wins.
Board sample:
								X HOME BOARD 	Freed:0
 -------------------------------------------------
|12  11  10  9   8   7  | | 6   5   4   3   2   1 |
|O               X      | | X                   O |
|O               X      | | X                   O |
|O               X      | | X                     |
|O                      | | X                     |
|O                      | | X                     |
 ------------------------------------------------- 
|X                      | | O                     |
|X                      | | O                     |
|X               O      | | O                     |
|X               O      | | O                   X |
|X               O      | | O                   X |
|13  14  15  16  17  18 | | 19  20  21  22  23  24|
 -------------------------------------------------
								O HOME BOARD 	Freed: 0

TO PLAY:
Type in two numbers, the first number is the position of the piece you want to move, and the second is the number of spots you want to move it by; for example, if you were O and you typed (1,6) you would move a piece at position 1 6 spots.
You can type 1,6 or 1 6 but you cannot type 16, the computer won't know what you mean by that.
You can undo one move by typing "u" or "undo" but you cannot undo more than the previous move.
You can finish your turn if you type "f" or "finish" or "d" or "done".  Your turn will finish automatically if you run out of moves.

Currently, you can only play player vs. player.  An update will come that will allow player vs. computer or even computer vs. computer if you're into that sort of thing.

Have fun!

