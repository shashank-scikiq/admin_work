import getSheetData
import pandas as pd
from datetime import datetime


def get_curr_date():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    return date_str


def get_update():
    values = getSheetData.read_values()
    df = pd.DataFrame(values)
    df.columns = ["Date", "Name", "Update", "Status"]
    # print(df)
    ref_date = get_curr_date()
    fil_df = df[df["Date"] == ref_date].reset_index(drop=True)
    # fil_df = df
    msg = []
    for x in fil_df.index:
        # print(x)
        # print(fil_df.iloc[x])
        msg.append(fil_df.iloc[x])
    return msg


if __name__ == "__main__":
    get_update()
