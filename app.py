import streamlit as st
import requests
countries ={
    'Sri Lanka':[12.9850,77.5078,"lk"],
    'United States':[47.7510,-120.7401,"us"],
    'United Kingdom':[51.5085,-0.1257,"gb"],
    'India':[20.5937,78.9629,"in"],
    'Australia':[-25.2744,133.7751,"au"],
    'Canada':[56.1304,-106.3468,"ca"],
    'Germany':[51.1657,10.4515,"de"],
    'France':[46.6034,1.8883,"fr"],
    'Italy':[41.8719,12.5674,"it"],
    'Japan':[36.2048,138.2529,"jp"],
    'China':[35.8617,104.1954,"cn"],
    'Brazil':[-14.2350,-51.9253,"br"],
    'South Africa':[-30.5595,22.9375,"za"],
    'Russia':[61.5240,105.3188,"ru"],
    'Mexico':[23.6345,-102.5528,"mx"],
    'Argentina':[-38.4161,-63.6167,"ar"],
    'Egypt':[26.8206,30.8025,"eg"],
    'Turkey':[38.9637,35.2433,"tr"],
    'Spain':[40.4637,-3.7492,"es"],
    'Netherlands':[52.1326,5.2913,"nl"],
    'Sweden':[60.1282,18.6435,"se"],
    'Norway':[60.4720,8.4689,"no"],
    'New Zealand':[-40.9006,174.8860,"nz"],
    'Kenya':[-0.0236,37.9062,"ke"],
    'Nigeria':[9.0820,8.6753,"ng"],
    'Saudi Arabia':[23.8859,45.0792,"sa"],
    'United Arab Emirates':[23.4241,53.8478,"ae"],
    'Thailand':[15.8700,100.9925,"th"],
    'Vietnam':[14.0583,108.2772,"vn"],
    'Philippines':[12.8797,121.7740,"ph"],
    'Indonesia':[-0.7893,113.9213,"id"],
    'Pakistan':[30.3753,69.3451,"pk"],
    'Bangladesh':[23.6850,90.3563,"bd"],
    'Colombia':[4.5709,-74.2973,"co"],
    'Chile':[-35.6751,-71.5430,"cl"],
    'Peru':[-9.1899,-75.0152,"pe"],
    'Greece':[39.0742,21.8243,"gr"],
    'Portugal':[39.3999,-8.2245,"pt"],
    'Switzerland':[46.8182,8.2275,"ch"],
    'Austria':[47.5162,14.5501,"at"],
    'Belgium':[50.8503,4.3517,"be"],
    'Czech Republic':[49.8175,15.4730,"cz"],
    'Poland':[51.9194,19.1451,"pl"],
    'Hungary':[47.1625,19.5033,"hu"],
    'Romania':[45.9432,24.9668,"ro"],
    'Bulgaria':[42.7339,25.4858,"bg"],
    'Croatia':[45.1000,15.2000,"hr"],
    'Slovakia':[48.6690,19.6990,"sk"],
    'Slovenia':[46.1512,14.9955,"si"],
    'Finland':[61.9241,25.7482,"fi"],
    'Iceland':[64.9631,-19.0208,"is"],
    'Ireland':[53.4129,-8.2439,"ie"],
    'Luxembourg':[49.8153,6.1296,"lu"],
    'Malta':[35.9375,14.3754,"mt"],
    'Cyprus':[35.1264,33.4299,"cy"],
    'Lebanon':[33.8547,35.8623,"lb"],
    'Jordan':[30.5852,36.2384,"jo"],
    'Iraq':[33.2232,43.6793,"iq"],
    'Iran':[32.4279,53.6880,"ir"],
    'Afghanistan':[33.9391,67.7100,"af"],
    'Nepal':[28.3949,84.1240,"np"],
    'Myanmar':[21.9162,95.9560,"mm"],
    'Cambodia':[12.5657,104.9910,"kh"],
    'Laos':[19.8563,102.4955,"la"],
    'Mongolia':[46.8625,103.8467,"mn"],
    'Kazakhstan':[48.0196,66.9237,"kz"],
    'Uzbekistan':[41.3775,64.5853,"uz"],
    'Turkmenistan':[38.9697,59.5563,"tm"],
    'Tajikistan':[38.8610,71.2761,"tj"],
    'Kyrgyzstan':[41.2044,74.7661,"kg"],
    'Ethiopia':[9.1450,40.4897,"et"],
    'Uganda':[1.3733,32.2903,"ug"],
    'Ghana':[7.9465,-1.0232,"gh"],
    'Tanzania':[-6.3690,34.8888,"tz"],
    'Zambia':[-13.1339,27.8493,"zm"],
    'Zimbabwe':[-19.0154,29.1549,"zw"],
    'Mozambique':[-18.6657,35.5296,"mz"],
    'Madagascar':[-18.7669,46.8691,"mg"],
    'Côte d\'Ivoire':[7.5399,-5.5471,"ci"],
    'Senegal':[14.4974,-14.4524,"sn"],
    'Cameroon':[7.3697,12.3547,"cm"],
    'Algeria':[28.0339,1.6596,"dz"],
    'Morocco':[31.7917,-7.0926,"ma"],
    'Tunisia':[33.8869,9.5375,"tn"],
    'Libya':[26.3351,17.2283,"ly"],
    'Sudan':[12.8628,30.2176,"sd"],
    'South Sudan':[6.8770,31.3070,"ss"],
    'Chad':[15.4542,18.7322,"td"],
    'Niger':[17.6078,8.0817,"ne"],
    'Mali':[17.5707,-3.9962,"ml"],
    'Burkina Faso':[12.2383,-1.5616,"bf"],
    'Gabon':[-0.8037,11.6094,"ga"],
    'Angola':[-11.2027,17.8739,"ao"],
    'Congo (Brazzaville)':[ -0.2280,15.8277,"cg"],
    'Congo (Kinshasa)':[ -4.0383,21.7587,"cd"],
    'Haiti':[18.9712,-72.2852,"ht"],
    'Cuba':[21.5218,-77.7812,"cu"],
    'Dominican Republic':[18.7357,-70.1627,"do"],
    'Jamaica':[18.1096,-77.2975,"jm"],
    'Trinidad and Tobago':[10.6918,-61.2225,"tt"],
    'Bahamas':[25.0343,-77.3963,"bs"],
    'Barbados':[13.1939,-59.5432,"bb"],
    'Saint Lucia':[13.9094,-60.9789,"lc"],
    'Grenada':[12.1165,-61.6790,"gd"],
    'Saint Vincent and the Grenadines':[12.9843,-61.2872,"vc"],
    'Antigua and Barbuda':[17.0608,-61.7964,"ag"],
    'Dominica':[15.4150,-61.3710,"dm"],
    'Saint Kitts and Nevis':[17.3578,-62.782998,"kn"]
    
    

}

countryselect = st.sidebar.selectbox('Select Country:', list(countries.keys()))

resp = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={countries[countryselect][0]}&longitude={countries[countryselect][1]}6&daily=weather_code,temperature_2m_max,sunrise,sunset,uv_index_max&hourly=temperature_2m,relative_humidity_2m,weather_code,surface_pressure,pressure_msl,visibility,wind_speed_10m,wind_gusts_10m,wind_direction_10m,soil_temperature_0cm&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m,wind_gusts_10m,weather_code,pressure_msl,surface_pressure&timezone=auto')
st.title('Weather Dashboard')
value = resp.json()
#st.json(value)

#sidebar

st.sidebar.subheader('Weather Parameters:')
st.sidebar.write('Temperature:',value['current']['temperature_2m'])
st.sidebar.write('Latitude:',value['latitude'])
st.sidebar.write('Longitude:',value['longitude'])



#main
st.image(f'https://flagcdn.com/w320/{countries[countryselect][2]}.png')
st.header(countryselect)
st.write('Timezone:', value['timezone'])

#selectbox
typeofinfo = st.selectbox('Select Data To View', ('All','Temperature','Wind Speed','Surface Pressure' ,'Soil Temperature'))
if typeofinfo == 'All':
     st.line_chart(value['hourly']['temperature_2m'], x_label='Hours', y_label='Temperature')
     st.area_chart(value['hourly']['wind_speed_10m'], x_label='Hours', y_label=' Wind Speed', color='#008000')
     st.scatter_chart(value['hourly']['surface_pressure'], x_label='Hours', y_label=' Surface Pressure', color ='#Ff0000')
     st.line_chart(value['hourly']['soil_temperature_0cm'], x_label='Hours', y_label='Soil Temperature', color='#FFFF00')

elif typeofinfo == 'Temperature':
    st.line_chart(value['hourly']['temperature_2m'], x_label='Hours', y_label='Temperature')
elif typeofinfo == 'Wind Speed':
    st.area_chart(value['hourly']['wind_speed_10m'], x_label='Hours', y_label=' Wind Speed', color ='#008000')
elif typeofinfo == 'Surface Pressure':
    st.scatter_chart(value['hourly']['surface_pressure'], x_label='Hours', y_label=' Surface Pressure', color='#Ff0000') 
elif typeofinfo == 'Soil Temperature':
    st.line_chart(value['hourly']['soil_temperature_0cm'], x_label='Hours', y_label='Soil Temperature', color='#FFFF00')

#background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
        background-attachment: fixed;
        background-size: cover
    }
    </style>
    """,
    unsafe_allow_html=True
)
     




