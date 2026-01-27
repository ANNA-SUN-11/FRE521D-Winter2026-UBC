# FRE 521D: Data Analytics in Climate, Food and Environment

[![Course](https://img.shields.io/badge/Course-FRE%20521D-002145)](https://github.com/aaneloy/FRE521D-Winter2026-UBC)
[![Term](https://img.shields.io/badge/Term-Winter%202026-0055B7)](https://github.com/aaneloy/FRE521D-Winter2026-UBC)
[![Institution](https://img.shields.io/badge/Institution-UBC-0055B7)](https://www.ubc.ca/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**University of British Columbia**  
**Master of Food and Resource Economics (MFRE)**  
**Winter 2026**

---

## Course Information

| | |
|---|---|
| **Instructor** | Asif Ahmed Neloy |
| **Program** | UBC Master of Food and Resource Economics |
| **Class Times** | Monday & Wednesday, 12:30 - 2:00 PM |
| **Term** | Winter 2026 (January 5 - February 11) |

---

## Course Description

This course provides graduate students with practical data analytics skills essential for analyzing climate, food, and environmental data. Students will learn to build data pipelines, write SQL queries, wrangle data with Python, and create compelling visualizations. The course emphasizes real-world applications through hands-on assignments and a scaffolded group project.

---

## Getting Started

### Prerequisites

Before starting the course, ensure you have the following software installed:

| Software | Download Link |
|----------|---------------|
| Anaconda | [anaconda.com/download](https://www.anaconda.com/download) |
| Git | [git-scm.com](https://git-scm.com/) |
| VS Code | [code.visualstudio.com](https://code.visualstudio.com/) |
| Docker Desktop | [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) |
| DBeaver | [dbeaver.io/download](https://dbeaver.io/download/) |
| Postman | [postman.com/downloads](https://www.postman.com/downloads/) |

> **Note:** See the **Installation Guide** in the course materials for detailed setup instructions.

---

## Course Schedule

| Week | Date | Topic | Deliverables |
|------|------|-------|--------------|
| 1 | Jan 5 | Introduction & SQL Basics | A-1 Released |
| 1 | Jan 7 | SQL Refresher - Joins, CTEs, Window Functions | Final Project Released |
| 2 | Jan 12 | ETL Pipeline I - CSV/JSON Ingest | Lab-1 Released |
| 2 | Jan 14 | ETL Pipeline II - APIs & Automation | A-2 Released |
| 3 | Jan 19 | ETL Tools - BigQuery | **Quiz 1**, ~~A-1 Due~~ |
| 3 | Jan 21 | Python Wrangling I - Tidy Data, Types, Validation | |
| 4 | Jan 26 | Python Wrangling II - Merges, Pivots, Analysis-Ready Tables | |
| 4 | Jan 28 | ETL Tools - BigQuery & Automation | **Quiz 2** |
| 5 | Feb 2 | Data Cleaning I - Formats, Dates, Strings | **A-2 Due** |
| 5 | Feb 4 | Data Cleaning II - Outliers & Validation | |
| 6 | Feb 9 | Visualization I - Matplotlib & Plotly | **Quiz 3** |
| 6 | Feb 11 | Final Presentations | **Final Project Due** |

---

## Lecture Materials

### Lecture 1: Introduction to Databases and SQL (Jan 5)
- Course overview and tools setup
- Database fundamentals (SQL vs NoSQL)
- MySQL with Docker
- Basic SQL: CREATE, INSERT, SELECT, UPDATE, DELETE
- Filtering and sorting data

### Lecture 2: SQL Refresher (Jan 7)
- Loading CSV data into MySQL
- SQL JOINs (INNER, LEFT, RIGHT, CROSS, SELF)
- Common Table Expressions (CTEs)
- Window Functions (ROW_NUMBER, RANK, LAG, LEAD)
- Data Contracts and validation

### Lecture 3: ETL Pipeline I - Files and Foundations (Jan 12)
- What is ETL? Extract, Transform, Load
- Working with CSV files (pandas, validation)
- Working with JSON files (nested structures, flattening)
- Raw vs Cleaned data layers
- Data lineage and documentation
- Logging for ETL pipelines
- Complete file-based ETL pipeline example

### Lecture 4: ETL Pipeline II - APIs and Automation (Jan 14)
- What is an API? REST API concepts
- Making HTTP requests with Python
- Understanding API parameters and authentication
- Handling pagination in API responses
- Rate limiting strategies (fixed delay, adaptive, token bucket)
- Error handling and retry logic with exponential backoff
- Logging for production pipelines
- Idempotent pipeline design
- Introduction to BigQuery
- Building complete automated ETL scripts

### Lecture 5: Python Wrangling I - Tidy Data, Types, and Validation (Jan 21)
- Tidy data principles (Hadley Wickham)
- Column typing and type coercion
- Reshaping data: wide to long (pd.melt)
- Missing data strategies (MCAR, MAR, MNAR)
- Validation checks: ranges, nulls, keys
- Building validation frameworks

### Lecture 6: Python Wrangling II - Merges, Reshaping, and Analysis-Ready Tables (Jan 26)
- Merging multiple data sources
- Handling different key column names
- Join types and validation
- Advanced pivot and unpivot patterns
- Building analysis-ready tables
- Data contracts and lineage documentation

### Lecture 8: ETL Tools - BigQuery and Automation (Jan 28)
- BigQuery overview and cloud data warehouses
- Data loading patterns (batch, streaming, chunked)
- Automated ETL scripts with configuration
- Scheduling with cron expressions
- Logging, monitoring, and alerting
- Pipeline orchestration patterns
- Error recovery and retry strategies

### Lecture 9: Data Cleaning I - Formats, Dates, and Strings (Feb 2)
- European decimal format conversion (semicolon delimiters, comma decimals)
- Multi-format date parsing strategies
- String normalization (case, whitespace, special characters)
- Generating matching keys for record linkage
- Deduplication strategies (exact, fuzzy, temporal)
- Method chaining for clean pipelines

### Lecture 10: Data Cleaning II - Outliers and Validation (Feb 4)
- Statistical outlier detection (IQR method, Z-score)
- Domain-based validation rules
- Missing value strategies by mechanism (MCAR, MAR, MNAR)
- Data quality scoring frameworks
- Completeness, validity, and consistency metrics
- Building comprehensive validation reports

### Lecture 11: Visualization I - Matplotlib and Plotly (Feb 9)
- Matplotlib fundamentals (Figure, Axes, Artists)
- Time series visualization with formatted date axes
- Multi-panel figures and subplots
- Interactive visualizations with Plotly Express
- Customizing hover information and tooltips
- Accessibility best practices (colorblind-friendly palettes)
- Data storytelling principles

---

## Labs

### Lab 1: Loading Data into MySQL (Due: Jan 16)
- Load CSV data (Food Nutrition dataset)
- Clean and prepare data for database storage
- Create MySQL table with proper schema
- Insert data and verify with SQL queries
- Practice basic SQL queries

### Lab 2: Building an ETL Pipeline (Jan 14)
- Extract data and add metadata columns (_source_file, _extracted_at, _row_num)
- Transform data by selecting and renaming columns
- Create raw and cleaned data layers
- Document data lineage transformations
- Work with climate change indicators dataset (FAO temperature data)

### Lab 3: Python Wrangling - Tidy Data, Types, and Validation (Jan 21)
- Read data from MySQL database tables
- Check and convert data types appropriately
- Reshape data from wide to long format using pd.melt()
- Analyze and handle missing data (MCAR, MAR, MNAR strategies)
- Implement validation checks (range, null, uniqueness)
- Create comprehensive data validation reports

### Lab 4: ETL Pipeline Development (Jan 28)
- Build configuration classes for pipeline settings
- Implement logging with different levels
- Create retry decorators with exponential backoff
- Write ETL extract, transform, and load functions
- Generate pipeline execution reports

### Lab 5: Data Cleaning Fundamentals (Feb 2)
- European decimal format conversion
- Multi-format date parsing
- String normalization techniques
- Deduplication with matching keys
- Complete data cleaning pipelines

### Lab 6: Data Visualization (Feb 9)
- Matplotlib line, bar, and histogram plots
- Multi-panel figure layouts
- Time series with moving averages
- Dual y-axis plots
- Interactive Plotly visualizations
- Accessibility-friendly design

---

## Supplementary Materials

### SQL Lecture Notes
Comprehensive notes covering:
- Git and GitHub workflows (fork, stash, pull conflicts)
- SQL fundamentals and case sensitivity
- DDL and table creation
- Primary keys and foreign keys
- Table relationships and joins
- Working with external data

### Installation Guide
Complete setup instructions for:
- Anaconda and Jupyter
- Git and GitHub (including SSH keys)
- VS Code and extensions
- Docker and MySQL container

---

## Assessment

| Component | Weight |
|-----------|--------|
| Assignments (2) | 20% |
| Labs (6) | 15% |
| Group Project & Report | 30% |
| Quizzes (3) | 30% |
| Case Study and Reading | 2% |
| Participation | 3% |

---

## Key Dates

| Item | Date |
|------|------|
| Teams Formed | Jan 07 |
| Lab 1 Due | **Jan 16, 11:59 PM** |
| Assignment 1 Due | ~~Jan 14~~ → **Jan 18, 11:59 PM** |
| Quiz 1 | Jan 19 |
| Quiz 2 | Jan 28 |
| Assignment 2 Due | Feb 02 |
| Quiz 3 | Feb 09 |
| Final Presentations | Feb 11 |

---

## Assignments Overview

### Assignment 1: SQL Access Layer (20 points)
- ERD and schema documentation
- SQL queries: joins, CTEs, window functions
- Pivot/unpivot operations
- Table contracts and analysis-ready views
- **Due: ~~January 14~~ January 18, 11:59 PM**

### Assignment 2: ETL Pipeline (20 points)
- Pipeline architecture documentation
- Extract data from Open-Meteo Weather API
- Rate limiting and retry logic implementation
- Data transformation and validation
- Monthly/annual aggregations
- Integration with crop production data
- **Due: February 2**

---

## Technologies Used

- **Database:** MySQL 8.0, Google BigQuery
- **Languages:** Python, SQL
- **Tools:** Docker, Jupyter Notebooks, VS Code, Git/GitHub
- **Libraries:** pandas, SQLAlchemy, pymysql, mysql-connector-python, matplotlib, plotly, requests

---

## Repository Structure

```
FRE521D-Winter2026-UBC/
├── README.md
├── LICENSE
├── Lectures/
│   ├── Lecture 1 01-05-2026/
│   ├── Lecture 2 01-07-2026/
│   ├── Lecture 3 01-12-2026/
│   ├── Lecture 4 01-14-2026/
│   ├── Lecture 6 01-21-2026/
│   ├── Lecture 7 01-26-2026/
│   ├── Lecture 8 01-28-2026/
│   ├── Lecture 9 02-02-2026/
│   ├── Lecture 10 02-04-2026/
│   └── Lecture 11 02-09-2026/
├── Labs/
│   ├── Lab-1 01-12-2026/
│   ├── Lab-2 01-19-2026/
│   ├── Lab-3 01-21-2026/
│   ├── Lab-4 28-01-2026/
│   ├── Lab-5 02-02-2026/
│   └── Lab-6 02-09-2026/
├── Datasets/
│   ├── AirQualityUCI.csv
│   ├── GlobalWeatherRepository.csv
│   ├── climate_change_indicators.csv
│   ├── FOOD-DATA-GROUP1.csv
│   ├── FOOD-DATA-GROUP2.csv
│   └── potential-impacts-world-food-supply.xls
├── Assignments/
│   ├── A-1/
│   └── A-2/
├── Notes/
│   └── SQL_Lecture_Notes.md
└── Setup/
    └── Installation_Guide.ipynb
```

---

## Contributing

This repository is for educational purposes. If you find any issues or have suggestions, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

**Instructor:** Asif Ahmed Neloy  
**GitHub:** [@aaneloy](https://github.com/aaneloy)

---

*University of British Columbia | Master of Food and Resource Economics | Winter 2026*
