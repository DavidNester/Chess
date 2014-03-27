using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

namespace Chess
{
    public partial class ChessForm : Form
    {
        BoardSquare[,] board;

        BoardSquare fromSq, toSq;

        ChessColors turn;
        
        int turnNumber = 1;
        int[] BlackKing = { 0, 3 };
        int[] WhiteKing = { 7, 4 };

        public ChessForm()
        {
            InitializeComponent();

            InitBoard();
        }

        private void InitBoard()
        {
            toSq = null;
            fromSq = null;
            board = new BoardSquare[8, 8];

            int width = panelChessBoard.Width/8;
            int height = panelChessBoard.Height/8;

            for (int row=0; row < 8; row++)
                for (int col = 0; col < 8; col++)
                {
                    board[row, col] = new BoardSquare(row, col, width, height);
                    panelChessBoard.Controls.Add(board[row, col]);
                    board[row, col].Click += new System.EventHandler(Square_Click);
                }
            
            board[0, 0].ChessPiece = new Rook(ChessColors.Black);
            board[0, 7].ChessPiece = new Rook(ChessColors.Black);

            board[7, 0].ChessPiece = new Rook(ChessColors.White);
            board[7, 7].ChessPiece = new Rook(ChessColors.White);

            board[0, 2].ChessPiece = new Bishop(ChessColors.Black);
            board[0, 5].ChessPiece = new Bishop(ChessColors.Black);

            board[7, 2].ChessPiece = new Bishop(ChessColors.White);
            board[7, 5].ChessPiece = new Bishop(ChessColors.White);

            board[0, 1].ChessPiece = new Knight(ChessColors.Black);
            board[0, 6].ChessPiece = new Knight(ChessColors.Black);

            board[7, 1].ChessPiece = new Knight(ChessColors.White);
            board[7, 6].ChessPiece = new Knight(ChessColors.White);

            board[0, 3].ChessPiece = new King(ChessColors.Black);
            board[7, 4].ChessPiece = new King(ChessColors.White);

            board[0, 4].ChessPiece = new Queen(ChessColors.Black);
            board[7, 3].ChessPiece = new Queen(ChessColors.White);

            
            for (int i = 0; i <= 7; i++)
                board[1, i].ChessPiece = new Pawn(ChessColors.Black);
            for (int i = 0; i <= 7; i++)
                board[6, i].ChessPiece = new Pawn(ChessColors.White);

            turn = ChessColors.White;
            label2.Text = turn.ToString();
            label2.Refresh();
            //board[0, 0].Image = (new Icon(Properties.Resources.Black_Rook, 48, 48)).ToBitmap();
        }



        private void Square_Click(object sender, EventArgs e)
        {
            BoardSquare sq = (BoardSquare)sender;

            //MessageBox.Show( string.Format("[{0},{1}]", sq.Row, sq.Col ) );
            if (sq.ChessPiece == null || sq.ChessPiece.PieceColor != turn)
            {
                // Deselect the previous selection?
                if (toSq != null && toSq != sq)
                    toSq.IsSelected = false;

                if (!sq.IsSelected)
                {
                    sq.IsSelected = true;
                    toSq = sq;
                }
                else
                {
                    sq.IsSelected = false;
                    toSq = null;
                }
            }
            else if (sq.ChessPiece.PieceColor == turn)
            {
                if (fromSq != null && fromSq != sq)
                    fromSq.IsSelected = false;

                if (!sq.IsSelected)
                {
                    sq.IsSelected = true;
                    fromSq = sq;
                }
                else
                {
                    sq.IsSelected = false;
                    fromSq = null;
                }
            }
        }

        private void btn_Click(object sender, EventArgs e)
        {
            if (toSq == null || fromSq == null)
            {
                MessageBox.Show("Must select to/from square");
            }
            else
            {
                if(fromSq.ChessPiece.IsValidMove(board, fromSq.Row, fromSq.Col, toSq.Row, toSq.Col, turn, turnNumber))
                {
                    if(board[fromSq.Row,fromSq.Col].ChessPiece.Name == ChessPieces.King)
                    {
                        if(board[fromSq.Row,fromSq.Col].ChessPiece.PieceColor == ChessColors.Black)
                        {
                            
                            	BlackKing[0] = toSq.Row;
                                BlackKing[1] = toSq.Col;
                                 
                        }
			        if(board[fromSq.Row,fromSq.Col].ChessPiece.PieceColor == ChessColors.White)
                        {
                            
				                WhiteKing[0] = toSq.Row;
                                WhiteKing[1] = toSq.Col;
                        }
                    }
                    bool enpassant = false;
                    ChessPiece tmp;
                    if (fromSq.ChessPiece.Name == ChessPieces.Pawn && toSq.ChessPiece == null && Math.Abs(toSq.Row - fromSq.Row) == Math.Abs(toSq.Col - fromSq.Col))
                    {
                        enpassant = true;
                        tmp = board[fromSq.Row, toSq.Col].ChessPiece;
                        toSq.ChessPiece = fromSq.ChessPiece;
                        fromSq.ChessPiece = null;
                        board[fromSq.Row, toSq.Col].ChessPiece = null;
                        
                    }
                    else
                    {
                        tmp = toSq.ChessPiece;
                        toSq.ChessPiece = fromSq.ChessPiece;
                        fromSq.ChessPiece = null;
                    }
		            bool check = false;
                    //MessageBox.Show("Valid");
                    for (int i = 0; i < 8; i++)
                    {
                        for (int j = 0; j < 8; j++)
                        {
                                if (board[i, j].ChessPiece == null) { }
                                else if (board[i, j].ChessPiece.PieceColor == ChessColors.Black) 
				                { 
				                    if (board[i, j].ChessPiece.IsValidMove(board, i, j, WhiteKing[0], WhiteKing[1], ChessColors.Black, turnNumber))
                                    {
					                    if(turn == ChessColors.Black)
						                    MessageBox.Show("Puts White King in Check");
					                    if(turn ==ChessColors.White)
					                    {
                                        	MessageBox.Show("Invalid: Puts king in check");
                                        	check = true;
					                    }
                                    }
				                }
                                else if (board[i, j].ChessPiece.PieceColor == ChessColors.White)
                                {
                                    if (board[i, j].ChessPiece.IsValidMove(board, i, j, BlackKing[0], BlackKing[1], ChessColors.White, turnNumber))
                                    {
					                    if(turn == ChessColors.White)
						                    MessageBox.Show("Puts Black King in Check");
					                    if(turn == ChessColors.Black)
					                    {
                                        	MessageBox.Show("Invalid: Puts king in check");
                                        	check = true;
					                    }
                                    }
                                }
                            }
                            

                        }
                    
		    if(!check)
		    {
                toSq.ChessPiece.LastMove = turnNumber;
                    	turnNumber++;
                    	if (turn == ChessColors.Black)
                        	turn = ChessColors.White;
                    	else
                        	turn = ChessColors.Black;
                    	label2.Text = turn.ToString();
                    	label2.Refresh();
		     }
		     else
            {
                if (enpassant)
                {
                    fromSq.ChessPiece = toSq.ChessPiece;
                    toSq.ChessPiece = null;
                    board[fromSq.Row, toSq.Col].ChessPiece = tmp;
                    enpassant = false;
                }
                else
                {
                    fromSq.ChessPiece = toSq.ChessPiece;
                    toSq.ChessPiece = tmp;
                }
                if (board[fromSq.Row, fromSq.Col].ChessPiece.Name == ChessPieces.King)
                {
                    if (board[fromSq.Row, fromSq.Col].ChessPiece.PieceColor == ChessColors.Black)
                    {
                        
                        BlackKing[0] = fromSq.Row;
                        BlackKing[1] = fromSq.Col;

                    }
                    if (board[fromSq.Row, fromSq.Col].ChessPiece.PieceColor == ChessColors.White)
                    {
                       
                        WhiteKing[0] = fromSq.Row;
                        WhiteKing[1] = fromSq.Col;
                    }
                }
                check = false;

            }
                }
                else
                {
                    MessageBox.Show("Not a Valid Move");
                }

            }
        }
    }
}
