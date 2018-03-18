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
