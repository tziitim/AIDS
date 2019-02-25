#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool over = false;

void print_board(char board[3][3])
{
    cout<<"\n------------------\n";
    cout<<"\n  "<<board[0][0]<<"  |  "<<board[0][1]<< "  |  "<<board[0][2];
    cout<<"\n------------------\n";
    cout<<"\n  "<<board[1][0]<<"  |  "<<board[1][1]<< "  |  "<<board[1][2];
    cout<<"\n------------------\n";
    cout<<"\n  "<<board[2][0]<<"  |  "<<board[2][1]<< "  |  "<<board[2][2];
    cout<<"\n------------------\n";
}

bool checkForCorrectMove (char board[3][3], int choice, bool player1Turn)
{
    int xCor;
    int yCor;
    xCor = ((choice + 2) / 3) - 1; 
    yCor = (choice - 1) % 3;
    if (((board[xCor][yCor]) != 'X') && ((board[xCor][yCor]) != 'O'))
    {
        if (player1Turn)
            board[xCor][yCor] = 'X';
        if (!player1Turn)
            board[xCor][yCor] = 'O';
        return true;
    }
    else 
        return false;
}

bool checkRow(char board[3][3])
{
    for (int i = 0; i<3; i++)
    {
        if ((board[i][0] == board[i][1]) && (board[i][1] == board[i][2]))
        {
            return true;
        }
    }
    return false;
}
bool checkColumn (char board[3][3])
{
    for (int i = 0; i<3; i++)
    {
        if ((board[0][i] == board[1][i]) && (board[1][i] == board[2][i]))
        {
            return true;
        }
    }
    return false;
}
bool checkForWin (char board[3][3])
{
    bool win = false;
    bool line_win = false;
    if ((board[0][0] == board[1][1]) && (board[1][1] == board[2][2]))
    {
        win = true;
        return win;
    }
    if ((board[2][0] == board[1][1]) && (board[1][1] == board[0][2]))
    {
        win = true;
        return win;
    }

    if (checkColumn(board) || checkRow (board))
    {
        win = true;
        return win;
    }
    return win;
}

int main()
{
    cout << "Welcome to Tic Tac Toe!\n";
    int choice;
    int boardcounter = 1;
    bool isOkayToMove = true;
    bool player1Turn = true;
    char board[3][3];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            board[i][j] = boardcounter + '0';
            boardcounter++;
        }
    }
    print_board(board);
    do {
        if (player1Turn)
        {
            cout <<"\n\nPlayer 1, please enter a number that corresponds to an open space: ";
        }
        else
        {
            cout <<"\n\nPlayer 2, please enter a number that corresponds to an open space: ";
        }
        cin>>choice;
        isOkayToMove = checkForCorrectMove(board, choice, player1Turn);
        if (isOkayToMove)
        {
            over = checkForWin(board);
            print_board(board);
            player1Turn = !player1Turn;
        }
        else
        {
            cout <<"\n\nYou have attempted to move into a space that is already occupied, please try again.";
            print_board(board);
        }
    }
    while (over == false);
    cout <<"\n\nCongratulations!";
    player1Turn = !player1Turn;
    if (player1Turn)
        cout<<" Player 1 has won!";
    else
        cout<<" Player 2 has won!";
}

