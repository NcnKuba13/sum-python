# sum-python
Rozwięcie projektu z programowania. Kod programu został przepisany z Javy do Pythona, skypty w języku Python są obsługiwane przez skrypt batch,
a raporty wynikowe są generowane w formacie HTML.

Suma ciągu jedynkowego jest to zadanie z I etapu V Olimpaiday Informatycznej z roku 1997/98. 
Ciąg liczbowy o wartościach będących liczbami całkowitymi nazywamy jedynkowym, 
jeżeli 2 dowolne jego sąsiednie wyrazy różnią się od siebie dokładnie o 1 oraz jego pierwszy wyraz jest równy 0.

## Funkcje plików
Skryptu "batch1_MENU.bat" zarządza wszystkimi dostepnymi procesami wykorzystując 2 skrypty powłoki Python - wyświetla w oknie konsoli wiersza poleceń "centralę".

<img src="https://github.com/NcnKuba13/sum-python/blob/main/screens/menu0.png" width="420">

<img src="https://github.com/NcnKuba13/sum-python/blob/main/screens/menu1.png" width="420">

<img src="https://github.com/NcnKuba13/sum-python/blob/main/screens/2git.png" width="420">

Skrypt "py1_SUM.py" odpowiada za generowanie ciągu. Po uruchomieniu pobiera z pliku 2 zmienne: n i S. 
Następnie sprawdza, czy wystąpiły błędy (czy zmienne są liczbami lub podane wartości mieszczą się w zadanych przedziałach).
Później wywołuje funkcję odpowiedzialną za utworzenie ciągu - najpierw sprawdza, czy łańcuch o zadanych n i S istnieje, 
a jeśli tak to zostaje on wygenerowany. Rezultat działania funkcji zapisywany jest do „ciag.txt”.

Skrypt "py2_HTML.py" pobiera dane otrzymane w wyniku działanie "py1_SUM.py" z plików tekstowych: "nciagu.txt", "Sciagu.txt" i "ciag.txt", 
a następnie na ich podstawie tworzy raport w formacie HTML, który segreguje uzyskane wartości w formie zestawienia. 
Gotowe raporty zapisywane są w folderze "raporty" pod aktualną datą.
