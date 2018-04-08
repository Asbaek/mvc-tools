import pandas as pd

def csv_column_stat(filename,column_name):
    """
    Loads a csv(filename), identifies values in one column, creates a dataframe, with index=csv column values and values=count of value. Returns the new dataframe and the number of rows in the csv file (for caluclation of %)"""
    df=pd.read_csv(filename,delimiter=";",encoding='ISO-8859-1')
    total_rows=len(df)
    df = df[df[column_name].notnull()]
    output_list = df[column_name].tolist()
    output_list = [x.split(",") for x in output_list if x != 'nan']
    final_list = []
    for output in output_list:
        for p in output:
            final_list.append(p.strip())
    s = pd.Series(final_list)
    df2=pd.DataFrame(s.value_counts())
    df2.columns = [column_name +'_counts']
    return df2,total_rows

def get_changed_rows(new_df, existing_df, compare_columns):
    """
    get_changed_rows compares two dataframes(new_df and existing_df), and outputs the difference in  selected columns (compare_columns). The two dataframes must have the same columns.
    """
    assert isinstance(new_df, pd.DataFrame), "Error: new_df is not pd.DataFrame type"
    assert isinstance(existing_df, pd.DataFrame), "Error: existing_df is not pd.DataFrame type"
    assert isinstance(compare_columns, list), "Error: compare_columns is not pd.DataFrame type"
    assert list(new_df)==list(existing_df),"Error: new_df columns does not equal existing_df columns"
    full_df = existing_df.append(new_df)
    changed_df = full_df.drop_duplicates(subset=compare_columns, keep=False)
    return changed_df
