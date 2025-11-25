import pandas as pd

def find_zero_sales_days(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies store-day combinations with zero total sales.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain ['store_id', 'day', 'sales'] columns.

    Returns
    -------
    pd.DataFrame
        DataFrame with ['store_id', 'day'] for days where total sales == 0.
    """
    outliers = (
        df.groupby(['store_id', 'day'])['sales']
        .sum()
        .reset_index()
        .loc[lambda x: x['sales'] == 0, ['store_id', 'day']]
    )
    return outliers
