import numpy as np
import pandas as pd
import tushare as ts

def get_realtime_info():
    codes = pd.DataFrame([['上指', 'sh'], ['深指', 'sz'], ['创指', 'cyb'], ['创业板B', '150153'], ['互联网B', '150195'], ['煤炭B', '150290'], ['钢铁B', '150288'], ['证券B', '150172'], ['房地产B', '150118'], ['国防B', '150206'], ['浙江世宝', '002703'], ['克明面业', '002661'], ['第一创业', '002797'], ['万科A', '000002'], ['恒生电子', '600570'], ['龙洲股份', '002682'], ['天顺股份', '002800'], ['深物业A', '000011']])
    rti = ts.get_realtime_quotes(codes[1])
    rti['percent'] = [100.0 * (float(rti['price'][i]) - float(rti['pre_close'][i]))/float(rti['pre_close'][i]) for i in range(len(rti.index))]
    rti['amount'] = [float(rti['amount'][i]) / 100000000.0 for i in range(len(rti.index))]
    return rti[['name','code','price','high','low','percent','amount','time']]
