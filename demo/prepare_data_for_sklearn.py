#Adapt Data for Scikit Learn model fitting and predict
def prepare_data_for_sklearn(df, is_test=False):
    x_columns = ['Hour','Month','Year','X','Y','DayOfWeek']
    y_column = 'Category'   
    #x_categorical_columns = ['']
       #x_columns.extend(x_categorical_columns)
    
    X = df[x_columns]
    #if len(x_categorical_columns)>0:
       # X = pd.get_dummies(X, columns=x_categorical_columns)
    
    y = None if is_test else df[y_column].values
    
    return X, y
%time X,y = prepare_data_for_sklearn(train)
%time X_test,dummy = prepare_data_for_sklearn(test,is_test=True)