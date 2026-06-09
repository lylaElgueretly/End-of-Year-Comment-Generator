# English Report Comment Generator

A Streamlit app for generating Year 7 English report comments within a 499-character limit.

## Features

- **Termly comments** — attitude, reading, and writing achievement with targets
- **End of year comments** — reflective, growth-focused language with Year 8 transition phrasing
- Optional attitude next steps field, appended before the closing sentence
- Correct pronoun handling for male, female, and gender-neutral students
- Download all generated comments as a Word document (.docx)

## Project Structure

```
├── app.py                 # Main Streamlit application
├── statements.py          # Termly statement banks (bands: 90–40)
├── eoy_statements.py      # End of year statement banks (bands: 100–30)
├── requirements.txt       # Python dependencies
└── .gitignore
```

## Installation

```bash
git clone https://github.com/your-username/english-report-generator.git
cd english-report-generator
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

## Band System

### Termly (statements.py)
Bands: `90, 85, 80, 75, 70, 65, 60, 55, 40`

### End of Year (eoy_statements.py)
Bands: `100, 90, 80, 70, 60, 50, 40, 30`

## Dependencies

- [Streamlit](https://streamlit.io/)
- [python-docx](https://python-docx.readthedocs.io/)

## Curriculum

Written for Year 7 English, British National Curriculum, with British spelling throughout.
