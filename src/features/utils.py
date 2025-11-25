import pandas as pd

def preprocess_sales(sales_df, start_date="2011-01-28"):
    """
    Melt the wide sales dataset into long format and add calendar features.
    
    Parameters
    ----------
    sales_df : pd.DataFrame
        Input DataFrame with sales columns like 'd_1', 'd_2', ..., plus id variables.
    start_date : str or datetime, optional
        Base date corresponding to d_1. Default is '2011-01-28'.
    
    Returns
    -------
    pd.DataFrame
        Processed long-format DataFrame with date and calendar features.
    """
    
    df = (
        sales_df
        .melt(
            id_vars=['id', 'item_id', 'dept_id', 'cat_id', 'store_id', 'state_id'],
            var_name='day',
            value_name='sales'
        )
        .assign(
            date=lambda x: pd.to_datetime(start_date) 
                            + pd.to_timedelta(x['day'].str[2:].astype(int), unit='D')
        )
        .assign(
            year=lambda x: x['date'].dt.year,
            month=lambda x: x['date'].dt.month,
            day_of_month=lambda x: x['date'].dt.day,
            day_of_week=lambda x: x['date'].dt.dayofweek
        )
    )
    
    return df
