import googlemaps
from datetime import datetime
import pprint

gmaps = googlemaps.Client(key="APIKey)

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions((37.490857,139.926805),
                                     (37.5027414,139.9500282),
                                     departure_time=now)
#directions_result = {'bounds': {'northeast': {'lat': 37.5028698, 'lng': 139.9517939}, 'southwest': {'lat': 37.48782449999999, 'lng': 139.9267699}}, 'copyrights': 'Map data ©2022', 'legs': [{'distance': {'text': '3.8 km', 'value': 3833}, 'duration': {'text': '9 mins', 'value': 526}, 'duration_in_traffic': {'text': '9 mins', 'value': 536}, 'end_address': '3-chōme-10-15 Iimori, Aizuwakamatsu, Fukushima 965-0007, Japan', 'end_location': {'lat': 37.5028698, 'lng': 139.9500554}, 'start_address': 'Japan, 〒965-0876 Fukushima, Aizuwakamatsu, Yamagamachi, 6−６７ サイトウBuild', 'start_location': {'lat': 37.490659, 'lng': 139.9267699}, 'steps': [{'distance': {'text': '3.7 km', 'value': 3661}, 'duration': {'text': '8 mins', 'value': 477}, 'end_location': {'lat': 37.5022748, 'lng': 139.9517776}, 'html_instructions': 'Head <b>east</b> toward <b>国道118号</b>/<wbr/><b>国道121号</b>', 'polyline': {'points': 'skycFim`uY@UDi@BUJ_B@SHyADi@Ba@XeFDo@F{@@c@FgA@KXwEFkAB_@LuBB_@LiBDcA@KBs@@OFgADo@BQ@UHoA@UBk@Bq@JaBBc@@ODq@Bi@@E?K@I?EBWBk@B[?KHoA@GHeA@MDs@@e@LiBDi@VaC?SVuC?EPsBv@kIPqBH}@b@uEFq@BYDe@@CDm@D_@Da@@O@KDg@BS@MBY@K@K?G?I@E?CAK?I?GAKCK?GCMAKCQACCSAOEQAKAGCQAI?AAEAM?CCKCOAECKEIIMKSIKOMIGIEIAC?CAE?C?C?S?A?c@@A?gABO@Y@sADA?aBDS@S@O?k@BC?[@i@BsABs@Ba@@K@U?oADU@M?sADc@BI?G?o@BsBFC?c@@a@@w@BO@]@U?Q?U@c@AUAYAUAOASEMAIA}@Oy@QI?YGs@OUEu@Ou@Mi@MIAo@M]GQEQC_AQk@K{@Qw@MsAWg@IKCa@IMEICIEOIIEWO[U{AgA_Aq@'}, 'start_location': {'lat': 37.490659, 'lng': 139.9267699}, 'travel_mode': 'DRIVING'}, {'distance': {'text': '0.2 km', 'value': 172}, 'duration': {'text': '1 min', 'value': 49}, 'end_location': {'lat': 37.5028698, 'lng': 139.9500554}, 'html_instructions': 'Turn <b>left</b><div style="font-size:0.9em">Destination will be on the left</div>', 'maneuver': 'turn-left', 'polyline': {'points': 'et{cFsieuYCASh@Yp@CDm@`BG`AEl@Ed@'}, 'start_location': {'lat': 37.5022748, 'lng': 139.9517776}, 'travel_mode': 'DRIVING'}], 'traffic_speed_entry': [], 'via_waypoint': []}], 'overview_polyline': {'points': 'skycFim`uYl@oJtAmVp@sLf@cJ`A}OVqE\\kDViDzAwPx@_Jb@}EJgABc@Aa@Im@WkBQqAUi@U_@YU[Ia@?oFNoQf@uIVgCHaB?uAGk@IqI}AqGmAoFaAeAW{@e@{DqC_BbEStC'}, 'summary': '', 'warnings': [], 'waypoint_order': []}
pprint.pprint(directions_result[0]['legs'][0]['distance']['text'])

# Validate an address with address validation
#addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'],
                                                    #regionCode='US',
                                                    #locality='Mountain View',
                                                    #enableUspsCass=True)
#print(directions_result)
