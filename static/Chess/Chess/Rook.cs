using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.Linq;
using System.Text;

namespace Chess
{
    class Rook : ChessPiece
    {
        public Rook(ChessColors color)
            : base(ChessPieces.Rook, color, color == ChessColors.Black ? Properties.Resources.Black_Rook : Properties.Resources.White_Rook)
        {

        }

        public override bool IsValidMove(BoardSquare[,] board, int fromRow, int fromCol, int toRow, int toCol, ChessColors turn, int turnNumber)
        {
            if (!base.IsValidMove(board, fromRow, fromCol, toRow, toCol, turn, turnNumber))
                return false;
            if (fromRow != toRow && fromCol != toCol)
                return false;
            //horiz or vert?
            if (fromRow == toRow ) 
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
                            if (board[fromRow, fromCol+i].ChessPiece != null)
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
                            if (board[fromRow-i, fromCol].ChessPiece != null)
                                return false;
                        }
                        if (fromCol < toCol)
                        {
                            if (board[fromRow+i, fromCol].ChessPiece != null)
                                return false;
                        }
                    }
                    
                }
                if (board[toRow, toCol].ChessPiece == null)
                    return true;
                else if (board[toRow, toCol].ChessPiece.PieceColor != turn)
                    return true;
                else
                    return false;
            //to Empty or OppColor
            //Math.Sign(----) +1, -1, 0
            
            
            //Castling
            //check?
            //1. Make move
            //2. Ask each opposing piece if it can move to king location
            //3. if all no --> commit , else --> undo
        }
    }
}
