
import pandas as pd

import feather


pingInfoFilePath = "./serverpings.ftr"

pingInfo = {"servername": ["svr_et_1", "svr_et_2", "svr_wt_1", "svr_wt_2", "svr_nr_1", "svr_nr_2", "svr_st_1", "svr_st_2"],

            "lastping": ["12.20.15.122", "12.20.11.395", "12.20.12.836", "12.20.16.769", "12.20.17.193", "12.20.18.416", "11.59.55.913", "12.20.14.811"],

            "roundtriptime": [300, 400, 0, 200, 100, 500, 350, 0],

            "status": ["PASS", "PASS", "FAIL", "PASS", "PASS", "PASS", "PASS", "FAIL"]}


dataFrame = pd.DataFrame(data=pingInfo)

dataFrame.to_feather(pingInfoFilePath)


readFrame = pd.read_feather(pingInfoFilePath, columns=None, use_threads=True)

print(readFrame)
