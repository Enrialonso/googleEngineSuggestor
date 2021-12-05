## Another Google Suggest Search Scraper

This script use a Browser for get suggested search form a keyword, get the keyword and merge with a letters and stops words
Google return a suggested search and the script look this and store on an output file.

### Dependencies

- Python 3.8
- pip

Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### Run
- Before run
  - Set input file for words to search inside: `input/input.txt` (one word per line)
  - Install dependencies

```bash
python main.py
```

### Example Output

```text
elegir al azar
elegir asiento iberia
elegir aleatorio
elegir almohada
elegir al azar nombres
elegir aguacate
elegir asiento vueling
elegir aplicaciones predeterminadas por tipo de archivo
elegir asientos ryanair
elegir aleatoriamente de una lista
```