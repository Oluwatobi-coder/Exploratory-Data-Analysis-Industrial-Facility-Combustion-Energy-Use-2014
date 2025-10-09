# importing the required libraries
import streamlit as st # for turning data scripts into web applications
import plotly.express as px # for Plotly visualizations using high-level interface
import plotly.io as pio # for displaying and saving Plotly figures
import pandas as pd # for data manipulation and analysis with DataFrames
import numpy as np # for numerical operations and array manipulation


# setting the opening of Plotly charts in a browser tab
pio.renderers.default = "browser"


# setting the helper function to load data (cached for performance)
@st.cache_data
def load_combustion__energy_dataset():
    # loading the dataset from the file system
    df = pd.read_csv('../data_source/IndustrialCombEnergy_2014.csv', encoding="ANSI")
    # returning the loaded dataset as output
    return df

# getting the loaded dataset via the function call
raw_df = load_combustion__energy_dataset()

# dropping the columns that are not required for the analysis
transformed_df = raw_df.drop(['FACILITY_ID', 'FUEL_TYPE_BLEND', 'FUEL_TYPE_OTHER', 'OTHER_OR_BLEND_FUEL_TYPE', 'CENSUS_PLACE_NAME', \
                                            'REPORTING_YEAR','COUNTY','COUNTY_FIPS','LATITUDE', 'LONGITUDE','ZIP', 'PRIMARY_NAICS_CODE'], \
                                                  axis=1)

# transforming the values of the COGENERATION_UNIT_EMISS_IND column
transformed_df.replace({'COGENERATION_UNIT_EMISS_IND': {'Y': 'Yes', 'N': 'No'}}, inplace=True)

# dropping the records having null values
cleaned_df = transformed_df.dropna(ignore_index=True)




# setting the page meta title
st.set_page_config(page_title='EDA Analysis on U.S. Industrial Facility Combustion Energy Use', page_icon="🏭",
                   layout="wide")


# setting up the page header
st.title("Exploratory Data Analysis of U.S. Industrial Facility Combustion Energy Use For Year 2014 🏭")
st.markdown("""
This app presents an interactive analysis of the U.S. Industrial Facility Combustion Energy Use For Year 2014. 
Explore the different sections using the **Navigation Menu**.
""")
st.markdown("[Link to the Source Code on GitHub](https://github.com/Oluwatobi-coder/Exploratory-Data-Analysis-Industrial-Facility-Combustion-Energy-Use-2014)")
st.markdown("**Author**: Bello Oluwatobi")
st.markdown("**Last Updated on**: 6th October, 2025")
# adding a visual separator
st.markdown("---")

# setting up the page sidebar
st.sidebar.header("Navigation Menu")
# displaying the pages as radio button for easy navigation
page = st.sidebar.radio("Go to", ["Project Overview", "Dataset Exploration", "Key Insights", "Conclusion and Recommendations", "References"])


# setting up the page contents for the sidebar navigation
# setting up the Project Overview page
if page == "Project Overview":
    # the introduction section
    st.header("Introduction 📰")
    # content for the introduction section
    st.write("""
    Industrial facilities are major drivers of the world economy and are significant consumers of energy. 
             The U.S. (United States) is a hugely industrialised nation, with the 
             industrial sector accounting for 33 percent and 35 percent of total U.S. energy 
             consumption and end-use energy consumption, respectively, in 2022, 
             according to the EIA (U.S. Energy Information Administration).
    """)
    st.write("""
    The industrial sector, being a massive user of energy, is prone to inefficiencies, 
             resulting in higher operational costs, carbon emissions and a substantial 
             environmental footprint. 
    """)

    # the project goals and objective section
    st.header("Project Goal and Objectives 🎯")
    # content for the project goals and objective section
    st.write("""
    The primary goal of this Exploratory Data Analysis (EDA) is to uncover insights 
             from the 2014 industrial facility combustion energy use dataset for the U.S. 
             This helps in proposing data-driven solutions to combat energy consumption 
             inefficiency in the industrial sector. 
    """)
    st.write("""
    This EDA project attempts to provide answers to the following **key questions**: 
    """)
    st.write("""
    - What are the dominant fuel types used by combustion units in the different regions of the country?
    - Which industrial facilities have the highest combustion energy use?
    - Which industrial facilities have the most combustion units, and what kind of combustion 
             units are present in such facilities?
    - What is the average and total energy consumption by region?
    - What is the distribution of average and total energy consumption by State?
    - What industries are the major contributors to energy use?
    - What industries employ majority of their energy use for cogeneration purposes?
    - What is the distribution of cogeneration-designated and non-cogeneration-designated units across the different industries?         
    """)
    
    # the dataset information subsection
    st.subheader("About the Dataset 📊")
    # content for the dataset information subsection
    st.write("""
    The [Industrial Facility Combustion Energy Use 2014](https://data.nrel.gov/system/files/50/IndustrialCombEnergy_2014%20%281%29.csv) dataset was obtained from 
             the [National Renewable Energy Laboratory (NREL) Data Catalog](https://data.nrel.gov/submissions).
    """)
    st.write("""
    **What do the rows and columns represent?**
    """)
    st.write("""
    **Rows:** Each row represents a single combustion unit. A **combustion unit** is a device 
             or a system where fuel is burned in a controlled environment to generate heat, 
             destroy waste, or recover energy.
    """)
    st.write("""
    **Columns:** The columns represent the attributes of each combustion unit.
    """)
    st.markdown("""
    - ```FACILITY_ID```: The unique identifier for the facility where the combustion unit belongs
    - ```FACILITY_NAME```: The name of the facility where the combustion unit belongs
    - ```FUEL_TYPE```: The type of fuel used by the combustion unit
    - ```FUEL_TYPE_BLEND```: The type of fuel blend used by the combustion unit
    - ```FUEL_TYPE_OTHER```: Other type of fuel used by the combustion unit
    - ```OTHER_OR_BLEND_FUEL_TYPE```: Other or blend of fuel used by the combustion unit
    - ```REPORTING_YEAR```: The reporting year i.e. 2014
    - ```UNIT_NAME```: The name of the combustion unit
    - ```UNIT_TYPE```: The type of the combustion unit
    - ```COUNTY```: The US county of the facility
    - ```COUNTY_FIPS```: The FIPS (Federal Information Processing Standard) unique identifier for a US county
    - ```LATITUDE```: The latitude of the facility 
    - ```LONGITUDE```: The longitude of the facility
    - ```STATE```: The US state of the facility
    - ```ZIP```: The ZIP code of the facility
    - ```PRIMARY_NAICS_CODE```: The unique identifier for the facility based on NAICS (North American Industry Classification System)
    - ```PRIMARY_NAICS_TITLE```: The title of the facility based on NAICS (North American Industry Classification System)
    - ```COGENERATION_UNIT_EMISS_IND```: Indicator of combustion unit use for cogeneration purposes
    - ```CENSUS_PLACE_NAME```: The name of the location where census is taken for the facility
    - ```MECS_Region```: The MECS (Manufacturing Energy Consumption Survey) region of the facility
    - ```MMBtu_TOTAL```: The total energy use of the combustion unit in MMBTU (Million British Thermal Units)
    - ```GWht_TOTAL```: The total energy use of the combustion unit in GWht (Gigawatt-hour thermal)
    - ```GROUPING```: The group where the facility belongs                                                                                           
    """)

# setting up the Dataset Exploration page
elif page == "Dataset Exploration":
    # the dataset exploration header
    st.header("Deep Dive into the Data 🔍")
    
    # the dataset's shape subsection
    st.subheader('Shape of the Dataset')
    # extracting the shape of the dataset
    size_of_df = raw_df.shape
    # content for the dataset's shape
    st.write(f"The dataset consists of **{size_of_df[0]} rows** and **{size_of_df[1]} columns**.")

    # the dataset overview subsection
    st.subheader('Quick Overview of the Dataset')
    # content for the dataset's shape
    st.write("Exploring the first and last few rows of the dataset.")
    # extracting the first few rows of the dataset
    st.dataframe(raw_df.head())
    # extracting the last few rows of the dataset
    st.dataframe(raw_df.tail())

    # the dataset's data types subsection
    st.subheader('Data Types of the Dataset')
    # content for the dataset's data types subsection
    st.write("Checking the data types for each column of the dataset.")
    # extracting the data types of the dataset
    df_dtypes = raw_df.dtypes
    # showing the data types
    st.write(df_dtypes)

    # the dataset's summary statistics subsection
    st.subheader('Summary Statistics of the Dataset')
    # content for the dataset's summary statistics subsection
    st.write("Examining the desciptive statistics of the dataset's numerical columns.")
    # extracting the summary statisitics of the dataset
    df_desc_stats = raw_df.describe()
    # showing the summary statistics
    st.write(df_desc_stats)

    # the dataset cleaning/preparation subsection
    st.subheader('Cleaning the Dataset')
    # content 2 for the dataset cleaning subsection
    st.write("**Dropping the unwanted columns**")
    # content 3 for the dataset cleaning subsection
    st.write("- The following columns were dropped from the dataset:")
    st.write("""
    - ```FACILITY_ID```, ```CENSUS_PLACE_NAME```, ```COUNTY```,  ```COUNTY_FIPS```, 
              ```LATITUDE```, ```LONGITUDE```, ```ZIP```, 
             ```PRIMARY_NAICS_TITLE```: These columns were dropped because they were not 
             required for the analysis.
    """)
    st.write("""
    - ```FUEL_TYPE_BLEND```, ```FUEL_TYPE_OTHER```, 
             ```OTHER_OR_BLEND_FUEL_TYPE```: These columns were dropped because they contained only
             missing values.
    """)
    st.write("""
    - ```REPORTING_YEAR```: This column was dropped because it was single-valued i.e. 
             contained ony 2014, which is the reporting year of the data, all through the dataset.
    """)
    # content 3 for the dataset cleaning subsection
    st.write("**Transforming the Y and N values in the ```COGENERATION_UNIT_EMISS_IND``` column**")
    st.write("""
    The binary values of column were transformed from:
     - ```Y``` to ```Yes``` and,
     - ```N``` to ```No```
    """)
    st.write("This was done to simplify the dataset for easy identification.")

    # content 4 for the dataset cleaning subsection
    st.write("**Searching for missing data**")
    st.write("""
    The dataset was examined for the presence of missing data.
    """)
    # checking the dataset for missing values
    cleaned_df_missing_vals = transformed_df.isna().sum()
    # showing the result
    st.write(cleaned_df_missing_vals)

    # content 5 for the dataset cleaning subsection
    st.write("**Removing missing data**")
    st.write("""
    Since the missing data in the dataset belong to categorical columns, 
             the rows where missing data was present were dropped. This is beause a 
             meaningful missing value replacement method could not be determined without 
             corrupting the integrity of the dataset.
    """)
    # checking again for missing values after cleaning
    st.write(cleaned_df.isna().sum())

    # content 6 for the dataset cleaning subsection
    st.write("**Checking for duplicated data**")
    dupli_df = cleaned_df.loc[cleaned_df.duplicated()]
    st.write("The dataset was assessed for presence of duplicated records, so that each record of data \
             was a representative of a unique observation. The dataset was found to contain \
              **0** duplicate records.")
    # showing the duplicated data, if any
    st.write(dupli_df)

    # content 7 for the dataset cleaning subsection
    st.write("**Data remaining after cleaning process**")
    # calculating the percentage of data remaining after the cleaning process
    pct_rem_data = len(cleaned_df)/len(raw_df)
    # showing the remaining data
    st.write(f"The percentage of data remaining after the cleaning process was {pct_rem_data*100:.2f} %, \
             representing a significant amount of data left for the EDA analysis.")

    # dataset feature exploration subsection
    st.subheader('Feature Exploration of the Dataset')

    # extracting the different fuel types in the dataset
    fuel_type_dt = cleaned_df['FUEL_TYPE'].value_counts()
    # extracting the fuel types and their corresponding counts 
    y_1, x_1 = fuel_type_dt.index, fuel_type_dt.values
    
    # plotting the bar graph of the fuel types
    fig_1 = px.bar(x=x_1, y=y_1, title='Fuel Type Used across the different combustion units', 
                   labels={'x':'No. of combustion units',
                           'y': 'Fuel Type'},
                           height=600)
    fig_1.update_layout(title={
            'x': 0.5, # Sets the x-position to the center (0.5)
            'xanchor': 'center' # Aligns the title's center with the x-position 
        })
    st.plotly_chart(fig_1, use_container_width=False)
    
    # extracting the different combustion units in the dataset
    unit_type_dt = cleaned_df['UNIT_TYPE'].value_counts()
    # extracting the combustion units and their corresponding counts
    y_2, x_2 = unit_type_dt.index, unit_type_dt.values

    # plotting the bar graph of the combustion units
    fig_2 = px.bar(x=x_2, y=y_2, title='Combustion Unit Type Used across the Industries', 
                   labels={'x':'No. of combustion units',
                           'y': 'Combustion unit type'},
                           height=600)
    fig_2.update_layout(title={
            'x': 0.5,
            'xanchor': 'center'
        })
    st.plotly_chart(fig_2, use_container_width=False)
    
    # extracting the different industries based on NAICS in the dataset and selecting the first 20
    naics_dt = cleaned_df['PRIMARY_NAICS_TITLE'].value_counts().head(20)
    # extracting the industries and their corresponding counts
    y_3, x_3 = naics_dt.index, naics_dt.values

    # plotting the bar graph of the industries
    fig_3 = px.bar(x=x_3, y=y_3, title='Classification of Combustion Units by NAICS title (Top 20)', 
                   labels={'x':'No. of combustion units',
                           'y': 'NAICS Title'},
                           height=600)
    fig_3.update_layout(title={
            'x': 0.5,
            'xanchor': 'center'
        })
    st.plotly_chart(fig_3, use_container_width=False)


    # extracting the different industry groups in the dataset
    group_dt = cleaned_df['GROUPING'].value_counts()
    # extracting the industry groups and their corresponding counts
    y_4, x_4 = group_dt.index, group_dt.values

    # plotting the bar graph of the industry groups
    fig_4 = px.bar(x=x_4, y=y_4, title='Classification of Combustion Units by Industry Group', 
                   labels={'x':'No. of combustion units',
                           'y': 'Industry Group'},
                           height=600)
    fig_4.update_layout(title={
            'x': 0.5,
            'xanchor': 'center'
        })
    st.plotly_chart(fig_4, use_container_width=False)

    
    # extracting the cogeneration status of the combustion units in the dataset
    cogen_dt = cleaned_df['COGENERATION_UNIT_EMISS_IND'].value_counts()
    # extracting the corresponding counts of the two groups (Yes and No)
    x_5, y_5 = cogen_dt.index, cogen_dt.values

    # plotting the bar graph of the cogeneration status of the combustion units
    fig_5 = px.bar(x=x_5, y=y_5, title='Classification of Combustion Units by Cogeneration', 
                   labels={'x':'Cogeneration Indicator',
                           'y': 'No. of combustion units'},
                           )
    fig_5.update_layout(title={
            'x': 0.5,
            'xanchor': 'center'
        })
    st.plotly_chart(fig_5, use_container_width=False)

    # extracting the different regions in the dataset
    mecs_dt = cleaned_df['MECS_Region'].value_counts()
    # extracting the different regions and their corresponding combustion unit counts
    x_6, y_6 = mecs_dt.index, mecs_dt.values

     # plotting the bar graph of the combustion units' division by region
    fig_6 = px.bar(x=x_6, y=y_6, title='Classification of Combustion Units by Manufacturing Energy Consumption Survey (MECS) Region', 
                   labels={'x':'MECS Region',
                           'y': 'No. of combustion units'},
                           )
    fig_6.update_layout(title={
            'x': 0.5, 
            'xanchor': 'center' 
        })
    st.plotly_chart(fig_6, use_container_width=False)

    # extracting the combustion energy values in MMBtu
    mmbtu_dt = cleaned_df['MMBtu_TOTAL']
    # extracting the combustion energy values in GWht
    gwht_dt = cleaned_df['GWht_TOTAL']

    # splitting the section into 2 columns - for MMBtu and GWht
    col_mmbtu, col_gwht = st.columns(2)

    # plotting the first histogram graph for the MMBtu values
    with col_mmbtu:
        fig_7_1 = px.histogram(x=mmbtu_dt, nbins=20, title='Distribution of Total Energy Use (MMBtu)',
                               labels={'x':'Total Energy Use (MMBtu)',
                           'y': 'Count'})
        fig_7_1.update_layout(
        title={
            'x': 0.5,  # Sets the x-position to the center (0.5)
            'xanchor': 'center' # Aligns the title's center with the x-position
        }
    )
        st.plotly_chart(fig_7_1, use_container_width=False)

    # plotting the second histogram graph for the GWht values
    with col_gwht:
        fig_7_2 = px.histogram(x=gwht_dt, nbins=20,  title='Distribution of Total Energy Use (GWht)',
                        labels={'x':'Total Energy Use (GWht)',
                           'y': 'Count'}        )
        fig_7_2.update_layout(
        title={
            'x': 0.5,  
            'xanchor': 'center' 
        }
    )
        st.plotly_chart(fig_7_2, use_container_width=False)

    # getting the correlation between the MMBtu and GWht values
    corr_df = cleaned_df[['MMBtu_TOTAL', 'GWht_TOTAL']].corr()

    # splitting the section into 2 columns - for scatter plot and heatmap
    col_rel_scatter, col_rel_corr = st.columns(2)

    # plotting the scatterplot for relationship between the MMBtu and GWht values
    with col_rel_scatter:
        fig_8_1 = px.scatter(x=gwht_dt, y=mmbtu_dt, title='Scatterplot of MMBtu vs GWht',
                               labels={'x':'Total Energy Use (GWht)',
                           'y': 'Total Energy Use (MMBtu)'})
        fig_8_1.update_layout(
        title={
            'x': 0.5, 
            'xanchor': 'center'
        }
    )
        st.plotly_chart(fig_8_1, use_container_width=False)
  
    # plotting the correlation heatmap to show the correlation between MMBtu and GWht
    with col_rel_corr:
        fig_8_2 = px.imshow(corr_df, text_auto=True, title='Heatmap of MMBtu vs GWht',
                            labels=dict(color="Correlation"),
                x=['MMBtu', 'GWht'],
                y=['MMBtu', 'GWht'])
        
        fig_8_2.update_layout(
        title={
            'x': 0.5, 
            'xanchor': 'center' 
        }
    )
        st.plotly_chart(fig_8_2, use_container_width=False)

    # content for the relationship and correlation of the MMbtu and GWht values
    st.write("The reason for the linear relationship and positive correlation **(i.e. 1)**" \
    " between energy units: " \
    "Million British Thermal Units **(MMBtu)** and Gigawatt Hours-thermal **(GWht)** \
        can be attributed to the direct conversion that exists between both units \
              **(1 MMBtu = 0.00029 GWh)**, according to \
                [Kyle's Converter](https://www.kylesconverter.com/energy,-work,-and-heat/million-british-thermal-units-to-gigawatt-hours).")
    st.write("**NOTE**: **GWht** indicates thermal energy, and it uses the same scale as **GWh** (which quantifies electrical energy)")

    # the dataset outlier visualization subsection
    st.subheader("**Visualizing Outliers in the Data**")
    
    # extracting the fuel type column of the dataset
    fuel_type_dt_1 = cleaned_df['FUEL_TYPE']
    # extracting the MMBtu column of the dataset
    mmbtu_dt_1 = cleaned_df['MMBtu_TOTAL']
    
    # showing the boxplot distribution of the different fuel types and their usage in terms of combustion energy
    fig_9 = px.box(x=mmbtu_dt_1, y=fuel_type_dt_1, 
                   title='Boxplot Distribution of Fuel Type and their energy use (MMBtu)',
                   labels={'x':'Total Energy Use (MMBtu)',
                           'y': 'Fuel Type'},
                   height=1000)
    fig_9.update_layout(title={
            'x': 0.5,  # Sets the x-position to the center (0.5)
            'xanchor': 'center' # Aligns the title's center with the x-position
        })
    st.plotly_chart(fig_9, use_container_width=False)
    
    # extracting the combustion unit type column of the dataset
    unit_type_dt_1 = cleaned_df['UNIT_TYPE']

    # showing the boxplot distribution of the different combustion units and their corresponding combustion energy use
    fig_10 = px.box(x=mmbtu_dt_1, y=unit_type_dt_1, 
                   title='Boxplot Distribution of  Combustion Unit Type and their energy use (MMBtu)',
                   labels={'x':'Total Energy Use (MMBtu)',
                           'y': 'Unit Type'},
                   height=800)
    fig_10.update_layout(title={
            'x': 0.5, 
            'xanchor': 'center' 
        })
    st.plotly_chart(fig_10, use_container_width=False)
    
    # extracting the industry group column of the dataset
    group_type_dt_1 = cleaned_df['GROUPING']
    # showing the boxplot distribution of the different industry groups and their corresponding combustion energy use
    fig_11 = px.box(x=mmbtu_dt_1, y=group_type_dt_1, 
                   title='Boxplot Distribution of the Industry Groups and their energy use (MMBtu)',
                   labels={'x':'Total Energy Use (MMBtu)',
                           'y': 'Group'},
                   height=600)
    fig_11.update_layout(title={
            'x': 0.5, 
            'xanchor': 'center'
        })
    st.plotly_chart(fig_11, use_container_width=False)

# setting up the Key Insights page
elif page == "Key Insights":
    # the key insights header
    st.header("Main Findings💡")
    # the key insights subsection
    st.subheader("Asking Key Questions About The Data ❓")

    # Question 1
    st.subheader("1. What are the dominant fuel types used by combustion units in each Manufacturing Energy Consumption Survey (MECS) region?")
    
    # extracting the fuel types used by combustion units in the South region and selecting the top 10 fuels used
    mecs_south = cleaned_df.query('MECS_Region == "South"') \
            .groupby('FUEL_TYPE') \
            .size() \
            .sort_values(ascending=False) \
            .head(10)

    # extracting the fuel types used by combustion units in the West region and selecting the top 10 fuels used
    mecs_west = cleaned_df.query('MECS_Region == "West"') \
                .groupby('FUEL_TYPE') \
                .size() \
                .sort_values(ascending=False) \
                .head(10)

    # extracting the fuel types used by combustion units in the Midwest region and selecting the top 10 fuels used
    mecs_midwest = cleaned_df.query('MECS_Region == "Midwest"') \
                .groupby('FUEL_TYPE') \
                .size() \
                .sort_values(ascending=False) \
                .head(10)

    # extracting the fuel types used by combustion units in the Northeast region and selecting the top 10 fuels used
    mecs_northeast = cleaned_df.query('MECS_Region == "Northeast"') \
                .groupby('FUEL_TYPE') \
                .size() \
                .sort_values(ascending=False) \
                .head(10)

    # extract the top 10 fuel types and their corresponding counts from the South region
    x_south, y_south = mecs_south.index, mecs_south.values


    # extract the top 10 fuel types and their corresponding counts from the West region
    x_west, y_west = mecs_west.index, mecs_west.values

    # extract the top 10 fuel types and their corresponding counts from the Midwest region
    x_midwest, y_midwest = mecs_midwest.index, mecs_midwest.values

    # extract the top 10 fuel types and their corresponding counts from the Northeast region
    x_northeast, y_northeast = mecs_northeast.index, mecs_northeast.values

    # splitting the section into 2 columns - for the first two regions
    col_mecs_south, col_mecs_west = st.columns(2)
    
   # plotting the first bar graph for the South region's top 10 fuel types
    with col_mecs_south:
        fig_12_1 = px.bar(x=x_south, y=y_south, title='South MECS Region (Top 10 Fuel Type Used)',
                               labels={'x':'Fuel Type',
                           'y': 'No. of combustion units'}, color_discrete_sequence=['green'])
        fig_12_1.update_layout(
        title={
            'x': 0.5, 
            'xanchor': 'center'
        },
        xaxis_tickangle=-45
    )
        st.plotly_chart(fig_12_1, use_container_width=False)

    # plotting the second bar graph for the West region's top 10 fuel types
    with col_mecs_west:
        fig_12_2 = px.bar(x=x_west, y=y_west, title='West MECS Region (Top 10 Fuel Type Used)',
                               labels={'x':'Fuel Type',
                           'y': 'No. of combustion units'}, color_discrete_sequence=['purple'])
        fig_12_2.update_layout(
        title={
            'x': 0.5, 
            'xanchor': 'center'
        },
        xaxis_tickangle=-45
    )
        st.plotly_chart(fig_12_2, use_container_width=False)

    # splitting the section into 2 columns - for the last two regions
    col_mecs_midwest, col_mecs_northeast = st.columns(2)

    # plotting the third bar graph for the Midwest region's top 10 fuel types
    with col_mecs_midwest:
        fig_12_3 = px.bar(x=x_midwest, y=y_midwest, title='Midwest MECS Region (Top 10 Fuel Type Used)',
                               labels={'x':'Fuel Type',
                           'y': 'No. of combustion units'}, color_discrete_sequence=['#D46A21'])
        fig_12_3.update_layout(
        title={
            'x': 0.5, 
            'xanchor': 'center'
        },
        xaxis_tickangle=-45
    )
        st.plotly_chart(fig_12_3, use_container_width=False)

    # plotting the last bar graph for the Nrtheast region's top 10 fuel types
    with col_mecs_northeast:
        fig_12_4 = px.bar(x=x_northeast, y=y_northeast, title='Northeast MECS Region (Top 10 Fuel Type Used)',
                               labels={'x':'Fuel Type',
                           'y': 'No. of combustion units'}, color_discrete_sequence=['#167F9E'])
        fig_12_4.update_layout(
        title={
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_tickangle=-45
    )
        st.plotly_chart(fig_12_4, use_container_width=False)
    
    # content for Question 1
    st.write("""
    A close examination of the different fuel types reveals striking similarities across the regions \
              of the United States: the South, West, Northeast, and Midwest. Although **natural gas** \
              is the **most dominant energy source**, the regions show a mix of other fossil \
             fuel-based energy sources, which are significant drivers of industrial processes.
    """)
    st.write("""
    Natural gas dominates the energy sources mix, due to its domestic availability, \
             relatively low cost, and clean nature compared to other fossil fuels, making \
             it attractive for most industrial facilities. Apart from natural gas, \
             energy sources, such as Distillate Fuel Oil No. 2 (or diesel fuel), fuel gas \
             and propane dominate as minority fuel types. Interestingly, energy sources \
             such as Municipal Solid Waste and Landfill Gas are present as significant \
             fuel types, showing the effort made towards transforming everyday waste \
             into beneficial energy resources.
  """)
    st.write("""
        The South region recorded the highest use of natural gas-powered combustion units, \
             with a total of **4467 units**, followed by the Midwest and West regions at **2981 units** \
             and **2051 units**, respectively. The Northeast region possesses the fewest natural \
             gas-powered combustion units, at **1497 units**.
    """)

    # Question 2
    st.subheader("2. Which industrial facilities have the highest combustion energy use?")
    
    # extracting the industrial facilities, ranking them based on total combustion energy usage and selecting the top 10
    inds_comb_high = cleaned_df.groupby('FACILITY_NAME')['MMBtu_TOTAL'] \
            .sum() \
            .sort_values(ascending=False) \
            .head(10)

    # extract the top 10 facilities and their corresponding total combustion energy use 
    x_inds_comb_high, y_inds_comb_high = inds_comb_high.index, inds_comb_high.values

    # plotting the bar graph for the top 10 industrial facilities
    fig_13 = px.bar(x=x_inds_comb_high, y=y_inds_comb_high, 
                          title='Top 10 Facilities with the Highest Combustion Energy Use',
                               labels={'x':'Facility',
                           'y': 'Combustion energy use (MMBtu)'}, height=600,
                           color_discrete_sequence=["#0B5345"])
    
    # plotting the bar graph for the top 10 industrial facilities
    fig_13.update_layout(
        title={
            'x': 0.5, 
            'xanchor': 'center'
        },
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig_13, use_container_width=False)
    
    # content for Question 2
    st.write("""
    The heaviest combustion energy consumers are petroleum refineries and petrochemical \
             facilities, due to the large amounts of combustion energy required to generate \
             heat and power for their operations. 
    """)
    st.write("""
    Occupying the first position is the ExxonMobil Baytown Complex, one of the world’s major \
             integrated petroleum and petrochemical facilities located in Texas and consisting \
              of four main sites that refine crude oil and produce petrochemicals. Other \
             ExxonMobil assets present are the Baton Rouge integrated facility and the Beaumont \
             refinery, located in Louisiana and Texas, respectively. The Blanchard Refining \
             Company LLC, Tesoro Carson Refinery, and Marathon Petroleum Company LP are all \
             subsidiaries of the Marathon Petroleum Company, which is the largest petroleum \
              refiner in the U.S. by capacity. 
  """)
    st.write("""
        Other facilities present are Dow Inc.’s Dow Texas Freeport Operations, an integrated \
             petrochemicals and plastics facility; Motiva Enterprises LLC’s Port Arthur \
             Manufacturing Complex, which houses the Port Arthur Refinery, which is the \
             largest refinery in North America; and Formosa Plastics Corporation’s Port \
              Comfort petrochemicals and plastics plant in Texas.  Alcoa Corporation’s Warwick \
             Operations is different from the others, as it is a primary metals facility involved \
             in aluminum production.
    """)

    # Question 3
    st.subheader("3. What industrial facilities  \
                 have the most combustion units? What kind of combustion units can \
                 be found in such facilities?")
    
    # extracting the facilities, ranking them based on the number of combustion units owned and selecting the top 10
    ind_top_comb_units = cleaned_df['FACILITY_NAME'] \
        .value_counts() \
        .sort_values(ascending=False) \
        .head(10)

    # extracting the top 10 facilities and their corresponding counts
    x_ind_top_comb_units, y_ind_top_comb_units = ind_top_comb_units.index, ind_top_comb_units.values
    
    # plotting the bar graph for the top 10 facilities
    fig_14_1 = px.bar(x=x_ind_top_comb_units, y=y_ind_top_comb_units, 
                      title='Top 10 Facilities with the most combustion units',
                        labels={'x':'Facility',
                           'y': 'No. of combustion units'}, height=600,
                          color_discrete_sequence=["#DC143C"])
    fig_14_1.update_layout(xaxis_tickangle=-45, title={
            'x': 0.5, 
            'xanchor': 'center'
        })
    st.plotly_chart(fig_14_1, use_container_width=False)

    # content for Question 3 - first part
    st.write("""
    A noteworthy and quite surprising finding from the analysis of the facilities with a \
             high number of combustion units is the presence of educational institutions \
             alongside heavy industrial operators. The ranking of universities such as the \
             University of Arizona and George Washington University highlights a key aspect \
              of campus operations, which lies in the substantial energy infrastructure \
             needed to support educational and research activities. 
    """)

    st.write("""
 After the educational institutions, the facilities with the most owned combustion units are \
             petrochemicals and oil refinery facilities. Motiva Enterprises LLC owns the largest North \
             American petroleum refinery and the United States' largest base oil plant, located in Port Arthur, \
              Texas. The Convent Refinery, \
             previously owned by Motiva and currently solely owned by Shell (acquired in 2017), is an \
             oil refinery located in Louisiana. The Dow Texas Operations, owned by Dow Inc., is located in 
              Freeport, Texas, and is an integrated petrochemicals facility that produces a significant \
              portion of Dow's products sold in the U.S. and globally. St Charles Operations (Taft/Star) \
             Union Carbide Corporation is a petrochemical manufacturing facility located in Louisiana, and \
              is also a subsidiary of Dow. Shell Deer Park Refinery is also a major petrochemical \
              manufacturing complex in Texas, U.S. The Whiting oil refinery, an asset of the BP Whiting \
             Business Unit, is located in Indiana and owned by BP, a major multinational oil and gas company. \
             The Mont Belvieu Complex is a petrochemical manufacturing complex located in Texas and owned by\
              Enterprise Products Operating LLC.  The Orchard Ridge Landfill & MRF, located in Wisconsin, is the\
              only waste management facility with a large energy usage footprint. 
    """)

    # splitting the section into 3 columns and 4 rows - one for each graph
    col_top_row = st.columns(3)
    col_2nd_row = st.columns(3)
    col_3rd_row = st.columns(3)
    col_bottom_row = st.columns(1)

    # making a copy of the cleaned dataset for aggregation
    copy_clean_df_1 = cleaned_df.copy()

    # extracting the top 10 facilities by number of units owned
    top_10_fcty_col = copy_clean_df_1.groupby('FACILITY_NAME')['UNIT_NAME'] \
                                        .size() \
                                        .sort_values(ascending=False) \
                                        .head(10).reset_index() \
                                        .drop('UNIT_NAME', axis=1)

    # extracting the facilities by the type and number of combustion units owned
    unit_group = copy_clean_df_1.groupby('FACILITY_NAME')['UNIT_TYPE'].value_counts()

    # looping through the array of 10 ten facilities based on number of combustion units owned
    for i in range(len(col_top_row)):
        # extracting the facility name
        fcty_name = top_10_fcty_col.iloc[i]['FACILITY_NAME']

        # plotting the bar graphs for the top row
        with col_top_row[i]:
            # extracting the combustion units for a single facility
            grouping_1 = unit_group[fcty_name]
            # extracting the combustion units and their corresponding counts
            x_1_, y_1_ = grouping_1.index, grouping_1.values
            # plotting the chart
            fig_14_1_1_ = px.bar(x=x_1_, y=y_1_, 
                      title=fcty_name,
                        labels={'x': 'Unit Type',
                           'y': 'Count'}, height=500,
                           color_discrete_sequence=["#000080"])
            fig_14_1_1_.update_layout(xaxis_tickangle=-45,
                                     title={
            'x': 0.5,
            'xanchor': 'center'
        },)
            st.plotly_chart(fig_14_1_1_, use_container_width=False, key=fcty_name)
    
    # looping through the array of 10 ten facilities based on number of combustion units owned
    for i in range(len(col_2nd_row)):
        # extracting the facility name
        fcty_name = top_10_fcty_col.iloc[i+3]['FACILITY_NAME']

        # plotting the bar graphs for the second row
        with col_2nd_row[i]:
            # extracting the combustion units for a single facility
            grouping_1 = unit_group[fcty_name]
            # extracting the combustion units and their corresponding counts
            x_2, y_2 = grouping_1.index, grouping_1.values
            # plotting the chart
            fig_14_1_2_ = px.bar(x=x_2, y=y_2, 
                      title=fcty_name[:40],
                        labels={'x': 'Unit Type',
                           'y': 'Count'}, height=500,
                           color_discrete_sequence=["#000080"])
            fig_14_1_2_.update_layout(xaxis_tickangle=-45,
                                     title={
            'x': 0.5,
            'xanchor': 'center' 
        },)
            st.plotly_chart(fig_14_1_2_, use_container_width=False, key=fcty_name)

    # looping through the array of 10 ten facilities based on number of combustion units owned
    for i in range(len(col_3rd_row)):
        # extracting the facility name
        fcty_name = top_10_fcty_col.iloc[i+6]['FACILITY_NAME']

        # plotting the bar graphs for the third row
        with col_3rd_row[i]:
            # extracting the combustion units for a single facility
            grouping_1 = unit_group[fcty_name]
            # extracting the combustion units and their corresponding counts
            x_3, y_3 = grouping_1.index, grouping_1.values
            # plotting the chart
            fig_14_1_3_ = px.bar(x=x_3, y=y_3, 
                      title=fcty_name,
                        labels={'x': 'Unit Type',
                           'y': 'Count'}, height=500,
                           color_discrete_sequence=["#000080"])
            fig_14_1_3_.update_layout(xaxis_tickangle=-45,
                                     title={
            'x': 0.5,
            'xanchor': 'center'
        },)
            st.plotly_chart(fig_14_1_3_, use_container_width=False, key=fcty_name)
    
    # looping through the array of 10 ten facilities based on number of combustion units owned
    for i in range(len(col_bottom_row)):
        fcty_name = top_10_fcty_col.iloc[i+9]['FACILITY_NAME']

        # plotting the bar graphs for the bottom row
        with col_bottom_row[i]:
            # extracting the facility name
            grouping_1 = unit_group[fcty_name]
            # extracting the combustion units and their corresponding counts
            x_4, y_4 = grouping_1.index, grouping_1.values
            # plotting the chart
            fig_14_1_4_ = px.bar(x=x_4, y=y_4, 
                      title=fcty_name,
                        labels={'x': 'Unit Type',
                           'y': 'Count'}, height=500, width=400,
                           color_discrete_sequence=["#000080"])
            fig_14_1_4_.update_layout(xaxis_tickangle=-45,
                                     title={
            'x': 0.5,  
            'xanchor': 'center' 
        },)
            st.plotly_chart(fig_14_1_4_, use_container_width=False, key=fcty_name)
    
    # content for Question 3 - second part  
    st.write("""
    A further breakdown into the combustion unit types used by these heavy energy users reveals some \
             interesting information. The universities possess a significant number of combustion units \
             that do not fit into well-defined categories such as boilers, turbines or process heaters. \
             These units are called **Other Combustion Source (OCS)**. Units that fall into this category are \
             commercial gas-fired water heaters, kitchen equipment, among others. The OCS term helps simplify \
             the emissions reporting process for equipment that falls in that group. Boilers and water heaters supply \
              hot water or steam for space heating of university buildings and for use in laboratories. \
             Furnaces are employed to heat air distributed through ducts for heating large spaces and in \
             laboratories for research in fields such as material science and chemistry. \
                Comfort heaters provide heat to living quarters or smaller spaces. Combined cycle turbines generate electrical \
             power for university-wide use.
    """)

    st.write("""
    Present in petrochemical, oil refinery and waste management facilities are units such as process heaters, \
             boilers, gas flare systems, simple and combined cycle turbines, internal combustion engines, \
             electricity generators, thermal oxidizers, and incinerators. These units perform functions \
             ranging from providing high temperatures required for distillation and chemical reactions \
             to managing and safely disposing of excess gases, generating steam and power for daily operations,\
              controlling combustion, and waste disposal.
    """)

    # Question 4
    st.subheader("4. What are the average and total \
                 combustion energy consumption by MECS region?")
   
    # extracting MMBtu_TOTAL values by MECS_Region and calculating the sum for each region
    tot_energy_mecs = cleaned_df.groupby('MECS_Region')[['MMBtu_TOTAL']].sum()

    # extract MMBtu_TOTAL values by MECS_Region and calculating the average for each region
    avg_energy_mecs = cleaned_df.groupby('MECS_Region')[['MMBtu_TOTAL']].mean()


    # extracting the MECS regions and their corresponding total energy consumed
    x_tot_mecs, y_tot_mecs = tot_energy_mecs.index, tot_energy_mecs.values

    # extracting the MECS regions and their corresponding average energy consumed
    x_avg_mecs, y_avg_mecs = avg_energy_mecs.index, avg_energy_mecs.values

    # converting 2-D array to 1-D array to allow for plotting 
    y_tot_mecs_conv, y_avg_mecs_conv = y_tot_mecs.flatten(), y_avg_mecs.flatten()

    # splitting the section into 2 columns - one for each graph
    col_mecs_tot, col_mecs_avg = st.columns(2)

    # plotting the first bar graph for the total combustion energy consumption for the regions
    with col_mecs_tot:
        fig_15_1 = px.bar(x=x_tot_mecs, y=y_tot_mecs_conv, 
                      title="Total MMBtu consumed by MECS Region",
                        labels={'x': 'MECS Region',
                           'y': 'Total amount of energy consumed (MMBtu)'},
                           color_discrete_sequence=['#008080'], height=500)
        fig_15_1.update_layout(xaxis_tickangle=-45,
                                     title={
            'x': 0.5,  
            'xanchor': 'center'
        },)
        st.plotly_chart(fig_15_1, use_container_width=False)
    
    # plotting the second bar graph for the average combustion energy consumption for the regions
    with col_mecs_avg:
        fig_15_2 = px.bar(x=x_avg_mecs, y=y_avg_mecs_conv, 
                      title="Average MMBtu consumed by MECS Region",
                        labels={'x': 'MECS Region',
                           'y': 'Average amount of energy consumed (MMBtu)'}, 
                           color_discrete_sequence=['#8C5DAF'], height=500)
        fig_15_2.update_layout(xaxis_tickangle=-45,
                                     title={
            'x': 0.5,
            'xanchor': 'center'
        },)
        st.plotly_chart(fig_15_2, use_container_width=False)

    # content for Question 4
    st.write("""
    The total energy consumption values show the aggregate amount of energy consumed by combustion in \
             each region, indicating the general size of its industrial economy or its population. On the \
             other hand, the average energy consumption values reveal the energy consumption per combustion \
              unit, indicating combustion energy density for each region.
    """)

    st.write("""
    The **South region** has a total energy use of 4.9 billion MMBtu, which indicates that it has the highest \
             overall use, due to its massive industrial layout, with it being home to the major oil \
             refineries and petrochemical plants (Motiva’s Port Arthur Refinery, Dow Inc.’s Texas Operations, \
             etc.). The region also recorded the highest energy consumption average at 654 thousand MMBtu. \
             This figure can also be due to the presence of energy-intensive industries, particularly in the \
             state of Texas.
    """)

    st.write("""
    The **West region** had the second-highest average energy consumption at 614 thousand MMBtu and a total \
             energy consumption of 2 billion MMBtu. These values indicate that although there is relatively \
             low total energy usage, high energy intensity is present, which could be due to the presence \
             of California, the most populous U.S. state, in the region. A large population typically \
             signifies increased residential energy utilization for heating and cooling purposes.
    """)

    st.write("""
    The **Midwest region** recorded the second-highest total energy consumption and the second-lowest average \
             energy consumption at 2.3 billion MMBtu and 436 thousand MMBtu, respectively. These figures \
             indicate a balanced energy consumption outlook, as substantial total energy consumption is \
             accompanied by a lower energy consumption density.
    """)

    st.write("""
    The **Northeast region** had the lowest total energy consumption and the lowest energy consumption average \
             at 0.8 billion MMBtu and 302 thousand MMBtu, respectively. These values show that the \
              Northeast has a low industrial footprint and population.
    """)

    # Question 5
    st.subheader("5. What are the average and total combustion energy consumption by State?")
    
    # extracting the MMBtu_TOTAL values by STATE and calculatimg the sum for each state
    tot_energy_state = cleaned_df.groupby('STATE')['MMBtu_TOTAL'].sum()

    # extracting the MMBtu_TOTAL values by STATE and calculating the average for each state
    avg_energy_state = cleaned_df.groupby('STATE')['MMBtu_TOTAL'].mean()

    # extracting the MECS regions and their corresponding total combustion energy consumed
    x_tot_state, y_tot_state = tot_energy_state.index, tot_energy_state.values

    # extracting the MECS regions and their corresponding average combustion energy consumed
    x_avg_state, y_avg_state = avg_energy_state.index, avg_energy_state.values

    # converting 2-D array to 1-D array to allow for plotting 
    y_tot_state_conv, y_avg_state_conv = y_tot_state.flatten(), y_avg_state.flatten()

    # plotting the bar graph of total combustion energy consumption for the different states
    fig_16_1 = px.bar(x=x_tot_state, y=y_tot_state_conv, 
                      title="Total MMBtu consumed by State",
                        labels={'x': 'State',
                           'y': 'Total amount of energy consumed (MMBtu)'},
                           color_discrete_sequence=['#4B0082'], height=500)
    fig_16_1.update_layout(title={
            'x': 0.5,
            'xanchor': 'center'
        },)
    st.plotly_chart(fig_16_1, use_container_width=False)
    
    # plotting the bar graph of average combustion energy consumption for the different states
    fig_16_2 = px.bar(x=x_avg_state, y=y_avg_state_conv, 
                      title="Average MMBtu consumed by State",
                        labels={'x': 'State',
                           'y': 'Average amount of energy consumed (MMBtu)'}, 
                           color_discrete_sequence=['#C41E3A'], height=500)
    fig_16_2.update_layout(title={
            'x': 0.5, 
            'xanchor': 'center' 
        })
    st.plotly_chart(fig_16_2, use_container_width=False)

    # content for Question 5
    st.write("""
    A glance at the distribution of states based on total combustion energy use reveals the three most significant states \
             with the highest energy consumption footprint: Texas (TX), Louisiana (LA), and California (CA). Texas and \
             Louisiana are states belonging to the South region (the region with the highest total energy use and average \
             energy use). They are heavy industrial hubs due to the presence of large refineries and petrochemical \
             facilities. California, a western state (the region with the second-highest energy consumption density), \
             finds itself among the group, mainly due to its massive population. 
    """)

    st.write("""
    Vermont (VT), New Hampshire (NH), Rhode Island (RI) and the District of Columbia (DC), the U.S. capital, \
             have the least total energy use. Vermont, New Hampshire and Rhode Island belong to the Northeast region \
             (the region with the lowest total and average energy use) and are known for being less-populated states \
             and the absence of heavy industries. The District of Columbia, although located in the South region, falls \
              under this group, due to being the country’s governmental seat, having a low population and industries with \
              a significantly low energy footprint. 
    """)

    st.write("""
    Montana (MT) has the highest energy consumption density, but has one of the lowest total energy use values. Despite \
             being a less populated state, the abundance of mineral resources such as gold, copper, oil, gas, and coal, \
             and the presence of energy-intensive industries, are factors influencing its high average energy consumption. \
             Wyoming (WY), the least populated U.S. state, has a significant energy consumption density due to its status \
             as a big fossil fuel-producing state, being the largest coal producer and the presence of oil and gas extraction \
             activities.
    """)

    # Question 6
    st.subheader("6. What industries are the major contributors to combustion \
                 energy consumption based on the North American Industry \
                 Classification System (NAICS)?")
    
    # extracting the industries in reference to NAICS, ranking them based on total combustion energy usage and selecting the top 10
    energy_cons_naics = cleaned_df.groupby('PRIMARY_NAICS_TITLE')[['MMBtu_TOTAL']] \
                                    .sum() \
                                    .sort_values(by='MMBtu_TOTAL', ascending=False) \
                                    .head(10)

    # extracting the top 10 industries and their corresponding counts
    x_energy_cons_naics, y_energy_cons_naics = energy_cons_naics.index,energy_cons_naics.values

    # converting the 2-D array to 1-D array to allow for plotting 
    y_energy_cons_naics_conv = y_energy_cons_naics.flatten()    
    
    # plotting the bar graph for the top 10 industries
    fig_17 = px.bar(x=x_energy_cons_naics, y=y_energy_cons_naics_conv, 
                      title='Top 10 NAICS Industries based on combustion energy consumption',
                        labels={'x':'NAICS Title',
                           'y': 'Total amount of energy consumed (MMBtu)'}, height=800,
                           color_discrete_sequence=["#151B54"])
    fig_17.update_layout(xaxis_tickangle=-45, title={
            'x': 0.5,
            'xanchor': 'center'
        })
    st.plotly_chart(fig_17, use_container_width=False)

    # content for Question 6
    st.write("""
        The top ten industries by NAICS title depict an economy dominated by those involved in natural resource extraction \
             and processing.
    """)

    st.write("""
        The fossil fuel value chain industries constitute half of this group, from the extraction of natural gas and oil \
             to pipeline infrastructure for transporting these raw products, facilities that refine them into a range of \
             beneficial products, and electricity generation for industrial and consumer use.  
    """)

    st.write("""
        The next 40 percent consists of industries primarily focused on transforming mineral or organic raw materials into \
             industrial products for further processing and end-user products. These industries are the iron and steel mills,\
              basic organic manufacturing facilities, and paper and paperboard mills.  
    """)

    st.write("""
        The remaining 10 percent are specialized industries involved in the conversion of agricultural products, \
             like sugarcane, corn and wheat, into Ethyl alcohol (or ethanol), an important product used in manufacturing \
              a wide range of products (medical items, alcoholic beverages, perfumes, etc.)
    """)

    # Question 7
    st.subheader("7. What Industry Groups are the major contributors to combustion \
                 energy consumption?")

    # extracting the industry groups, ranking them based on total combustion energy usage and selecting the top 10
    energy_cons_grp = cleaned_df.groupby('GROUPING')[['MMBtu_TOTAL']] \
                                    .sum() \
                                    .sort_values(by='MMBtu_TOTAL', ascending=False) \
                                    .head(10)

    # extracting the top 10 industry groups and their corresponding counts
    x_energy_grp, y_energy_grp = energy_cons_grp.index, energy_cons_grp.values

    # converting the 2-D array to 1-D array to allow for plotting 
    y_energy_grp_conv = y_energy_grp.flatten()    
    
    # plotting the bar graph for the top 10 industry groups
    fig_18 = px.bar(x=x_energy_grp, y=y_energy_grp_conv, 
                      title='Top 10 Industry Groups based on combustion energy consumption',
                        labels={'x':'Group',
                           'y': 'Total amount of energy consumed (MMBtu)'}, 
                           color_discrete_sequence=['#c21807'],
                             height=800)
    fig_18.update_layout(xaxis_tickangle=-45, title={
            'x': 0.5, 
            'xanchor': 'center'
        })
    st.plotly_chart(fig_18, use_container_width=False)

    # content for Question 7
    st.write("""
    The Petroleum and Coal Products and Chemical Manufacturing industries are \
        at the top of combustion energy consumption in the U.S. The position \
            occupied by these industries indicates their intensive dependence \
                on energy for high temperatures and pressures for crude \
                     refining, natural gas processing, and the manufacturing of a \
                        wide variety of chemical compounds.
    """)
    
    st.write("""
    The Mining and Extraction industry, which is among the top three energy consumers, \
        focuses on extracting fossil fuels and minerals from the earth and uses a large amount \
             of energy for operating heavy machinery, transporting massive amounts of raw materials\
                 and processing ores.
    """)    

    st.write("""
    The Utilities industry, occupying the fourth position and primarily concerned with activities \
        such as power generation and water treatment, is a pronounced consumer of energy itself, while \
            also providing energy to other industries.  Following closely are the Paper Manufacturing \
                and Primary Metals industries, and their use of energy for converting raw materials,\
                     wood and metallic ores into beneficial products.
    """) 

    st.write("""
    The low-ranking industries are Food Manufacturing, Transportation and Warehousing, Administrative \
        and Support, Waste Management and Remediation Services, and Nonmetallic Mineral Products. \
            These industries typically require a significant amount of energy for their various \
                processes and activities, including refrigeration, cooking, and packaging, movement \
                     of goods across the entire country via ships, planes and trucks, administrative \
                         and facilities support services, waste collection and management, and \
                            manufacturing cement and glass.
    """) 

    # Question 8
    st.subheader("8. Across industry groups, what is the distribution of combustion units for cogeneration versus non-cogeneration use?")

    # extracting the industry groups based on units used for cogeneration
    cogen_grp_yes = cleaned_df.groupby('COGENERATION_UNIT_EMISS_IND')['GROUPING'] \
                            .value_counts()['Yes']

    # extracting the industry groups based on units not used for cogeneration
    cogen_grp_no = cleaned_df.groupby('COGENERATION_UNIT_EMISS_IND')['GROUPING'] \
                            .value_counts()['No']    

    
    # extracting the industry groups and their corresponding counts
    x_cogen_grp_yes, y_cogen_grp_yes = cogen_grp_yes.index, cogen_grp_yes.values
    
    # extracting the industry groups and their corresponding counts
    x_cogen_grp_no, y_cogen_grp_no = cogen_grp_no.index, cogen_grp_no.values
    
    # plotting the bar graph for the first group (units used for cogeneration)
    fig_19_1 = px.bar(x=x_cogen_grp_yes, y=y_cogen_grp_yes, 
                      title='Distribution of Combustion Units Used For Cogeneration',
                        labels={'x':'Industry Group',
                           'y': 'No. of combustion units'}, 
                           color_discrete_sequence=['#ff6e00'],
                             height=800)
    fig_19_1.update_layout(xaxis_tickangle=-45, title={
            'x': 0.5,
            'xanchor': 'center'
        })
    st.plotly_chart(fig_19_1, use_container_width=False)

    # plotting the bar graph for the second group (units not used for cogeneration)
    fig_19_2 = px.bar(x=x_cogen_grp_no, y=y_cogen_grp_no, 
                      title='Distribution of Combustion Units Not Used For Cogeneration',
                        labels={'x':'Industry Group',
                           'y': 'No. of combustion units'}, 
                           color_discrete_sequence=["#a1195d"],
                            height=800)
    fig_19_2.update_layout(xaxis_tickangle=-45, title={
            'x': 0.5, 
            'xanchor': 'center'
        })
    st.plotly_chart(fig_19_2, use_container_width=False)

    # content for Question 8
    st.write("""
    Utilities, Chemical Manufacturing, and Petroleum and Coal Products are the top three industries \
             in the combustion unit for the cogeneration utilization group. These industries have an \
             enormous and constant need for process heat and electricity. This need is for daily \
             operations and their customers. Cogeneration serves as a highly efficient and \
             cost-effective means to cater to their energy needs.
    """)

    st.write("""
    Paper Manufacturing commands a significant portion of the cogeneration units' share. \
        This occurrence is due to its need for steam to dry paper products and electricity to power \
            its machinery. The Educational Services has a substantial share of cogeneration units \
                within the group. This amount of cogeneration units is most likely due to the \
                    operation of central heating and power plants at various institutions' locations. \
                        These systems are responsible for supplying heat and power to student halls, \
                            office buildings and research laboratories.
    """)

    st.write("""
    Present at the very end of the cogeneration-based units distribution are industries like \
             Accommodation and Food Services, Printing, and Real Estate and Leasing, whose heat \
             energy needs are extremely small-scale, for space heating and hot water supply, with \
             little or no need for self-generated electricity, as they depend on the Utilities \
             industry for electricity supply.
    """)

    st.write("""
    The Utilities industry also finds itself at the top of the list for combustion units not utilized \
             for cogeneration, due to the need to generate power from fossil fuel-based resources such \
             as natural gas and coal.
    """)

    st.write("""
    The Mining and Extraction, Chemical Manufacturing, and Petroleum and Coal Products industries \
             also have relatively high numbers of non-cogeneration-based combustion units. \
             Improved in-situ generation of electricity in facilities that generate massive \
             amounts of process heat will help cut electricity costs. It can also enable these \
             facilities to have sufficient power for internal usage and to generate electricity \
             for trade. 
    """)

# setting up the Conclusions and Recommendations page
elif page == "Conclusion and Recommendations":
    # the conclusion subsection
    st.header("Conclusion ✅")
    # the conclusion content
    st.write("""
    The exploratory data analysis looked to identify the major drivers and patterns of combustion energy use \
             across U.S. industrial facilities in 2014. The dataset used, which contained over 18,000 \
             combustion units (after the data cleaning process), belonging to different industrial facilities \
             across the U.S., provided several key insights.
    """)

    st.write("""
    Petroleum refineries and petrochemical plants are the facilities that consume the most combustion energy \
             and also have a significant number of combustion units. By extension, ExxonMobil and the Marathon \
             Petroleum Company are the two major contributors to combustion energy consumption in the U.S. \
             in 2014. This situation is due to their ownership of several massive petroleum and petrochemical facilities \
             across the country, particularly in the southern region. Additionally, a breakdown of the facilities \
             with the highest number of combustion units revealed that educational institutions are significant \
             users of combustion energy, using these units for research and other campus activities. 
    """)

    st.write("""
    A significant number of outliers were also present in the combustion energy use data. This finding \
             indicates a relatively irregular combustion energy use across the different industrial facilities \
             housing these combustion units.
    """)

    st.write("""
    The use of combustion units for cogeneration signifies an effective and cost-friendly method \
             of providing critical production inputs in terms of process heat and electricity. \
             Dominating this area are the Utilities and Chemical Manufacturing industries, although \
             there’s still room to improve their energy efficiency.
    """)

    st.write("""
    The limitation of this analysis includes the dataset’s lack of the cost per MMBtu for each \
             combustion unit. The absence of this critical piece of data prevented the assessment \
             of cost savings associated with the different fuel types and efficiency measures, \
             i.e. combustion units employed for cogeneration versus units used for only process heat. \
             Another critical missing data point was the carbon emissions associated with the different \
             combustion units and fuel types, which would have been beneficial towards environmental \
             impact analysis of the various industrial facilities.
    """)
    
    # the recommendations subsection
    st.header("Recommendations and Next Steps ⚙️")
    # the recommendations content
    st.write("""
    The following recommendations are brought forward for action based on the conclusions drawn from this \
             EDA project:
    """)
    st.write("""
    - Governmental agencies at the federal and state levels should consider creating energy \
             efficiency programs and the necessary technical support for the Petroleum and \
             Petrochemical industries, which are the highest combustion energy consumers. \
             This exercise would further improve the current energy efficiency programs of these \
             industries.
    - Further analysis should focus on the outliers identified in the dataset to determine the \
             underlying causes of such high combustion energy values. 
    - Facilities with high combustion energy use rates but limited or no cogeneration units should \
             be ideal targets for cogeneration modification campaigns and be given incentives for \
             complying.
    - Data on the age and efficiency rating of the combustion units should be collected to aid \
             efficient industrial policy recommendations, through the analysis of the underlying \
             technology and its service life on energy efficiency.
    """)

# setting up the References section     
elif page == "References":
    # the references header
    st.header("References 📚")
    # the references content
    st.markdown("""
    - Alcoa Corporation. (2024). Warwick Operations primary metals facility. Alcoa. Retrieved September 20, 2025, from https://www.alcoa.com/global/en/pdf/Alcoa-Warrick-Fact-Sheet.pdf 
    - BP Whiting Business Unit. (2024). Whiting oil refinery overview. BP Corporate. Retrieved September 21, 2025, from https://www.bp.com/en_us/united-states/home/what-we-do/production-and-operations/refineries/whiting-refinery.html
    - Dow Inc. (2024). Texas Operations and St. Charles Operations facilities. Dow Corporate. Retrieved September 21, 2025, from https://corporate.dow.com/en-us/locations/freeport.html 
    - Enterprise Products Operating LLC. (2024). Mont Belvieu Complex facilities and operations. Enterprise Products.  Retrieved September 20, 2025, from https://www.enterpriseproducts.com/about-us/our-history/
    - ExxonMobil Corporation. (2024). Baytown Complex and Baton Rouge facilities. ExxonMobil. Retrieved September 21, 2025, from https://corporate.exxonmobil.com/-/media/global/files/locations/united-states-operations/baytown/baytown-complex-2024-fact-sheet.pdf 
    - Formosa Plastics Group. (2024). Port Comfort petrochemicals and plastics plant. Formosa Plastics. Retrieved September 21, 2025, from https://en.wikipedia.org/wiki/Formosa_Plastics_Corp
    - Intel Corporation. (2014). 2014 Greenhouse Gas Report. Retrieved September 23, 2025, from https://www.exploreintel.com/assets/documents/newmexico/reports/2014%20Greenhouse%20Gas%20Report.pdf
    - Kyle's Converter. (n.d.). Million British Thermal Units to Gigawatt Hours (MMBtu to GWh) conversion. Retrieved September 21, 2025, from https://www.kylesconverter.com/energy,-work,-and-heat/million-british-thermal-units-to-gigawatt-hours
    - McMillan, Colin. (2016). "Industrial Facility Combustion Energy Use." NREL Data Catalog. Golden, CO: National Renewable Energy Laboratory. Last updated: December 18, 2024. DOI: 10.7799/1278644.
    - Marathon Petroleum Corporation. (2024). Company subsidiaries and refinery operations. Marathon Petroleum. Retrieved September 21, 2025, from https://www.ebsco.com/research-starters/history/marathon-petroleum-corporation 
    - Motiva Enterprises LLC. (2024). Port Arthur Refinery overview. Motiva Enterprises. Retrieved September 15, 2025, from https://en.wikipedia.org/wiki/Port_Arthur_Refinery 
    - National Renewable Energy Laboratory (NREL). (2022). Cogeneration and industrial energy efficiency. U.S. Department of Energy. Retrieved September 26, 2025, from https://www.nrel.gov/docs/fy24osti/90442.pdf 
    - U.S. Census Bureau. (2017). North American Industry Classification System (NAICS). U.S. Department of Commerce. Retrieved September 16, 2025, from https://www.census.gov/naics/ 
    - U.S. Energy Information Administration (EIA). (2014). Manufacturing Energy Consumption Survey (MECS): Detailed combustion energy data and fuel use in industrial facilities. U.S. Department of Energy. Retrieved September 11, 2025, from https://www.eia.gov/consumption/manufacturing/    
    - Union Carbide Corporation. (2024). St Charles Operations petrochemical facility. Dow Inc. subsidiary information.Retrieved September 21, 2025, from https://corporate.dow.com/en-us/locations/texas-city.html 
                """)