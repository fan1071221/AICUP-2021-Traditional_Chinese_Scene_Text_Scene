from __future__ import print_function
import os, sys, zipfile
import json

for i in range(1,4001):
    json_file = 'img_'+str(i)+'.json'  # # Object Instance 類型的標註
    data = json.load(open(json_file, 'r'))
 
    ana_txt_save_path = "./new1"  # 保存的路徑
    if not os.path.exists(ana_txt_save_path):
        os.makedirs(ana_txt_save_path)

    for img in data['shapes']:
        #if ((img['group_id'])==0 or img['group_id']==2 or img['group_id']==3 or img['group_id']==4):
        if ((img['group_id'])!=0 and img['group_id']!=2 and img['group_id']!=3 and img['group_id']!=4):
            filename = data['imagePath']
            xl_up=img['points'][0][0]#Xmin
            yl_up=img['points'][0][1]#Ymin

            xr_up=img['points'][1][0]#Xmax
            yr_up=img['points'][1][1]#Ymin

            xr_dn=img['points'][2][0]#Xmax
            yr_dn=img['points'][2][1]#Ymax

            xl_dn=img['points'][3][0]#Xmin
            yl_dn=img['points'][3][1]#Ymax
            img_width = float(data['imageWidth'])#w圖
            img_height = float(data['imageHeight'])#H圖

            if(xr_up> xr_dn):
                Xmax = xr_up
            else:
                Xmax = xr_dn

            if(yr_dn> yl_dn):
                Ymax = yr_dn
            else:
                Ymax = yl_dn

            if(xl_up> xl_dn):
                Xmin = xl_dn
            else:
                Xmin = xl_up

            if(yr_up> yl_up):
                Ymin = yl_up
            else:
                Ymin = yr_up

            X_center = ((Xmin+Xmax)/2)/img_width
            Y_center = ((Ymin+Ymax)/2)/img_height

            width = abs((Xmax-Xmin)/img_width)
            height = abs((Ymax-Ymin)/img_height)

            group_id = 0
            ana_txt_name = filename.split(".")[0] + ".txt"#對應的txt名字，與jpg一致
            print(ana_txt_name)
            f_txt = open(os.path.join(ana_txt_save_path, ana_txt_name), 'a')

            f_txt.write("%s %s %s %s %s\n" % (group_id, X_center, Y_center, width, height))
            f_txt.close()