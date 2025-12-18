# Morris & Dickson Sales Pipeline

## 1. Project Overview
This repository contains a take-home exercise completed as part of the interview process with **Morris & Dickson**. The assignment was to build a simple, end-to-end data pipeline from provided JSON sales data into a medallion architecture and to produce a small set of business-facing dashboards.

At the hiring manager’s suggestion, the solution was implemented using **Databricks Free Edition** to demonstrate familiarity with tools used by the team, while keeping the overall scope intentionally modest. 

---

## 2. Stakeholder Questions
The stakeholder requirements for this exercise were intentionally focused:

- View **sales by customer**
- View **sales by geographic location**

The pipeline and downstream analytics are designed specifically to support these questions without unnecessary complexity.

---

## 3. Dataset
The dataset  consists of JSON files representing a small sales domain. At a high level, the data includes:

- Customers  
- Products  
- Orders  
- Sales transactions  
- Country / geographic reference data  

---

## 4. Architecture Overview
The solution follows a  **medallion architecture** pattern:

- **Bronze**: Raw ingestion of source JSON files with minimal transformation  
- **Silver**: Cleaned, normalized tables suitable for relational joins and modeling  
- **Gold**: Analytics-ready tables designed for consumption by BI tools  

---

## 5. Technology Choices
Tech stack for this project:

- **Databricks Free Edition** – execution environment (used per hiring manager guidance)  
- **PySpark** – data ingestion and transformation  
- **Python** – supporting logic and notebook organization  
- **CSV exports** – used to bridge Databricks outputs into Power BI  
- **Power BI** – dashboarding and visualization  

While orchestration tools were not required for this exercise, the structure reflects patterns that would translate cleanly to scheduled or orchestrated pipelines.

---

## 6. Repository Structure
The repository is organized to mirror the logical flow of the pipeline:

- `notebooks/` – Databricks notebooks for ingestion, transformation, and modeling  
- `data/` – Exported CSV files produced from the Gold layer for BI consumption  
- `powerbi/` – Power BI report file  
- `README.md` – Project overview and documentation  

---

## 7. Data Pipeline Walkthrough

### 7.1 Bronze Layer
The Bronze layer ingests the raw JSON files exactly as provided. Minimal changes are applied beyond basic parsing and column normalization where required to load the data reliably.


### 7.2 Silver Layer
In the Silver layer, raw data is cleaned and normalized:

- Column names are standardized  
- Data types are corrected  
- Reference data (e.g., countries) is resolved  
- Relationships between entities are made explicit  

These tables are designed to be reusable building blocks for downstream analytics.

### 7.3 Gold Layer
The Gold layer reshapes Silver tables into analytics-ready structures. Fact and dimension tables are created with a clear grain, making them easy to consume in Power BI without additional transformation logic.

---

## 8. Analytics Layer (Gold)
The Gold layer supports reporting through:

- A sales fact table containing transactional measures  
- Dimension tables for customers, products, dates, and geography  

---

## 9. Dashboard Overview
The Power BI dashboard built on top of the Gold layer includes:

- Sales by customer  
- Sales by geographic location  
- Basic filtering and aggregation to support exploratory analysis  

The dashboard is intentionally simple and focused on answering the stated stakeholder questions.

---

## 10. How to Reproduce
A full local reproduction is not required to review the solution. To explore the project:

1. Clone the repository  
2. Review the Databricks notebooks for each pipeline stage  
3. Inspect the exported Gold-layer CSV files  
4. Open the Power BI report to view the dashboards

Notebooks were executed sequentially.

---

## 11. Notes & Assumptions
- The dataset is static and provided solely for this exercise  
- Pipelines are executed manually  
- The solution prioritizes clarity and correctness over scalability or automation  

