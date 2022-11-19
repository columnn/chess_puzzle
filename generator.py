import numpy as np
# f"capture(piece({},Color,N), Y, S) :- {}(piece({}, Color, N), S), {}(Y, S)."
pieces1 = ['rook','bishop', 'knight']

# f"capture(piece({},Color), Y, S) :- {}(piece({}, Color), S), {}(Y, S)."
pieces2 = ['king', 'queen']

# f"capture(piece(pawn,{}, N), Y, S) :- {}(piece(pawn, {}, N), S), {}(Y, S)."
pieces3 = ['white', 'black']

def generate_captures(fields, file):
    for field in fields:
        x, y = [*field]
        x = ord(x) - 97
        y = int(y) - 1
        
        #rook
        for i in range(8):
            if(i == x):
                continue
            a = f"{chr(i+97)}{y+1}"
            if a not in fields:
                continue
            s = f"capture(piece(rook,Color,N), Y, S) :- {field}(piece(rook, Color, N), S), {a}(Y, S).\n"
            file.write(s)
        for i in range(8):
            if(i == y):
                continue
            a = f"{chr(x+97)}{i+1}"
            if a not in fields:
                continue
            s = f"capture(piece(rook,Color,N), Y, S) :- {field}(piece(rook, Color, N), S), {a}(Y, S).\n"
            file.write(s)

        #bishop
        for i in range(1, 8):
            x2 = x+i
            y2 = y+i
            if (0 <= x2 <=7 and 0 <= y2 <=7):
                a = f"{chr(x2+97)}{y2+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(bishop,Color,N), Y, S) :- {field}(piece(bishop, Color, N), S), {a}(Y, S).\n"
                file.write(s)
            x2 = x+i
            y2 = y-i
            if (0 <= x2 <=7 and 0 <= y2 <=7):
                a = f"{chr(x2+97)}{y2+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(bishop,Color,N), Y, S) :- {field}(piece(bishop, Color, N), S), {a}(Y, S).\n"
                file.write(s)
            x2 = x-i
            y2 = y+i
            if (0 <= x2 <=7 and 0 <= y2 <=7):
                a = f"{chr(x2+97)}{y2+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(bishop,Color,N), Y, S) :- {field}(piece(bishop, Color, N), S), {a}(Y, S).\n"
                file.write(s)
            x2 = x-i
            y2 = y-i
            if(0 <= x2 <=7 and 0 <= y2 <=7):
                a = f"{chr(x2+97)}{y2+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(bishop,Color,N), Y, S) :- {field}(piece(bishop, Color, N), S), {a}(Y, S).\n"
                file.write(s)

        #king
        for i in range(3):
            for j in range(3):
                u = x+i-1
                v = y+j-1
                if not(0 <= u <= 7):
                    continue
                if not(0 <= v <= 7):
                    continue
                if (i==1 and j==1):
                    continue
                a = f"{chr(u+97)}{v+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(king,Color), Y, S) :- {field}(piece(king, Color), S), {a}(Y, S).\n"
                file.write(s)

        #knight
        q = [(2,-1),(2,1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2)]
        for i, j in q:
            u = x + i
            v = y + j
            pass
            if not(0 <= u <= 7):
                continue
            if not(0 <= v <= 7):
                continue
            a = f"{chr(u+97)}{v+1}"
            if a not in fields:
                continue
            s = f"capture(piece(knight,Color, N), Y, S) :- {field}(piece(knight, Color, N), S), {a}(Y, S).\n"
            file.write(s)
        
        #queen

        for i in range(8):
            if(i == x):
                continue
            a = f"{chr(i+97)}{y+1}"
            if a not in fields:
                continue
            s = f"capture(piece(queen,Color), Y, S) :- {field}(piece(queen, Color), S), {a}(Y, S).\n"
            file.write(s)
        for i in range(8):
            if(i == y):
                continue
            a = f"{chr(x+97)}{i+1}"
            if a not in fields:
                continue
            s = f"capture(piece(queen,Color), Y, S) :- {field}(piece(queen, Color), S), {a}(Y, S).\n"
            file.write(s)

        for i in range(1, 8):
            x2 = x+i
            y2 = y+i
            if (0 <= x2 <=7 and 0 <= y2 <=7):
                a = f"{chr(x2+97)}{y2+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(queen,Color), Y, S) :- {field}(piece(queen, Color), S), {a}(Y, S).\n"
                file.write(s)
            x2 = x+i
            y2 = y-i
            if (0 <= x2 <=7 and 0 <= y2 <=7):
                a = f"{chr(x2+97)}{y2+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(queen,Color), Y, S) :- {field}(piece(queen, Color), S), {a}(Y, S).\n"
                file.write(s)
            x2 = x-i
            y2 = y+i
            if (0 <= x2 <=7 and 0 <= y2 <=7):
                a = f"{chr(x2+97)}{y2+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(queen,Color), Y, S) :- {field}(piece(queen, Color), S), {a}(Y, S).\n"
                file.write(s)
            x2 = x-i
            y2 = y-i
            if(0 <= x2 <=7 and 0 <= y2 <=7):
                a = f"{chr(x2+97)}{y2+1}"
                if a not in fields:
                    continue
                s = f"capture(piece(queen,Color), Y, S) :- {field}(piece(queen, Color), S), {a}(Y, S).\n"
                file.write(s)
        #pawn
        
        q_white = [(1,-1),(1,1)]
        for i, j in q_white:
            u = x + i
            v = y + j
            pass
            if not(1 <= u <= 6):
                continue
            if not(1 <= v <= 6):
                continue
            a = f"{chr(u+97)}{v+1}"
            if a not in fields:
                continue
            s = f"capture(piece(pawn,white, N), Y, S) :- {field}(piece(pawn, white, N), S), {a}(Y, S).\n"
            file.write(s)
            
        q_black = [(-1,-1),(-1,1)]
        for i, j in q_black:
            u = x + i
            v = y + j
            pass
            if not(1 <= u <= 6):
                continue
            if not(1 <= v <= 6):
                continue
            a = f"{chr(u+97)}{v+1}"
            if a not in fields:
                continue
            s = f"capture(piece(pawn,black, N), Y, S) :- {field}(piece(pawn, black, N), S), {a}(Y, S).\n"
            file.write(s)

def generate_fields2(fields, file):
    for field in fields:
        x, y = [*field]
        x = abs(ord(x) - 104)
        y = int(y) - 1
        s = f"{field}(X, c("
        for i in range(8):
            for j in range(8):
                if(i==x and j==y):
                    s+="X,"
                else:
                    s+="_,"
            if(i == 7):
                s = s[:-1]
                s += ")).\n"
            else:
                s += '\n\t\t'
        file.write(s)
        
def generate_fields(file):
    for x in range(8):
        for y in range(8):
            s = f"{chr(x+97)}{y+1}(X, c("
            for i in range(8):
                for j in range(8):
                    if(i==x and j==y):
                        s+="X,"
                    else:
                        s+="_,"
                if(i == 7):
                    s = s[:-1]
                    s += ")).\n"
                else:
                    s += '\n\t\t'
            file.write(s)
        

def generate_arounds(fields, file):
    for field in fields:
        x, y = [*field]
        x = ord(x) - 97
        y = int(y) - 1
        for i in range(3):
            for j in range(3):
                u = x+i-1
                v = y+j-1
                if not(0 <= u <= 7):
                    continue
                if not(0 <= v <= 7):
                    continue
                if (i==1 and j==1):
                    continue
                a = f"{chr(u+97)}{v+1}"
                if a not in fields:
                    continue
                s = f"around(X, Y, S) :- {field}(X, S), {a}(Y, S).\n"
                file.write(s)

def generate_edges(fields, file):
    for field in fields:
        x, y = [*field]
        if(x == 'a' or x == 'h' or y == '1' or y == '8'):
            s = f"edge(X, S) :- {field}(X, S).\n"
            file.write(s)
            

def main():
    f = ['b5','b6','b7','c5','c6','c7','d4','d5','d6','d8','e5','e6','f4','f6','f7']

    file = open('predykaty.txt', 'w')

    generate_fields2(f, file)
    file.write('\n')

    generate_captures(f, file)
    file.write('\n')

    generate_edges(f, file)
    file.write('\n')

    generate_arounds(f, file)
    
    file.close()
    
    
if(__name__ == '__main__'):
    main()