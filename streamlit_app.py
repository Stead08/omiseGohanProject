#https://www.salesanalytics.co.jp/datascience/datascience017/を参照して作成
#ライブラリのインポート
import streamlit as st
import csv
import requests
# データの読み込み
csv1 = "Shop_location_list.csv"
shop_name_list = []
with open(csv1) as c1:
    reader = csv.reader(c1)
    csvfile_header = next(reader)
    # csvファイルのデータをループ(飲食店の名前だけのリストを作成）
    for row in reader:
        # A列を配列へ格納
        shop_name_list.append(str(row[0]))
#飲食店の緯度経度情報を二次元配列で取得
with open(csv1) as c1:
    shop_list = list(csv.reader(c1))
town_name_list = []
csv2 = "Town_list.csv"
with open(csv2) as c2:
    reader = csv.reader(c2)
    csvfile_header = next(reader)
    # csvファイルのデータをループ
    for row in reader:
        # A列を配列へ格納
        town_name_list.append(str(row[0]))
with open(csv2) as c2:
    town_list = list(csv.reader(c2))
#タイトルを表示
st.title('おみせごはんプロジェクト')
st.title('配達距離計算ツール')
#飲食店リストを表示（ドロップダウン)
st.subheader("飲食店を選択")
shop_selected = st.selectbox("飲食店を一つ選択してください", shop_name_list)
st.write(shop_selected, "が選択されました。")
#町名リストを表示(ドロップダウン)
st.subheader("配達先を選択")
town_selected = st.selectbox("配達先を一つ選択してください", town_name_list)
st.write(town_selected, "が選択されました。")
#選択された飲食店と配達先の緯度経度を取得
for i, line_s in enumerate(shop_list):
    if shop_selected in line_s:
        shop_selected_index = i
shop_selected_longitude_and_latitude = shop_list[shop_selected_index][2], shop_list[shop_selected_index][3]
for i, line_s in enumerate(town_list):
    if town_selected in line_s:
        town_selected_index = i
town_selected_longitude_and_latitude = town_list[town_selected_index][2], town_list[town_selected_index][3]

#直線距離を計算
from geopy.distance import geodesic
dis = geodesic(shop_selected_longitude_and_latitude, town_selected_longitude_and_latitude).km
#Googleマップで車での移動距離を計算
#google mapライブラリのインポート
import googlemaps
from datetime import datetime
googlemapAPIkey = st.secrets["googlemapAPIkey"]
gmaps = googlemaps.Client(key= googlemapAPIkey)
now = datetime.now()
directions_result = gmaps.directions(shop_selected_longitude_and_latitude,
                                     town_selected_longitude_and_latitude,
                                     departure_time=now)
distance_driving_km = directions_result[0]['legs'][0]['distance']['text']
#タクシー運賃を計算
## 距離運賃
#運転距離をmに換算
import math
distance_driving_km.split()
distance_driving_m = math.floor(float(distance_driving_km[0]) * 1000)
if float(distance_driving_m) >= 1000:
    fare_distance = round(580 + 90 * (distance_driving_m - 1000) / 248)
else:
    fare_distance = 580

#出力（テクスト）
dis_round = round(dis, 2)
st.subheader('直線距離')
st.write('{}km'.format(dis_round))
st.subheader('運転距離')
st.write('{}'.format(distance_driving_km))
st.subheader('予想運賃')
st.write("{}円".format(fare_distance))
