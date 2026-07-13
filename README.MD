# NeetCode Practice Solutions

*(Polski poniżej / Polish version below)*

## Overview

This repository is a personal collection of algorithm and data-structure solutions written in Python, based on the well-known [NeetCode](https://neetcode.io/) problem list (commonly referred to as the "NeetCode 150"). It is structured as a flat set of standalone Python scripts — one file per problem — rather than as an installable package or application.

There is no application entry point, web server, CLI, or build pipeline here: this is a study/reference repository for practicing coding-interview style problems.

## Przegląd

To repozytorium to prywatny zbiór rozwiązań algorytmicznych i strukturalnych napisanych w Pythonie, oparty na znanej liście zadań [NeetCode](https://neetcode.io/) (potocznie nazywanej "NeetCode 150"). Projekt jest zorganizowany jako płaski zestaw samodzielnych skryptów Python — jeden plik na jedno zadanie — a nie jako instalowalny pakiet czy aplikacja.

Nie ma tu punktu wejścia aplikacji, serwera, CLI ani pipeline'u budowania: to repozytorium ma charakter edukacyjny/referencyjny, służące do ćwiczenia zadań w stylu rozmów kwalifikacyjnych.

---

## Tech Stack & Requirements

- **Language:** Python 3 (no version pinned anywhere in the project; standard modern Python 3 syntax is used — f-strings are not used, but type hints, `collections.deque`, `collections.defaultdict`, and `heapq` from the standard library are).
- **Dependencies:** None. Every file relies exclusively on the Python standard library (`collections`, `heapq`). There is no `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile`, or any dependency-management file in the repository.
- **Package manager:** Not applicable — no packaging or dependency manifest exists.
- **Tests/CI:** No test suite (`pytest`, `unittest`, etc.) and no CI configuration (e.g. GitHub Actions) were found in the project.
- **License:** No `LICENSE` file was found in the repository, so no license is explicitly declared.

## Stos technologiczny i wymagania

- **Język:** Python 3 (żadna konkretna wersja nie jest wskazana w projekcie; używana jest standardowa nowoczesna składnia Python 3 — nie wykorzystano f-stringów, natomiast wykorzystano adnotacje ze standardowej biblioteki: `collections.deque`, `collections.defaultdict` oraz `heapq`).
- **Zależności:** Brak. Każdy plik korzysta wyłącznie z biblioteki standardowej Pythona (`collections`, `heapq`). W repozytorium nie ma pliku `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile` ani żadnego innego manifestu zależności.
- **Menedżer pakietów:** Nie dotyczy — nie istnieje żaden plik pakietowania ani manifest zależności.
- **Testy/CI:** Nie znaleziono zestawu testów (`pytest`, `unittest` itp.) ani konfiguracji CI (np. GitHub Actions) w projekcie.
- **Licencja:** W repozytorium nie znaleziono pliku `LICENSE`, więc licencja nie jest jawnie zadeklarowana.

---

## Project Structure

```
neetcode/
├── README.md
├── anagram.py                     # Valid Anagram
├── binary.py                      # Binary Search
├── bintreeleveltraversal.py       # Binary Tree Level Order Traversal
├── climbingstairs.py              # Climbing Stairs
├── combinationsum.py              # Combination Sum
├── containerwater.py              # Container With Most Water
├── containsdupes.py               # Contains Duplicate
├── courseschedule.py              # Course Schedule
├── courseschedule2.py             # Course Schedule II
├── groupanagram.py                # Group Anagrams
├── inverttree.py                  # Invert Binary Tree
├── kclosestpointoorigin.py        # K Closest Points to Origin
├── kthlargestelement.py           # Kth Largest Element in an Array
├── linkedcyclelist.py             # Linked List Cycle
├── longestpalindromicsubstring.py # Longest Palindromic Substring
├── longestrepeatingchar.py        # Longest Repeating Character Replacement
├── longestsubstring.py            # Longest Substring Without Repeating Characters
├── maxdepthbinarytree.py          # Maximum Depth of Binary Tree
├── mergelist.py                   # Merge Two Sorted Lists
├── minstack.py                    # Min Stack
├── numislands.py                  # Number of Islands
├── palindrome.py                  # Valid Palindrome
├── reverselinkedlist.py           # Reverse Linked List
├── rotatedsortedarray.py          # Search in Rotated Sorted Array
├── slidingwindow.py               # Best Time to Buy and Sell Stock
├── subsets.py                     # Subsets
├── threesum.py                    # 3Sum
├── topkelements.py                # Top K Frequent Elements
├── trie.py                        # Implement Trie (Prefix Tree)
├── twosum.py                      # Two Sum
├── twosumII.py                    # Two Sum II - Input Array Is Sorted
├── validparentheses.py            # Valid Parentheses
└── wordsearch.py                  # Word Search
```

Every problem lives in its own file at the repository root — there are no sub-packages, `__init__.py` files, or nested modules. The only generated artifact is a `__pycache__` directory created when the scripts are executed.

## Struktura projektu

```
neetcode/
├── README.md
├── anagram.py                     # Poprawny anagram
├── binary.py                      # Wyszukiwanie binarne
├── bintreeleveltraversal.py       # Przechodzenie drzewa binarnego poziomami
├── climbingstairs.py              # Wchodzenie po schodach
├── combinationsum.py              # Suma kombinacji
├── containerwater.py              # Pojemnik z największą ilością wody
├── containsdupes.py               # Wykrywanie duplikatów
├── courseschedule.py              # Harmonogram kursów
├── courseschedule2.py             # Harmonogram kursów II
├── groupanagram.py                # Grupowanie anagramów
├── inverttree.py                  # Odwracanie drzewa binarnego
├── kclosestpointoorigin.py        # K najbliższych punktów od początku układu
├── kthlargestelement.py           # K-ty największy element w tablicy
├── linkedcyclelist.py             # Wykrywanie cyklu w liście wiązanej
├── longestpalindromicsubstring.py # Najdłuższy podciąg będący palindromem
├── longestrepeatingchar.py        # Najdłuższa zamiana powtarzających się znaków
├── longestsubstring.py            # Najdłuższy podciąg bez powtarzających się znaków
├── maxdepthbinarytree.py          # Maksymalna głębokość drzewa binarnego
├── mergelist.py                   # Łączenie dwóch posortowanych list
├── minstack.py                    # Stos z minimum
├── numislands.py                  # Liczba wysp
├── palindrome.py                  # Poprawny palindrom
├── reverselinkedlist.py           # Odwracanie listy wiązanej
├── rotatedsortedarray.py          # Wyszukiwanie w obróconej posortowanej tablicy
├── slidingwindow.py               # Najlepszy czas na kupno i sprzedaż akcji
├── subsets.py                     # Podzbiory
├── threesum.py                    # Suma trzech liczb (3Sum)
├── topkelements.py                # K najczęściej występujących elementów
├── trie.py                        # Implementacja drzewa Trie
├── twosum.py                      # Suma dwóch liczb (Two Sum)
├── twosumII.py                    # Suma dwóch liczb II - tablica posortowana
├── validparentheses.py            # Poprawne nawiasy
└── wordsearch.py                  # Wyszukiwanie słów w planszy
```

Każde zadanie znajduje się w osobnym pliku w katalogu głównym repozytorium — nie ma tu żadnych podpakietów, plików `__init__.py` ani zagnieżdżonych modułów. Jedynym generowanym artefaktem jest katalog `__pycache__`, tworzony po uruchomieniu skryptów.

---

## Solutions by Category

The 33 solved problems are organized below by the classic NeetCode topic groupings, inferred directly from each algorithm's logic (the files themselves are not grouped into folders).

| Category | File | Problem |
|---|---|---|
| Arrays & Hashing | `containsdupes.py` | Contains Duplicate |
| Arrays & Hashing | `twosum.py` | Two Sum |
| Arrays & Hashing | `anagram.py` | Valid Anagram |
| Arrays & Hashing | `groupanagram.py` | Group Anagrams |
| Arrays & Hashing | `topkelements.py` | Top K Frequent Elements |
| Two Pointers | `palindrome.py` | Valid Palindrome |
| Two Pointers | `twosumII.py` | Two Sum II – Input Array Is Sorted |
| Two Pointers | `threesum.py` | 3Sum |
| Two Pointers | `containerwater.py` | Container With Most Water |
| Sliding Window | `slidingwindow.py` | Best Time to Buy and Sell Stock |
| Sliding Window | `longestsubstring.py` | Longest Substring Without Repeating Characters |
| Sliding Window | `longestrepeatingchar.py` | Longest Repeating Character Replacement |
| Stack | `validparentheses.py` | Valid Parentheses |
| Stack | `minstack.py` | Min Stack |
| Binary Search | `binary.py` | Binary Search |
| Binary Search | `rotatedsortedarray.py` | Search in Rotated Sorted Array |
| Linked List | `reverselinkedlist.py` | Reverse Linked List |
| Linked List | `mergelist.py` | Merge Two Sorted Lists |
| Linked List | `linkedcyclelist.py` | Linked List Cycle |
| Trees | `inverttree.py` | Invert Binary Tree |
| Trees | `maxdepthbinarytree.py` | Maximum Depth of Binary Tree |
| Trees | `bintreeleveltraversal.py` | Binary Tree Level Order Traversal |
| Tries | `trie.py` | Implement Trie (Prefix Tree) |
| Heap / Priority Queue | `kthlargestelement.py` | Kth Largest Element in an Array |
| Heap / Priority Queue | `kclosestpointoorigin.py` | K Closest Points to Origin |
| Backtracking | `subsets.py` | Subsets |
| Backtracking | `combinationsum.py` | Combination Sum |
| Backtracking | `wordsearch.py` | Word Search |
| Graphs | `numislands.py` | Number of Islands |
| Graphs | `courseschedule.py` | Course Schedule |
| Graphs | `courseschedule2.py` | Course Schedule II |
| 1-D Dynamic Programming | `climbingstairs.py` | Climbing Stairs |
| 1-D Dynamic Programming | `longestpalindromicsubstring.py` | Longest Palindromic Substring |

## Rozwiązania według kategorii

Poniżej 33 rozwiązane zadania są pogrupowane według klasycznych kategorii tematycznych NeetCode, wywnioskowanych bezpośrednio z logiki każdego algorytmu (same pliki nie są fizycznie pogrupowane w foldery).

| Kategoria | Plik | Zadanie |
|---|---|---|
| Tablice i haszowanie | `containsdupes.py` | Wykrywanie duplikatów |
| Tablice i haszowanie | `twosum.py` | Suma dwóch liczb |
| Tablice i haszowanie | `anagram.py` | Poprawny anagram |
| Tablice i haszowanie | `groupanagram.py` | Grupowanie anagramów |
| Tablice i haszowanie | `topkelements.py` | K najczęściej występujących elementów |
| Dwa wskaźniki | `palindrome.py` | Poprawny palindrom |
| Dwa wskaźniki | `twosumII.py` | Suma dwóch liczb II – tablica posortowana |
| Dwa wskaźniki | `threesum.py` | Suma trzech liczb (3Sum) |
| Dwa wskaźniki | `containerwater.py` | Pojemnik z największą ilością wody |
| Przesuwane okno | `slidingwindow.py` | Najlepszy czas na kupno i sprzedaż akcji |
| Przesuwane okno | `longestsubstring.py` | Najdłuższy podciąg bez powtarzających się znaków |
| Przesuwane okno | `longestrepeatingchar.py` | Najdłuższa zamiana powtarzających się znaków |
| Stos | `validparentheses.py` | Poprawne nawiasy |
| Stos | `minstack.py` | Stos z minimum |
| Wyszukiwanie binarne | `binary.py` | Wyszukiwanie binarne |
| Wyszukiwanie binarne | `rotatedsortedarray.py` | Wyszukiwanie w obróconej posortowanej tablicy |
| Lista wiązana | `reverselinkedlist.py` | Odwracanie listy wiązanej |
| Lista wiązana | `mergelist.py` | Łączenie dwóch posortowanych list |
| Lista wiązana | `linkedcyclelist.py` | Wykrywanie cyklu w liście wiązanej |
| Drzewa | `inverttree.py` | Odwracanie drzewa binarnego |
| Drzewa | `maxdepthbinarytree.py` | Maksymalna głębokość drzewa binarnego |
| Drzewa | `bintreeleveltraversal.py` | Przechodzenie drzewa binarnego poziomami |
| Trie | `trie.py` | Implementacja drzewa Trie |
| Kopiec / kolejka priorytetowa | `kthlargestelement.py` | K-ty największy element w tablicy |
| Kopiec / kolejka priorytetowa | `kclosestpointoorigin.py` | K najbliższych punktów od początku układu |
| Backtracking | `subsets.py` | Podzbiory |
| Backtracking | `combinationsum.py` | Suma kombinacji |
| Backtracking | `wordsearch.py` | Wyszukiwanie słów w planszy |
| Grafy | `numislands.py` | Liczba wysp |
| Grafy | `courseschedule.py` | Harmonogram kursów |
| Grafy | `courseschedule2.py` | Harmonogram kursów II |
| Programowanie dynamiczne 1D | `climbingstairs.py` | Wchodzenie po schodach |
| Programowanie dynamiczne 1D | `longestpalindromicsubstring.py` | Najdłuższy podciąg będący palindromem |

---

## How to Run

Each file is a standalone Python module. Since there is no packaging, entry point, or CLI, the intended way to use a solution is to either:

1. Run a file directly, for the handful of scripts that include an example call at the bottom of the file (e.g. `anagram.py`, `threesum.py`, `groupanagram.py`, `topkelements.py`):
   ```bash
   python3 anagram.py
   ```
2. Import the function/class into your own script or a REPL for files that only define a function or class without a runnable example (e.g. `twosum.py`, `binary.py`, `trie.py`):
   ```bash
   python3 -c "from twosum import twosum; print(twosum([2,7,11,15], 9))"
   ```

No installation step is required beyond having Python 3 available, since the project has zero third-party dependencies.

## Jak uruchomić

Każdy plik jest samodzielnym modułem Pythona. Ponieważ w projekcie nie ma pakietowania, punktu wejścia ani CLI, zamierzony sposób korzystania z rozwiązania to:

1. Uruchomienie pliku bezpośrednio — dotyczy garstki skryptów zawierających przykładowe wywołanie na końcu pliku (np. `anagram.py`, `threesum.py`, `groupanagram.py`, `topkelements.py`):
   ```bash
   python3 anagram.py
   ```
2. Zaimportowanie funkcji/klasy do własnego skryptu lub interaktywnej konsoli — dla plików, które definiują wyłącznie funkcję lub klasę bez przykładu wywołania (np. `twosum.py`, `binary.py`, `trie.py`):
   ```bash
   python3 -c "from twosum import twosum; print(twosum([2,7,11,15], 9))"
   ```

Nie jest wymagany żaden krok instalacyjny poza posiadaniem Pythona 3, ponieważ projekt nie ma żadnych zależności zewnętrznych.


