using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Chess
{
    class Queen : ChessPiece
    {
        public Queen(ChessColors color)
            : base(ChessPieces.Queen, color, color == ChessColors.Black ? Properties.Resources.Black_Queen : Properties.Resources.White_Queen)
        {

        }
        public override bool IsValidMove(BoardSquare[,] board, int fromRow, int fromCol, int toRow, int toCol, ChessColors turn, int turnNumber)
        {
            if (!base.IsValidMove(board, fromRow, fromCol, toRow, toCol, turn, turnNumber))
                return false;
            if (fromRow != toRow && fromCol != toCol && Math.Abs(fromRow - toRow) != Math.Abs(fromCol - toCol))
                return false;
            if (fromRow == toRow)
            {
                if (Math.Abs(fromCol - toCol) == 1)
                {
                    if (board[toRow, toCol].ChessPiece == null)
                        return true;
                    else if (board[toRow, toCol].ChessPiece.PieceColor != turn)
                        return true;
                    else
                        return false;
                }


                for (int i = 1; i <= Math.Abs(toCol - fromCol) - 1; i++)
                {
                    if (fromCol > toCol)
                    {
                        if (board[fromRow, fromCol - i].ChessPiece != null)
                            return false;
                    }
                    if (fromCol < toCol)
                    {
                        if (board[fromRow, fromCol + i].ChessPiece != null)
                            return false;
                    }
                }

            }
            if (fromCol == toCol)
            {
                if (Math.Abs(fromRow - toRow) == 1)
                {
                    if (board[toRow, toCol].ChessPiece == null)
                        return true;
                    else if (board[toRow, toCol].ChessPiece.PieceColor != turn)
                        return true;
                    else
                        return false;
                }
                for (int i = 1; i <= Math.Abs(toRow - fromRow) - 1; i++)
                {
                    if (fromRow > toRow)
                    {
                        if (board[fromRow - i, fromCol].ChessPiece != null)
                            return false;
                    }
                    if (fromRow < toRow)
                    {
                        if (board[fromRow + i, fromCol].ChessPiece != null)
                            return false;
                    }
                }

            }
            if (board[toRow, toCol].ChessPiece == null)
                return true;
            else if (board[toRow, toCol].ChessPiece.PieceColor != turn)
                return true;
            
            if (Math.Abs(fromRow - toRow) == Math.Abs(fromCol - toCol))
            {

                for (int i = 1; i < Math.Abs(fromRow - toRow); i++)
                {
                    if (fromRow > toRow && fromCol > toCol)
                    {
                        if (board[fromRow - i, fromCol - i].ChessPiece != null)
                            return false;
                    }
                    if (fromRow > toRow && fromCol < toCol)
                    {
                        if (board[fromRow - i, fromCol + i].ChessPiece != null)
                            return false;
                    }
                    if (fromRow < toRow && fromCol < toCol)
                    {
                        if (board[fromRow + i, fromCol + i].ChessPiece != null)
                            return false;
                    }
                    if (fromRow < toRow && fromCol > toCol)
                    {
                        if (board[fromRow + i, fromCol - i].ChessPiece != null)
                            return false;
                    }

                }
                if (board[toRow, toCol].ChessPiece == null)
                    return true;
                else if (board[toRow, toCol].ChessPiece.PieceColor != turn)
                    return true;
                else
                    return false;

            }
            else
                return false;
        }
    }
}
