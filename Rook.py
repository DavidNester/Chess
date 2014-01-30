class Rook(ChessPiece):
    def __init__(self,color):
        super(Rook,self).__init__(self,Rook,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
        if not (super(Bishop,self).IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber)):
            return False
        if fromRow != toRow and fromCol != toCol:
                return False
            #horiz or vert?
            if fromRow == toRow:
                if abs(fromCol - toCol) == 1:
                    if board[toRow, toCol].ChessPiece == None:
                        return True
                    elif board[toRow, toCol].ChessPiece.PieceColor != turn:
                        return True
                    else:
                        return False

                    # C#: for (int i = 1; i <= Math.Abs(toCol - fromCol) - 1; i++)
                    for i in range(i,abs(toCol - fromCol) - 1):
                        if fromCol > toCol:
                            if board[fromRow, fromCol - i].ChessPiece != None:
                                return False
                        if fromCol < toCol:
                            if board[fromRow, fromCol+i].ChessPiece != None:
                                return False
                
             if fromCol == toCol:
                if abs(fromRow - toRow) == 1:
                        if board[toRow, toCol].ChessPiece == None:
                            return True
                        elif board[toRow, toCol].ChessPiece.PieceColor != turn:
                            return True
                        else:
                            return False
                    # C#: for (int i = 1; i <= Math.Abs(toRow - fromRow) - 1; i++)
                    for i in range(1,abs(toRow - fromRow) - 1):
                        if fromRow > toRow:
                            if board[fromRow-i, fromCol].ChessPiece != None:
                                return False
                        if fromCol < toCol:
                            if board[fromRow+i, fromCol].ChessPiece != None:
                                return False
                                
                if board[toRow, toCol].ChessPiece == None:
                    return True
                elif board[toRow, toCol].ChessPiece.PieceColor != turn:
                    return True
                else:
                    return False
