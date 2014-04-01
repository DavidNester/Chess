using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Chess
{
    class Knight : ChessPiece
    {
        public Knight(ChessColors color)
            : base(ChessPieces.Knight, color, color == ChessColors.Black ? Properties.Resources.Black_Knight : Properties.Resources.White_Knight)
        {

        }
	public override bool IsValidMove(BoardSquare[,] board, int fromRow, int fromCol, int toRow, int toCol, ChessColors turn, int turnNumber)
        { 
        	if (!base.IsValidMove(board, fromRow, fromCol, toRow, toCol, turn, turnNumber))
                	return false;
        	if (Math.Abs(toRow-fromRow) > 2 || Math.Abs(toCol-fromCol) > 2 || toRow == fromRow || toCol == fromCol)
                	return false;
        	else if (Math.Abs(toRow-fromRow) == 2 && Math.Abs(toCol-fromCol) == 1)
		    {
            		if (board[toRow,toCol].ChessPiece == null)
                    {
                        
                        return true;

                    }	
			        else if(board[toRow,toCol].ChessPiece.PieceColor != turn)
                    {
                        
                        return true;

                    }
           	 	    else
                		return false;
		}	
        	else if(Math.Abs(toRow-fromRow) == 1 && Math.Abs(toCol-fromCol) == 2)
            {
			    if (board[toRow,toCol].ChessPiece == null)
                {
                    
                    return true;

                }
			    else if(board[toRow,toCol].ChessPiece.PieceColor != turn)
                {
                  
                    return true;

                }
           	 	else
                	return false;
		}
        	else 
	        	return false;
	


}

    }
}
