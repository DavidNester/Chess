
using System;
using System.Drawing;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Chess
{
    public enum ChessPieces { King, Queen, Bishop, Knight, Rook, Pawn }

    class ChessPiece
    {
        ChessPieces name;

        public ChessPieces Name
        {
            get { return name; }
        }
        ChessColors pieceColor;

        public ChessColors PieceColor
        {
            get { return pieceColor; }
        }
        public Image image;

        public Image Image
        {
            get { return image; }
        }
        
        public int lastMove;
        public int LastMove
        {
            get { return lastMove; }
            set { lastMove = value; }
        }
        public ChessPiece(ChessPieces name, ChessColors color, Icon icon)
        {
            this.name = name;
            this.pieceColor = color;
           
            this.lastMove = 0;
            image = (new Icon(icon, 48, 48)).ToBitmap();
        }
        private bool InRange(int value)
        {
            return 0 <= value && value < 8;
        }
        public virtual bool IsValidMove(BoardSquare[,] board, int fromRow, int fromCol, int toRow, int toCol, ChessColors turn, int turnNumber)
        {
            if (!(InRange(fromRow) && InRange(fromCol) && InRange(toRow) && InRange(toCol)))
                return false;
            else if (fromRow == toRow && fromCol == toCol)
                return false;
            else
                return true;
        }
    }
}
