import getSheetData
import pandas as pd
from datetime import datetime, timedelta


def get_curr_date(days: int = None):
    now = datetime.now()
    date_str = []
    if days is not None:
        for x in range(10):
            dt_val = (datetime.now() - timedelta(days=x)).date()
            date_str.append(dt_val.strftime("%Y-%m-%d"))
    else:
        date_str = [now.strftime("%Y-%m-%d")]
    return date_str


def get_update(days: int = None):
    values = getSheetData.read_values()
    df = pd.DataFrame(values)
    df.columns = ["Date", "Name", "Update", "Status"]
    ref_date = get_curr_date(days)
    print(ref_date)
    fil_df = df[df["Date"].isin(ref_date)].reset_index(drop=True)
    # fil_df = df
    fil_df.to_csv("message.csv")
    msg = []
    for x in fil_df.index:
        msg.append(fil_df.iloc[x])
    return msg


if __name__ == "__main__":
    print(get_update(10))
