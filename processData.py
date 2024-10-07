import getSheetData
import pandas as pd
from datetime import datetime, timedelta


def get_curr_date(days: int = None):
    now = datetime.now()
    if days is not None:
        date_str = [day for day in datetime.now() - timedelta(days=5)]
    else:
        date_str = [now.strftime("%Y-%m-%d")]
    return date_str


def get_update():
    values = getSheetData.read_values()
    df = pd.DataFrame(values)
    df.columns = ["Date", "Name", "Update", "Status"]
    ref_date = get_curr_date()
    fil_df = df[df["Date"].isin(ref_date)].reset_index(drop=True)
    # fil_df = df
    msg = []
    for x in fil_df.index:
        msg.append(fil_df.iloc[x])
    return msg


if __name__ == "__main__":
    get_update()
