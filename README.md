# Demographic Data Analyzer

A Python-based data analysis project that analyzes demographic data from the 1994 Census database using Pandas.

## 📋 Project Overview

This project analyzes demographic data to answer key questions about age, education, salary, and occupation patterns. It uses the UCI Machine Learning Repository's adult dataset extracted from the 1994 Census database.

## 🎯 Analysis Questions

The project answers 9 key demographic questions:

1. **Race Distribution** - Count of people by race
2. **Average Age of Men** - Mean age of male population
3. **Bachelor's Degree Percentage** - Percentage of people with Bachelor's degree
4. **Advanced Education & Salary** - Percentage of advanced degree holders earning >$50K
5. **Non-Advanced Education & Salary** - Percentage without advanced degree earning >$50K
6. **Minimum Work Hours** - Minimum hours per week worked
7. **Minimum Hours & High Salary** - Percentage of minimum hours workers earning >$50K
8. **Highest Earning Country** - Country with highest percentage earning >$50K
9. **Top Occupation in India** - Most popular occupation for high earners in India

## 📊 Dataset

- **Source:** UCI Machine Learning Repository
- **Size:** 32,561 training records
- **Features:** 14 demographic and employment attributes
- **Target:** Salary classification (>50K or ≤50K)

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/KodsZn/Demographic-Data-Analyzer.git
cd Demographic-Data-Analyzer

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install pandas
```

### Running the Analysis

```bash
# Display analysis results
python demographic_data_analyzer.py

# Run unit tests
python main.py
```

## 📁 Project Structure

```
Demographic-Data-Analyzer/
├── demographic_data_analyzer.py  # Main analysis code
├── test_module.py               # Unit tests
├── main.py                      # Test runner
├── adult.data.csv               # Dataset
└── README.md                    # This file
```

## 🧪 Testing

All calculations are validated with unit tests:

```bash
python main.py
```

**Test Results:** ✅ 10/10 tests passing

## 📈 Sample Output

```
============================================================
DEMOGRAPHIC DATA ANALYSIS RESULTS
============================================================

1. Race Distribution:
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271

2. Average Age of Men: 39.4

3. Percentage with Bachelor's Degree: 16.4 %

4. Percentage with Advanced Education earning >50K: 46.5 %

5. Percentage WITHOUT Advanced Education earning >50K: 17.4 %

6. Minimum Hours Per Week: 1 hours

7. Percentage of Minimum Hours Workers earning >50K: 10.0 %

8. Country with Highest >50K Earning Percentage:
   Country: Iran
   Percentage: 41.9 %

9. Most Popular Occupation for >50K Earners in India: Prof-specialty
============================================================
```

## 💡 Key Features

- ✅ All decimals rounded to nearest tenth
- ✅ Clean, well-documented code
- ✅ Comprehensive unit test coverage
- ✅ Easy-to-read output formatting
- ✅ Efficient Pandas operations

## 📚 Technologies Used

- **Python 3.13**
- **Pandas** - Data manipulation and analysis
- **Unittest** - Test framework

## 📝 Data Source Citation

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science

Original data extraction: Barry Becker from the 1994 Census database

## ✨ Author

Created as a freeCodeCamp demographic data analysis challenge.

## 📄 License

This project is part of the freeCodeCamp curriculum.