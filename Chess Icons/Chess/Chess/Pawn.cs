using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Chess
{
    class Pawn : ChessPiece
    {
        public Pawn(ChessColors color)
            : base(ChessPieces.Pawn, color, color == ChessColors.Black ? Properties.Resources.Black_Pawn : Properties.Resources.White_Pawn)
        {

        }
        public override bool IsValidMove(BoardSquare[,] board, int fromRow, int fromCol, int toRow, int toCol, ChessColors turn, int turnNumber)
        {
            if (!base.IsValidMove(board, fromRow, fromCol, toRow, toCol, turn, turnNumber))
                return false;
            if (turn == ChessColors.Black)
            {
                if (fromRow > toRow)
                    return false;
            }
            if (turn == ChessColors.White)
            {
                if (fromRow < toRow)
                    return false;
            }

            if (board[toRow, toCol].ChessPiece == null)
            {
                if (Math.Abs(fromRow - toRow) == 1 && fromCol == toCol)
                    return true;
                //en passant implemented here
                else if (Math.Abs(fromRow - toRow) == 1 && Math.Abs(toCol - fromCol) == 1)
                {
                    if (board[fromRow, toCol].ChessPiece.Name == ChessPieces.Pawn &&board[fromRow, toCol].ChessPiece.PieceColor != turn && board[fromRow, toCol].ChessPiece.LastMove == turnNumber - 1)
                        return true;
                    else
                        return false;
                }
                else if (Math.Abs(fromRow - toRow) == 2 && toCol == fromCol)
                {
                    if (board[fromRow,fromCol].ChessPiece.LastMove == 0)
                        return true;
                    else
                        return false;
                }
                else
                    return false;
            }
            else if (board[toRow, toCol].ChessPiece != null)
            {
                if (board[toRow, toCol].ChessPiece.PieceColor != turn && Math.Abs(fromRow - toRow) == 1 && Math.Abs(toCol-fromCol) == 1)
                    return true;
                else
                    return false;
            }
            return false;
            
                    
        }
        
        //promotion
    }
}
