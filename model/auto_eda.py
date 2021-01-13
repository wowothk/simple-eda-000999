import pandas as pd
import numpy as np


def main_overview(dataframe):
    stat =  dict()

    variables_name = dataframe.columns.tolist()
    numeric_variables = dataframe._get_numeric_data().columns.tolist()
    num_numeric_variables = len(numeric_variables)
    categorical_variables = [var for var in dataframe.columns.tolist() if dataframe[var].dtype is np.dtype('object')]
    num_categorical_variables = len(categorical_variables)
    for variable in variables_name:
        if dataframe[variable].unique().tolist() == [0,1] or dataframe[variable].unique().tolist() == [1,0]:
            numeric_variables.append(variable)
            num_numeric_variables -= 1
            categorical_variables.append(variable)
            num_categorical_variables +=1
    
    type_list = []
    for variable in variables_name:
        if variable in categorical_variables: 
            type_list.append("CATEGORICAL")
        elif variable in numeric_variables:
            type_list.append("NUMERIC")
        else:
            type_list.append("UNKNOWN")


    stat["number_variables"] = dataframe.shape[1]
    stat["tot_data_observations"] =  dataframe.shape[0]
    stat["tot_duplicate"] = dataframe.duplicated().sum().tolist()
    stat["categorical_variables"] = num_categorical_variables
    stat["numeric_variables"] = num_numeric_variables 
    
    # for i in range(0,len(variables_name)):
    #     series_stat(dataframe[variables_name[i]], stat, variable, type_list[i])
    return stat, type_list

def series_stat(series, type):
    stat_info = dict()

    stat_info["values"] = series.notnull().sum().tolist()
    stat_info["missing"] = series.isnull().sum().tolist()
    stat_info["unique"] = len(series.unique().tolist())
    stat_info["data_type"] = type

    series_detail_stat(series, stat_info)
    
    return stat_info

def series_detail_stat(series, stat_info):
    stat_info["detail_info"] = dict()
    detail_stat_info = stat_info["detail_info"]
    

    if stat_info["data_type"] == "CATEGORICAL":
        
        if stat_info["unique"] > 5:
            top_unique_variable = series.value_counts()[:5].index.tolist()
            top_unique_tot = series.value_counts()[:5].tolist()
            top_unique_tot.append(len(series.index) - sum(top_unique_tot))
            top_unique_variable.append("other")
        else:
            top_unique_variable = series.value_counts().index.tolist()
            top_unique_tot = series.value_counts().tolist()

        detail_stat_info["data_distribution"] = dict()
        detail_stat_info["data_distribution"]["Unique_var"] = top_unique_variable
        detail_stat_info["data_distribution"]["Unique_Tot"] = top_unique_tot

    elif stat_info["data_type"] == "NUMERIC":
            detail_stat_info["max"] = series.max().tolist()
            detail_stat_info["95%"] = series.quantile(0.95)
            detail_stat_info["Q3"] = series.quantile(0.75)
            detail_stat_info["average"] = round(series.mean(),3)
            detail_stat_info["median"] = series.median()
            detail_stat_info["Q1"] = series.quantile(0.25)
            detail_stat_info["5%"] = series.quantile(0.05)
            detail_stat_info["min"] = series.min().tolist()

            detail_stat_info["range"] = detail_stat_info["max"] - detail_stat_info["min"]
            detail_stat_info["iqr"] = detail_stat_info["Q3"] - detail_stat_info["Q1"]
            detail_stat_info["std"] = round(series.std(),3)
            detail_stat_info["variance"] = round(series.var(),3)
            detail_stat_info["kurtosis"] = round(series.kurt(),3)
            detail_stat_info["skew"] = round(series.skew(),3)
            detail_stat_info["sum"] = series.sum().tolist()
            detail_stat_info["cv"] = round(detail_stat_info["std"] / detail_stat_info["average"],3) if detail_stat_info["average"] else null

            if not isinstance(series, np.float64):
                unique_variable = series.value_counts().index.tolist()
                unique_tot = series.value_counts().tolist()
                zipped_lists = zip(unique_variable, unique_tot)
                sorted_pairs = sorted(zipped_lists)

                tuples = zip(*sorted_pairs)
                unique_variable, unique_tot = [ list(tuple) for tuple in  tuples]

                detail_stat_info["data_distribution"] = dict()
                detail_stat_info["data_distribution"]["Unique_var"] = unique_variable
                detail_stat_info["data_distribution"]["Unique_Tot"] = unique_tot
                
    else:
        detail_stat_info["data_distribution"] = "error, unknown data type"


def histogram(dataframe):
    pass

def box_plot(dataframe):
    pass


