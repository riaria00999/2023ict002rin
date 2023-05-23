kings, queens, rooks, bishops, knights, pawns = map(int, input().split())

king = 1 - kings
queen = 1 - queens
rook = 2 - rooks
bishop = 2 - bishops
knight = 2 - knights
pawn = 8 - pawns

print(king, queen, rook, bishop, knight, pawn)
