# BotWakacjePL
Bot przeglądający Wakacje.pl i zapisujący nazwy Hoteli oraz Ceny do pliku Excel.
Następnie sprawdza oceny zapisanych hoteli w Google.
Na koniec tworzy ranking hotelu na podstawie punktów przyznanych za cenę oraz ocenę.

Instrukcja krok po kroku:

ZANIM ZACZNIESZ:
1. Jeśli nie posiadasz przeglądarki Google Chrome, pobierz i zanstaluj ją: https://www.google.com/intl/pl_pl/chrome/
2. Pobierz i zainstaluj ChromeDrive dokładnie tej samej wersji, co Twoja Google Chrome https://googlechromelabs.github.io/chrome-for-testing/
4. Pobierz z nieniejszego repozytorium BotWakacjePL.exe i uruchom go na swoim Windowsie. 
5. Postępuj zgodnie z instrukcją w programie. 

USTAWIAMY BOTA
1. Utwórz wyszukiwanie na stronie Wakacje.pl. Ustaw skąd, dokąd, kiedy chcesz pojechać. Wyszukaj i przefiltruj hotele (panele wyników po lewej). Następnie przejdź do drugiej strony wyników i skopiuj pełny link z Twojej przeglądarki.
2. Wklej go do formularza programu BotWakacjePL.exe.
3. Wybierz, ile stron wyników chcesz przeanalizować.
4. Podaj lokalizację pobranej przeglądarki ChromeDriver.exe.
5. Podaj ścieżkę do folderu, gdzie mają się zapisać wyniki analiz.
6. Naciśnij "Start".
7. Śledź postępy automatycznego przeglądania internetu przez bota. W razie potrzeby, rozwiąż CAPCHA na stronie Google.
8. Uzyskasz plik execel z rankingiem hoteli przygotowanym na podstawie ich aktualnych cen i ocen.

Pobrane dane nadają się do dalszych analiz.
-----------------------------------------------
NOWOŚĆ W WERSJI 3.0
- plik exe kompatybilny z Windows,
- graficzny interface użytkownika,
- brak konieczność zmieniania kodu Python oraz instalowania tego środowiska,
- tworzenie rankingu hoteli na sumy punktów przyznanych za cenę i ocenę.

Jeśli chcesz rozwijać narzędzie? Proszę bardzo. 
Stworzyłem je na własny użytek i udostępniam za darmo.
