# Titanic EDA Project

##  Overview
This project performs **Exploratory Data Analysis (EDA)** on the famous Titanic dataset.  
The main goal is to clean the dataset, handle missing values, visualize key features, and summarize insights in a simple report.

---

##  Dataset
- Dataset: Titanic dataset (available in Seaborn library)
- Rows: ~891
- Columns: 15+
- Features: age, sex, class, fare, survived, embarked, etc.

---

##  Steps Performed
1. **Data Cleaning**
   - Missing `age` values filled with median
   - Missing `embarked` and `embark_town` values filled with mode
   - Dropped `deck` column due to excessive missing values  

2. **Exploratory Data Analysis**
   - Survival rates visualization
   - Age distribution with KDE
   - Age vs Fare scatter plot colored by survival status  

3. **Reporting**
   - Findings summarized and saved into `outputs/eda_report.txt`

---

##  Key Findings
- **Survival Rates:** Fewer passengers survived compared to those who did not.  
- **Age Distribution:** Most passengers were in their 20s and 30s.  
- **Age vs Fare:** No strong correlation between age and fare. Higher fares were linked to higher survival probability.  

---

## 📁 Project Structure
