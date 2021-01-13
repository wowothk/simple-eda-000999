import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

from model.auto_eda import main_overview, series_stat

from pyecharts.charts import Bar
from pyecharts import options as opts
import streamlit.components.v1 as components

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


def variables_overview_interface(series,type_list):
    var_stat = series_stat(series, type_list)
    peretage_unique = round((var_stat["unique"]/var_stat["values"])*100,0)

    st.write(f'Type     : {var_stat["data_type"]}')
    st.write(f'Values   : {var_stat["values"]}')
    st.write(f'missing  : {var_stat["missing"]}')
    st.write(f'Unique   : {var_stat["unique"]} ({peretage_unique} %)')
    st.write()
    st.markdown("### Detail Information")

    # var_stat1, var_stat2, var_dis = st.beta_columns(3)

    if var_stat["data_type"] == "NUMERIC":
        var_stat1, var_stat2 = st.beta_columns(2)
        #Statistic 1
        var_stat1.write(f' Max      : {var_stat["detail_info"]["max"]}')
        var_stat1.write(f' 95%      : {var_stat["detail_info"]["95%"]}')      
        var_stat1.write(f' Q3       : {var_stat["detail_info"]["Q3"]}')
        var_stat1.write(f' Mean     : {var_stat["detail_info"]["average"]}')  
        var_stat1.write(f' Median   : {var_stat["detail_info"]["median"]}')  
        var_stat1.write(f' Q1       : {var_stat["detail_info"]["Q1"]}')  
        var_stat1.write(f' 5%       : {var_stat["detail_info"]["5%"]}')  
        var_stat1.write(f' Min      : {var_stat["detail_info"]["min"]}')

#         #Statistic 2
        var_stat2.write(f' Range    : {var_stat["detail_info"]["range"]}')
        var_stat2.write(f' iqr      : {var_stat["detail_info"]["iqr"]}')      
        var_stat2.write(f' std      : {var_stat["detail_info"]["std"]}')
        var_stat2.write(f' Variance : {var_stat["detail_info"]["variance"]}')  
        var_stat2.write(f' Kurtosis : {var_stat["detail_info"]["kurtosis"]}')  
        var_stat2.write(f' Skew     : {var_stat["detail_info"]["skew"]}')  
        var_stat2.write(f' Sum      : {var_stat["detail_info"]["sum"]}')  
        var_stat2.write(f' cv       : {var_stat["detail_info"]["cv"] }')

        distribution_plot_options = distribution_plot(var_stat["detail_info"]["data_distribution"])
        with st.beta_expander("See data distribution"):
            st_echarts(distribution_plot_options) 

    elif var_stat["data_type"] == "CATEGORICAL":
        var_stat1, var_stat2 = st.beta_columns(2)
        var_stat1.dataframe(var_stat["detail_info"]["data_distribution"])
        freq_data_plot_options = freq_data_plot(var_stat["detail_info"]["data_distribution"])
        
        with st.beta_expander("See 5 frequents data"):
            st_echarts(freq_data_plot_options)



def freq_data_plot(data_distribution):
    options = {
    "title": {
            "text": 'Most 5 Frequents data'},
    "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'shadow'
                }
            },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": "true"
            },
    "xAxis": {"type": "value"},
    "series": [
        {"data": data_distribution["Unique_Tot"], "type": "bar"}],
    "yAxis":{
        "type": "category",
        "data": data_distribution["Unique_var"],
        }
    } 

    return options

def distribution_plot(data_distribution):
    options = {
    "title": {
            "text": 'Data distribution'},
    "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'shadow'
                }
            },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": "true"
            },
    "xAxis": {
        "type": "category",
        "data": data_distribution["Unique_var"],
        },
    "yAxis":{"type": "value"},
    "series": [
        {"data": data_distribution["Unique_Tot"], "type": "bar"}],
    } 

    return options