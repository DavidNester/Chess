using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Chess
{
    class Bishop : ChessPiece
    {
        public Bishop(ChessColors color)
            : base(ChessPieces.Bishop, color, color == ChessColors.Black ? Properties.Resources.Black_Bishop : Properties.Resources.White_Bishop)
        {

        }
        public override bool IsValidMove(BoardSquare[,] board, int fromRow, int fromCol, int toRow, int toCol, ChessColors turn, int turnNumber)
        {
            if (!base.IsValidMove(board, fromRow, fromCol, toRow, toCol, turn, turnNumber))
                return false;
            if (toCol == fromCol || toRow == fromRow)
                return false;
            if (Math.Abs(fromRow - toRow) == Math.Abs(fromCol - toCol))
            {
		
                for (int i = 1; i < Math.Abs(fromRow-toRow); i++)
                {
			        if (fromRow> toRow && fromCol>toCol)
			        {
				        if (board[fromRow-i,fromCol-i].ChessPiece != null)
					        return false;
			        }
			        if (fromRow> toRow && fromCol<toCol)
			        {
			            if (board[fromRow-i,fromCol+i].ChessPiece != null)
					        return false;
			        }
			        if (fromRow<toRow && fromCol<toCol)
			        {
			            if (board[fromRow+i,fromCol+i].ChessPiece != null)
			                return false;
			        }
			        if (fromRow< toRow && fromCol>toCol)
			        {   
				        if (board[fromRow+i,fromCol-i].ChessPiece != null)
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
            //if absolute vaalue of (fromRow - toRow) == absolute value of (toRow - toCol) Math.Abs(----) 
        }
    }
}
