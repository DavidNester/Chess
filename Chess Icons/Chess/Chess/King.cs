using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Chess
{
    class King : ChessPiece
    {
        public King(ChessColors color)
            : base(ChessPieces.King, color, color == ChessColors.Black ? Properties.Resources.Black_King : Properties.Resources.White_King)
        {

        }
        public override bool IsValidMove(BoardSquare[,] board, int fromRow, int fromCol, int toRow, int toCol, ChessColors turn, int turnNumber)
        {
            if (!base.IsValidMove(board, fromRow, fromCol, toRow, toCol, turn, turnNumber))
                return false;
            if (Math.Abs(toRow - fromRow) > 1 || Math.Abs(toCol - fromCol) > 1)
            {
                return false;
            }
            else if (board[toRow, toCol].ChessPiece == null)
            {
                
                return true;
                
            }
            else if (board[toRow, toCol].ChessPiece.PieceColor != turn)
            {
             
                return true;

            }
            
            return false;
        }
    }
}
