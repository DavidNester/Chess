using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;


namespace Chess
{
    public enum ChessColors { Black, White }

    class BoardSquare : PictureBox
    {
        int row, col;

        public int Row 
        {
            get { return row; }
        }

        public int Col 
        {
            get { return col; }
        }

        ChessColors squareColor;

        public ChessColors SquareColor
        {
            get { return squareColor; }
        }
        ChessPiece chessPiece;

        bool selected;

        public bool IsSelected
        {
            get { return selected; }
            set 
            { 
                selected = value;
                this.Refresh();
            }
        }

        public ChessPiece ChessPiece
        {
            get { return chessPiece; }
            set 
            {
                chessPiece = value;

                if (value != null)
                    this.Image = chessPiece.Image;
                else
                    this.Image = null;
            }
        }

        public BoardSquare(int row, int col, int width, int height)
        {
            this.row = row;
            this.col = col;

            this.Location = new Point(col * width, row * height);
            this.Size = new Size(width, height);

            squareColor = (row + col) % 2 == 0 ? ChessColors.Black : ChessColors.White;

            this.BackColor = squareColor == ChessColors.Black ? Color.Black : Color.White;

            this.SizeMode = PictureBoxSizeMode.CenterImage;
            chessPiece = null;
        }
        protected override void OnPaint(PaintEventArgs pe)
        {
            base.OnPaint(pe);
            if (selected)
                ControlPaint.DrawBorder(pe.Graphics, pe.ClipRectangle, Color.Red, ButtonBorderStyle.Solid);
        }
    }
}
