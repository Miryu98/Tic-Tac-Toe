import board as Board

print("Zacznijmy grę:")
player = input("Kto ma zacząć? X czy O: ")

board = Board.Board(player.upper()) # Tworzy obiekt klasy Board o nazwie board, używając wcześniej zdefiniowanej klasy Board. Przekazuje wartość player.upper() jako argument do konstruktora klasy Board, co tworzy planszę gry, zaczynając od gracza oznaczonego jako "X" lub "O"

while (not board.check_if_win()) and (not board.check_if_draw()): # Pętla wykonuje się, dopóki nie wystąpi zwycięstwo lub remis. Warunek pętli sprawdza, czy ani metoda check_if_win (sprawdzająca zwycięstwo), ani metoda check_if_draw (sprawdzająca remis) nie zwracają True

    board.show_board() # Wywołuje metodę show_board() na obiekcie board, aby wyświetlić aktualny stan planszy
    
    x, y = [int(x) for x in input("Podaj wspołrzędne pola na którym chcesz postawić X bądź O: ").split()] # Pobiera od użytkownika współrzędne pola, na którym chce postawić "X" lub "O". Użytkownik podaje dwie liczby oddzielone spacją, które są pobierane jako pojedyncze linie tekstu za pomocą funkcji input(). Następnie linia tekstu jest rozdzielana na dwie liczby za pomocą metody split(), a te liczby są konwertowane na typ int i przypisywane do zmiennych x i y przy użyciu składni listowej

    board.put_to_board(x, y) # Umieszcza "X" lub "O" na podanych współrzędnych na planszy

board.show_board() # Wyświetla aktualny stan planszy po wykonaniu ruchu
print()

if board.check_if_win(): # Sprawdza, czy gra została wygrana
    if board.get_player() == "X": # Warunek ten sprawdza, czy aktualny gracz jest "X", porównując go z wartością "X" zwróconą przez metodę get_player() na obiekcie board
        print("Wygrał 'O")
    else:
        print("Wygrał 'X'")
else:
    print("Remis - nikt nie wygrał.") # Wyświetla się wtedy, gdy warunek "if board.check_if_win()" nie zostanie spełniony