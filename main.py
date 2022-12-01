from geopy.distance import geodesic
import csv
import pprint
#飲食店の緯度経度リスト
with open('Shop_location_list.csv') as s:
    #Name,result,longitude,latitude
    reader = csv.reader(s)
    l_s = [row for row in reader]
    print(l_s)
#町の緯度経度リスト
with open('Town_list.csv') as t:
    # Address,Result,longitude,latitude,link for check
    reader = csv.reader(t)
    t_s = [row for row in reader]
    print(t_s)
#飲食店名
restaurant_name = input("飲食店名:")
#飲食店名の座標
#restaurant_location = l_s.index(restaurant_name)
#配達先
deliver_point = input("配達先:")

# (緯度, 経度)
restaurant_location = (float(l_s[1][2]), float(l_s[1][3]))
town_location = (float(t_s[1][2]), float(l_s[1][3]))

dis = geodesic(TokyoStation, NagoyaStation).km

print(dis)