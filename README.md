# BotWakacjePL
Bot przeglądający Wakacje.pl i zapisujący nazwy Hoteli oraz Ceny do pliku Excel

Instrukcja krok po kroku:

ZANIM ZACZNIESZ:
1. Jeśli nie posiadasz przeglądarki Google Chrome, pobierz i zanstaluj ją: https://www.google.com/intl/pl_pl/chrome/
2. Pobierz i zainstaluj ChromeDrive https://googlechromelabs.github.io/chrome-for-testing/
4. Pobierz i zainstaluj Python: https://www.python.org/downloads/
5. Pobierz i zainstaluj edytor kodu w języku Python, IDE np. PyCharm Community Edition: https://www.jetbrains.com/pycharm/download/?section=windows
6. Pobierz plik BotWakacjePL.py z niniejszego repozytorium

USTAWIAMY BOTA
1. Otwórz plik BotWakacjePL.py by dostosować parametry kodu do Twojego działania (np. przy użyciu PyCharm Community Edition)
2. Jeżeli zainstalowany ChromeDrive znajduje się w innej lokalizacji niż C:\chromedriver-win64\chromedriver.exe, należy w kodzie zmienić ścieżkę prowadzącą do niego.
3. Wchodzimy na stronę Wakacje.pl i wybieramy skąd, dokąd chcemy lecieć, w jakim terminie, w ile osób. Możemy wybrać też inne opcje, np. All Inclusive. Dajemy szukaj.
4. Uzyskaną stronę z wynikami możemy filtrować oraz sortować (np. wg ceny).
5. Zjeżdżamy na dół strony i przechodzimy do drugiej strony wyników.
6. Kopiujemy z przeglądarki link do swoich wyników wyszukiwania.
7. Wklejamy go we wskazane miejsce pliku BotWakacjePL.py, podmieniając widniejący tam domyślnie link.
8. Zamieniamy nr strony będący w linku na {X}, np. fragment linku "wczasy/turcja/?str-2" powinniśmy zamienić na "wczasy/turcja/?str-{X}", jak w linku domyślnym.
9. Ustalamy, ile stron wyników ma przeglądać bot. Domyślnie jest 5. Możemy to zmienić.

URUCHAMIAMY BOTA
Uruchamiamy bota, wykonując kod BotWakacjePL.py, np. klikając zieloną ikonkę play w programie PyCharm. 
Bot przejrzy za nas strony z wynikami, pobierze nazwy hoteli, sprawdzi ich najniższe ceny i zapisze w pliku Excel, domyślnie hotels_data.xlsx.
Przy kolejnym uruchomieniu bot zaktualizuje ceny hotelu, które będzie można porównać z cenami wcześniejszymi.

Pobrane dane nadają się do dalszych analiz.


