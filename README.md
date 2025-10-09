# Project Title: Exploratory Data Analysis of Industrial Facility Combustion Energy Use in the US in 2014

 **Uncover Insights🔎**: [Open the Interactive Web App 🚀](https://your-streamlit-app-url.streamlit.app/)

This project entails the exploratory data analysis of industrial facilities' combustion energy use for 2014. The primary objective is to discover valuable and actionable insights from the dataset on combustion energy use to help reduce energy inefficiencies in the industries covered. The entire project was executed in Python, using libraries such as Pandas for data manipulation, Matplotlib and Seaborn for data visualization, Plotly for creating dynamic visualizations, and Streamlit to deploy a web-based dashboard for data reporting.

## 🎯 Table of Contents
- [Project Overview](#projectoverview)
- [Data Source](#datasource)
- [Project Structure](#projectstructure)
- [Getting Started](#gettingstarted)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## 📖 Project Overview <a name="projectoverview"></a>
* **Motivation:** The dataset was chosen because of the need to improve energy efficiency in industrial facilities.
* **Key Questions asked:** The exploratory analysis looked to answer the following key questions:
  - What are the dominant fuel types used by combustion units in the different regions of the country?
  - Which industrial facilities have the highest combustion energy use?
  - Which industrial facilities have the most combustion units, and what kind of combustion units are present in such facilities?
  - What is the average and total energy consumption by region?
  - What is the distribution of average and total energy consumption by State?
  - What industries are the major contributors to energy use?
  - What industries employ majority of their energy use for cogeneration purposes?
  - What is the distribution of cogeneration-designated and non-cogeneration-designated units across the different industries? 
* **Technologies Used:** Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Jupyter Notebook, Streamlit.

## 💾 Data Source <a name="datasource"></a>
* **Source:** The [Industrial Facility Combustion Energy Use](https://data.nrel.gov/system/files/50/IndustrialCombEnergy_2014%20%281%29.csv) dataset was obtained from [NREL Data Catalog](https://data.nrel.gov/submissions)
* **Description:** The dataset contains **20,117** records of combustion units from different industrial facilities in the US for 2014. It includes **23 primary features**: 11 numerical (e.g., *Total MMBtu, Total GWht*) and 12 categorical (e.g., *Fuel Type, Unit Type*). A critical initial step involved data cleaning: 7% of records with missing *Unit Type*, *Cogeneration Unit Emission Indicator* and *MECS Region* were removed from the dataset; 12 unwanted columns were dropped; and a custom label encoder was applied to make the binary category values of the *Cogeneration Unit Emission Indicator* feature easily interpretable.

## 📂 Project Structure <a name="projectstructure"></a>
<pre>
├── analysis_notebook/
│   └── main.ipynb
├── app_deploy/
│   └── initial_exploration.ipynb
├── data_source/
│   └── IndustrialCombEnergy_2014.csv
├── LICENSE
├── README.md
├── requirements.txt
</pre>

## 🛠️ Getting Started <a name="gettingstarted"></a>
### Prerequisites <a name="prerequisites"></a>
* Python 3.12.0 or higher
* Git for cloning the repository
* Pip for installing python libraries
* Integrated Development Environment (IDE): VSCode, or any other suitable development environment

### Installation <a name="installation"></a>
1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Oluwatobi-coder/Exploratory-Data-Analysis-Industrial-Facility-Combustion-Energy-Use-2014.git](https://github.com/Oluwatobi-coder/Exploratory-Data-Analysis-Industrial-Facility-Combustion-Energy-Use-2014.git)
    cd Exploratory-Data-Analysis-Industrial-Facility-Combustion-Energy-Use-2014
    ```
2.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## 🏃 Usage <a name="usage"></a>
* **For a Jupyter Notebook analysis:**
    "The full analysis can be viewed and executed in the `main.ipynb` notebook. Press `Ctrl + Enter` (for Windows) (or `Cmd + Enter` on macOS) to run each cell."
* **For a Streamlit app:**
    "To view the interactive app, run the following command in your terminal:"
    ```sh
    cd app_deploy # to navigate to the app_deploy folder
    streamlit run app.py
    ```

## 📄 License <a name="license"></a>
* This project is licensed under the MIT License - see the `LICENSE.md` file for details.
