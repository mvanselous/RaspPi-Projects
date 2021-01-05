from sense_hat import SenseHat
from generate_ticker import*

sense = SenseHat()
sense.clear()
sense.low_light = True; sense.set_rotation(90)

def disp_ticker(ticker):
    data = Ticker(ticker)
    print(data.close)
    range_clr = [0,0,153]
    closed_clr = [100,100,100]
    change_clr = [255,255,25]
    if data.close[6] > data.close[0]:
        close_clr = [0,255,0] #grn
    elif data.close[6] == data.close[0]:
        close_clr = [255,255,255] #wht
    else:
        close_clr = [255,0,0] #red
    
    range_data = [range(round(7*(l-data.min)/data.spread),
                        round(7*(h-data.min)/data.spread)+1)
                  for l,h in zip(data.low,data.high)]
    close_data = [round(7*(x-data.min)/data.spread) for x in data.close]
    
    for idx,(close,day_range) in enumerate(zip(close_data,range_data)):
        for col in day_range:
            sense.set_pixel(idx,col,range_clr)
        sense.set_pixel(idx,close,close_clr)
        if data.low[idx] == data.high[idx]:
            sense.set_pixel(idx,close,closed_clr)
    
    per_change_disp = [0]*8
    per_change_data = round(data.percent_change)
    print(per_change_data)
    for idx in range(0,abs(per_change_data)):
        if per_change_data >=0:
            per_change_disp[idx %8] +=1
        else:
            per_change_disp[(7-idx) %8] +=1
        
    change_clr_dict ={0: [0,0,0],
                      1:[255,255,25],
                      2:[255,102,255],
                      3:[68,0,102],
                      4:[255,255,255]}
    
    print(per_change_disp)
    for idx,pixel in enumerate(per_change_disp):
        sense.set_pixel(7,idx,change_clr_dict[pixel])
    sense.flip_v()
    
    
disp_ticker('BTC-USD')
#disp_ticker('XRP-USD')
#disp_ticker('ES%3DF')
#disp_ticker('CL%3DF')
#disp_ticker('MU')
