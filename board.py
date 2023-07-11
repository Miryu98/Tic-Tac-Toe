class Board: # Będzie zawierać logikę gry i przechowywać informacje o stanie planszy

    def __init__(self, player): # przyjmuje argument "player" określający który gracz rozpoczyna grę
        self.board = [[".", ".", "."], [".",".","."], [".",".","."]] # Tworzy planszę gry jako dwuwymiarową listę. Plansza ma rozmiar 3x3. Znak "." reprezentuje puste pole na planszy

        self.player = player # Przechowuje informację o aktualnym graczu

        self.win = False # Sprawdzenie, czy któryś z graczy wygrał grę. Na początku gry ustawione jest na False, ponieważ nikt jeszcze nie wygrał

# --------------------------------------------------------------------------------------------------------------------------

    def check_if_win(self):  #  Sprawdza, czy któryś z graczy wygrał grę

        for x in range(0,3): # Pętla iteruje po wartościach x od 0 do 2. Pętla sprawdza warunki zwycięstwa dla wierszy na planszy

            if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] and (self.board[x][2] == "X" or self.board[x][2] == "O"):
                self.win = True
                return True # Warunek ten sprawdza, czy wszystkie trzy pola w danym wierszu (o indeksie x) mają takie same wartości (również "X" lub "O"). Jeśli warunek ten jest spełniony, oznacza to, że gracz wygrał, więc zmienna self.win jest ustawiana na True, a metoda zwraca True, wskazując, że gra została wygrana

        for y in range(0,3): #  Pętla iteruje po wartościach y od 0 do 2. Ta pętla sprawdza warunki zwycięstwa dla kolumn na planszy

            if self.board[0][y] == self.board[1][y] and self.board[1][y] == self.board[2][y] and (self.board[2][y] == "X" or self.board[2][y] == "O"):
                self.win = True
                return True # Warunek ten sprawdza, czy wszystkie trzy pola w danej kolumnie (o indeksie y) mają takie same wartości (również "X" lub "O"). Jeśli warunek ten jest spełniony, oznacza to, że gracz wygrał, więc zmienna self.win jest ustawiana na True, a metoda zwraca True

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and (self.board[2][2] == "X" or self.board[2][2] == "O"):
            self.win = True
            return True # Warunek ten sprawdza, czy trzy pola na głównej przekątnej (indeksy [0][0], [1][1], [2][2]) mają taką samą wartość (również "X" lub "O"). Jeśli warunek ten jest spełniony, oznacza to, że gracz wygrał, więc zmienna self.win jest ustawiana na True, a metoda zwraca True

        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and (self.board[2][0] == "X" or self.board[2][0] == "O"):
            self.win = True
            return True # Warunek ten sprawdza, czy trzy pola na drugiej przekątnej (indeksy [0][2], [1][1], [2][0]) mają taką samą wartość (również "X" lub "O"). Jeśli warunek ten jest spełniony, oznacza to, że gracz wygrał, więc zmienna self.win jest ustawiana na True, a metoda zwraca True

        return False # Jeśli żaden z warunków zwycięstwa nie jest spełniony, oznacza to, że gra nie została wygrana, więc metoda zwraca False 
           
# --------------------------------------------------------------------------------------------------------------------------

    def check_if_draw(self): # Metoda  sprawdza, czy gra zakończyła się remisem poprzez sprawdzenie, czy istnieją jakieś puste pola na planszy. Jeśli wszystkie pola są wypełnione (brak pustych pól) i nie ma zwycięzcy, metoda zwraca True, co oznacza remis. W przeciwnym przypadku, gdy istnieje puste pole lub jest zwycięzca, metoda zwraca False

        if not self.check_if_win(): # Sprawda czy gra nie została wygrana poprzez wywołanie metody check_if_win(). Jeśli metoda check_if_win() zwraca False (czyli nikt nie wygrał), to warunek ten jest spełniony, co oznacza, że możemy sprawdzić, czy gra zakończyła się remisem

            for row in self.board: # Iteruje po wierszach planszy

                for element in row: # Iteruje po elementach w danym wierszu

                    if element == ".":
                        return False # sprawdza, czy dany element na planszy jest pustym polem (oznaczonym jako "."). Jeśli warunek ten jest spełniony, oznacza to, że istnieje przynajmniej jedno puste pole na planszy, co sugeruje, że gra nie zakończyła się remisem. W takim przypadku metoda zwraca False, oznaczając, że nie ma remisu
                    
            return True # Jeśli nie wystąpił warunek przy "if element == "."  " dla żadnego elementu na planszy, to oznacza, że nie ma żadnego pustego pola na planszy. W takim przypadku metoda zwraca True, co wskazuje, że gra zakończyła się remisem
        
        else: # Jeśli warunek "if not self.check_if_win():" nie jest spełniony (czyli gra została wygrana), to instrukcje w tym bloku zostaną wykonane
            
            return False # Jeśli gra została wygrana, to metoda zwraca False, co oznacza, że nie ma remisu
        
# --------------------------------------------------------------------------------------------------------------------------

    def show_board(self): # Metoda iteruje po planszy gry i wyświetla jej aktualny stan, wraz z numeracją kolumn i wierszy. Każdy element planszy jest wyświetlany w jednym wierszu, oddzielony od siebie spacjami. Po wyświetleniu całej planszy, metoda przejmuje nową linię, aby oddzielić planszę od innych elementów wyjścia

        print("  1 2 3") # Wyświetla nagłówki kolumn planszy, aby wskazać numerację kolumn jako "1", "2" i "3". Ta linia pojawia się na górze planszy

        numberRow = 1 # Ta zmienna będzie służyć do wyświetlania numerów wierszy planszy

        for row in self.board: # Iteruje po wierszach planszy

            print(numberRow, end = " ") # Wyświetla numer aktualnego wiersza, zakończony spacją. Numer wiersza jest wyświetlany przed wypisaniem zawartości tego wiersza

            for element in row: # Iteruje po elementach w danym wierszu

                print(element, end = " ") # Wyświetla zawartość aktualnego elementu planszy, zakończoną spacją. Każdy element planszy jest wyświetlany po numerze wiersza

            print()
            numberRow += 1 # Zwiększa wartość zmiennej "numberRow" o 1, aby przejść do kolejnego numeru wiersza

# --------------------------------------------------------------------------------------------------------------------------

    def check_if_free(self, x, y): # Metoda służy do sprawdzenia, czy pole na planszy o podanych współrzędnych (x, y) jest puste. Jeśli pole jest puste (wartość równa "."), metoda zwraca True, co oznacza, że pole jest wolne. W przeciwnym przypadku, gdy pole jest zajęte innym znakiem niż ".", metoda zwraca False, co oznacza, że pole nie jest wolne

        return self.board[x-1][y-1] == "." # Zwraca wartość logiczną True lub False, w zależności od tego, czy pole na planszy o podanych współrzędnych (x, y) jest puste (oznaczone jako "."). Wyrażenie self.board[x-1][y-1] odnosi się do konkretnego elementu planszy na pozycji [x-1][y-1], ponieważ indeksy listy są przesunięte o 1 w stosunku do współrzędnych planszy. Porównanie self.board[x-1][y-1] == "." sprawdza, czy wartość tego pola jest równa "." (czyli czy pole jest puste)
    
# --------------------------------------------------------------------------------------------------------------------------

    def change_player(self): # Metoda służy do zmiany gracza po każdym wykonanym ruchu. Jeśli aktualny gracz jest "O", metoda zmienia go na "X". W przeciwnym przypadku, gdy aktualny gracz nie jest "O" (czyli jest "X"), metoda zmienia go na "O". Dzięki temu metoda pozwala na cykliczną zmianę graczy w trakcie gry

        if self.player == "O": # Sprawdza czy aktualny gracz jest oznaczony jako "O"

            self.player = "X" #  Jeśli warunek wyżej jest spełniony, to oznacza, że aktualny gracz jest "O". W takim przypadku ustawiamy wartość zmiennej self.player na "X", co oznacza, że następny ruch należy do gracza "X"
        else:
            self.player = "O" # Następny ruch należy do gracza "O".

# --------------------------------------------------------------------------------------------------------------------------

    def put_to_board(self, x, y): # Metoda służy do umieszczenia znaku gracza na planszy w określonym miejscu. Jeśli pole jest wolne, metoda ustawia znak gracza na planszy na podanej pozycji, a następnie zmienia gracza, aby przekazać ruch drugiemu graczowi. Jeśli pole jest już zajęte, metoda nie wykonuje żadnych zmian na planszy

        if self.check_if_free(x, y): # Sprawdza, czy pole na planszy o współrzędnych (x, y) jest wolne, wywołując metodę "check_if_free(x, y)". Jeśli pole jest wolne, warunek ten jest spełniony, co oznacza, że można umieścić znak gracza na tym polu

            self.board[x-1][y-1] = self.player # Przypisanie wartości aktualnego gracza (self.player) do pola na planszy o współrzędnych [x-1][y-1]. Ponieważ indeksy listy są przesunięte o 1 w stosunku do współrzędnych planszy, musimy odjąć 1 od wartości x i y, aby uzyskać odpowiednie indeksy na planszy

            self.change_player() # Wywołanie metody change_player(), która zmienia aktualnego gracza na przeciwnika po umieszczeniu znaku na planszy

# --------------------------------------------------------------------------------------------------------------------------

    def get_player(self): # Metodą dostępowa (getter), która umożliwia uzyskanie informacji o aktualnym graczu. Można ją wywołać na obiekcie klasy Board, aby otrzymać wartość aktualnego gracza ("X" lub "O")

        return self.player # zwraca wartość zmiennej self.player, która reprezentuje aktualnego gracza
    
# --------------------------------------------------------------------------------------------------------------------------

    def return_board(self): # Metoda dostępowa (getter), która zwraca kopię aktualnego stanu planszy gry. Można ją wywołać na obiekcie klasy Board, aby uzyskać aktualną kopię planszy w formie dwuwymiarowej listy

        return self.board # Zwraca wartość zmiennej self.board, która przechowuje aktualny stan planszy