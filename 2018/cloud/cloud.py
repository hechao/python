#! /usr/bin/python
#-*- encoding: utf-8 -*-

import os
from datetime import datetime, timedelta

def data_gd():
    now = datetime.now()
    datelist_gd = []
    min_stamp = '02'
    
    for i in range(12):
        timestamp = now - timedelta(hours=i)
        #print timestamp
        datelist_gd.append(timestamp.strftime('%Y%m%d%H' + min_stamp))
    #print datelist_gd
    return datelist_gd
    
def data_fy():
    now = datetime.now()
    datelist_fy = []
    min_stamp = '15'
    
    for i in range(12):
        timestamp = now - timedelta(hours=i)
        #print timestamp
        datelist_fy.append(timestamp.strftime('%Y%m%d%H' + min_stamp))
    #print datelist_fy
    return datelist_fy
    
def get_gdpic(datelist_gd):
    GDYT = '%E5%B9%BF%E4%B8%9C%E4%BA%91%E5%9B%BE/%E7%BA%A2%E5%A4%96%E4%BA%91%E5%9B%BE' 

    for i in datelist_gd:
        command_wget_image = "wget -q http://www.gdwater.gov.cn:9001/Data/Cloud/%s/%s.jpg\
                                -O /srv/www/cloud/gd%s.jpg" % (GDYT, i, i)
        os.system(command_wget_image)

    # convert gif and copy
    command_convert = 'convert -delay 50 -resize 400x300 /srv/www/cloud/gd*.jpg /srv/www/cloud/fngd_cloud.gif'
    os.system(command_convert)
    
    command_remove_www_jpg = "rm /srv/www/cloud/gd*.jpg"
    os.system(command_remove_www_jpg)
    
    command_wget_last_image = "wget http://www.gdwater.gov.cn:9001/Data/Cloud/%s/%s.jpg\
                                -O /srv/www/cloud/fngd_last.jpg" % (GDYT, datelist_gd[1])
    os.system(command_wget_last_image)
    cmd_crop = 'convert /srv/www/cloud/fngd_last.jpg -crop 550x400+130+20 /srv/www/cloud/fngd_last.jpg'
    os.system(cmd_crop)
    
def get_fypic(datelist_fy):
    fy_url = "%E9%A3%8E%E4%BA%91%E4%BA%8C%E5%8F%B7"

    for i in datelist_fy:
        command_wget_image = "wget -q http://www.gdwater.gov.cn:9001/Data/Cloud/%s/201601/%s.jpg\
                                -O /srv/www/cloud/fy%s.jpg" % (fy_url, i, i)
        os.system(command_wget_image)

    # convert gif and copy
    command_convert = 'convert -delay 50 -resize 400x300 /srv/www/cloud/fy*.jpg\
                        /srv/www/cloud/fnfy_cloud.gif'
    os.system(command_convert)
    
    command_remove_www_jpg = "rm /srv/www/cloud/fy*.jpg"
    os.system(command_remove_www_jpg)
    
    command_wget_last_image = "wget http://www.gdwater.gov.cn:9001/Data/Cloud/%s/201601/%s.jpg\
                                -O /srv/www/cloud/fnfy_last.jpg" % (fy_url, datelist_fy[1])
    os.system(command_wget_last_image)
    cmd_crop = 'convert /srv/www/cloud/fnfy_last.jpg -crop 550x400+800+500 /srv/www/cloud/fnfy_last.jpg'
    os.system(cmd_crop)

        
if __name__ == "__main__":
    datelist_gd = data_gd()
    datelist_fy = data_fy()
    get_gdpic(datelist_gd)
    get_fypic(datelist_fy)