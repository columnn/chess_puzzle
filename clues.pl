clues(S) :-
    around(piece(queen,white), piece(pawn,white,one), S),               %1. Biała królowa sąsiaduje z polem, na którym stoi pierwszy biały pionek.
    edge(piece(bishop, black, one), S),                                 %2. Pierwszy czarny goniec znajduje się przy krawędzi szachownicy.
    f4(piece(pawn,white,two), S),                                       %3. Biały drugi pionek znajduje się na polu F4.
    capture(piece(rook, black, one), piece(rook, white, one), S),       %4. Pierwsza czarna wieża może bić pierwszą białą wieżę.
    capture(piece(pawn, white, three), piece(pawn, black, one), S),     %5. Trzeci biały pionek może bić pierwszego pionka.
    capture(piece(king,black), piece(queen,white), S),                  %6. Czarny król może bić królową.
    capture(piece(rook, white, one), piece(pawn, black, two), S),       %7. Pierwsza biała wieża może bić drugiego pionka.
    capture(piece(bishop, black, two), piece(rook, white, one), S),     %8. Drugi czarny goniec może bić pierwszą wieżę.
    capture(piece(bishop, white, one), piece(pawn, black, one), S),     %9. Pierwszy biały goniec może bić pierwszego pionka.
    capture(piece(king, white), piece(rook, black, one), S),            %10. Biały król może bić pierwszą wieżę.
    capture(piece(knight, black, two), piece(pawn, white, three), S),   %11. Pierwszy czarny skoczek może bić trzeciego pionka.
    capture(piece(pawn, black, two), piece(bishop, white, two), S),     %12. Drugi czarny pionek może bić drugiego gońca.
    capture(piece(bishop, black, one), piece(queen, white), S),         %13. Pierwszy czarny goniec może bić hetmana.
    capture(piece(bishop, white, two), piece(pawn, black, two), S),     %14. Drugi biały goniec może bić drugiego pionka.
    capture(piece(king, black), piece(bishop, white, two), S),          %15. Czarny król może bić drugiego gońca.
    capture(piece(rook, white, one), piece(rook, black, one), S),       %16. Pierwsza biała wieża może bić pierwszą wieżę.
    capture(piece(bishop, white, two), piece(king, black), S),          %17. Drugi biały goniec może bić króla.
    capture(piece(pawn, black, one), piece(pawn, white, three), S),     %18. Pierwszy czarny pionek może bić trzeciego pionka.
    capture(piece(pawn, black, one), piece(bishop, white, one), S),     %19. Pierwszy czarny pionek może bić pierwszego gońca.
    capture(piece(rook, black, one), piece(pawn, white, three), S).     %20. Pierwsza czarna wieża może bić trzeciego pionka.