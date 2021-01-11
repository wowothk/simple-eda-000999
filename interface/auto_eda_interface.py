import pandas as pd
import streamlit as st

from model.auto_eda import main_overview, series_stat

def overview_interface(dataframe):
    stat, type_list = main_overview(dataframe)

    st.markdown("## Main Overview")
    
    peretage_duplicate = (stat["tot_duplicate"]/stat["tot_data_observations"])*100

    
    st.write(f'Number of Observations : {stat["tot_data_observations"]}')
    st.write(f'Number of duplicate    : {stat["tot_duplicate"]}  ({peretage_duplicate} %)')    
    st.write(f'Number of variables    : {stat["number_variables"]}')
    st.write(f'Categorical variables  : {stat["categorical_variables"]}')
    st.write(f'Numberic of variables  : {stat["numeric_variables"]}')

    return type_list





def variables_overview_interface(series, type_list):
    var_stat = series_stat(series, type_list)
    st.write(var_stat)

#     st.markdown("## Variables")
#     variables_name = dataframe.columns.tolist()
#     values, missing, unique, data_type, detail_info = variables_overview(dataframe)

#     st.write(values)
#     st.write(missing)
#     st.write(unique)
#     st.write(data_type)
#     st.write(detail_info)
    # var_main, var_stat1, var_stat2 = st.beta_columns(3)

    # for variable in variables_name:
    #     st.markdown(f'### {variable}')
    #     percentage_unique = unique[variable] / tot_data_observations * 100

    #     var_main.write(f' Type      : {data_type[variable]}')
    #     var_main.write(f' Values    : {values[variable]}')
    #     var_main.write(f' Missing   : {missing[variable]}')
    #     var_main.write(f' Unique    : {unique[variable]} ({percentage_unique}%)')

    #     if unique[variable] == "NUMERIC":
    #         #Statistic 1
    #         var_stat1.write(f' Max      : {detail_info[variable]["max"]}')
    #         var_stat1.write(f' 95%      : {detail_info[variable]["95%"]}')      
    #         var_stat1.write(f' Q3       : {detail_info[variable]["Q3"]}')
    #         var_stat1.write(f' Mean     : {detail_info[variable]["mean"]}')  
    #         var_stat1.write(f' Median   : {detail_info[variable]["median"]}')  
    #         var_stat1.write(f' Q1       : {detail_info[variable]["Q1"]}')  
    #         var_stat1.write(f' 5%       : {detail_info[variable]["5%"]}')  
    #         var_stat1.write(f' Min      : {detail_info[variable]["min"]}')    
            
    #         #Statistic 2
    #         var_stat1.write(f' Range    : {detail_info[variable]["range"]}')
    #         var_stat1.write(f' iqr      : {detail_info[variable]["iqr"]}')      
    #         var_stat1.write(f' std      : {detail_inf["std"]}')
    #         var_stat1.write(f' Variance : {detail_info[variable]["variance"]}')  
    #         var_stat1.write(f' Kurtosis : {detail_info[variable]["kurtosis"]}')  
    #         var_stat1.write(f' Skew     : {detail_info[variable]["skew"]}')  
    #         var_stat1.write(f' Sum      : {detail_info[variable]["sum"]}')  
    #         var_stat1.write(f' cv       : {detail_info[variable]["cv"] }')               