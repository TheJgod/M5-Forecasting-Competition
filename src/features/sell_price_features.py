import pandas as pd
import numpy as np

def detect_promotions(df: pd.DataFrame, roll_window: int = 90, eps: float = 1e-6) -> pd.DataFrame:
    """
    Detects price promotions and computes absolute and relative reductions constant over each promo period.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain ['store_id', 'item_id', 'sell_price', 'd'] (or equivalent day identifier).
    roll_window : int, optional
        Rolling window size (default=90) for baseline median price estimation.
    eps : float, optional
        Tolerance for detecting price reductions (default=1e-6).

    Returns
    -------
    pd.DataFrame
        Original DataFrame with added columns:
        ['promo_abs_const', 'promo_rel_const'].
    """
    data = df.copy()
    data['day_num'] = data['d'].str.extract(r'(\d+)$').astype(int)
    data = data.sort_values(['store_id', 'item_id', 'day_num']).reset_index(drop=True)

    data['baseline'] = (
        data.groupby(['store_id', 'item_id'])['sell_price']
        .transform(lambda s: s.rolling(window=roll_window, min_periods=1).median())
    )
    data['is_promo'] = data['sell_price'] < (data['baseline'] - eps)
    data['run_id'] = (
        data.groupby(['store_id', 'item_id'])['is_promo']
        .apply(lambda x: (x != x.shift(1)).cumsum())
        .reset_index(level=[0, 1], drop=True)
    )

    seg_idx = ['store_id', 'item_id', 'run_id']
    data['seg_min_price'] = (
        data[data['is_promo']].groupby(seg_idx)['sell_price'].transform('min')
    )
    data['seg_baseline'] = (
        data[data['is_promo']].groupby(seg_idx)['baseline'].transform('median')
    )
    data['seg_min_price'] = data.groupby(seg_idx)['seg_min_price'].transform('first')
    data['seg_baseline'] = data.groupby(seg_idx)['seg_baseline'].transform('first')

    data['promo_abs_const'] = np.where(
        data['is_promo'], data['seg_baseline'] - data['seg_min_price'], 0.0
    )
    data['promo_rel_const'] = np.where(
        data['is_promo'], data['promo_abs_const'] / data['seg_baseline'], 0.0
    )
    data['promo_abs_const'] = data['promo_abs_const'].clip(lower=0.0)
    data['promo_rel_const'] = data['promo_rel_const'].clip(lower=0.0)

    return data.drop(columns=['day_num', 'run_id', 'seg_min_price', 'seg_baseline'])
