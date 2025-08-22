A Python Selenium script to automate fetching **exam results**.  
It reads roll numbers from a CSV file, submits them on the official results portal, and retrieves data efficiently.  

---

## Features
- Reads hallticket/roll numbers from a CSV file.
- Automates form submission on the GRIET results portal.
- Fetches results without manual entry.
- Easy to run and customize.

---

## Requirements
- Python 3.8+
- Google Chrome
- ChromeDriver (auto-installed via `webdriver-manager`)

Install dependencies:
```bash
pip install selenium webdriver-manager
Usage
Clone the repo:
git clone https://github.com/your-username/griet-results-scraper.git
cd griet-results-scraper
Add roll numbers to a file named roll.csv:
320121001
320121002
320121003
Run the script:
python scraper.py
File Structure
.
├── scraper.py    # Main Selenium script
├── roll.csv      # Input file with roll numbers
└── README.md
Notes
The script opens the official results page for each roll number and submits it.
Add appropriate wait times if the server is slow.
Currently prints results; can be extended to save into CSV/Excel.
Disclaimer
This project is for educational and personal use only.

