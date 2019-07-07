query_list = {
    "hl=ja&gl=JP": ["Japan", 138.030896, 37.592301, "Asia"],
    "hl=cs&gl=CZ": ["Czechia", 15.312402, 49.733412, "Europe"],
    "hl=de&gl=DE": ["Germany", 10.385781, 51.106982, "Europe"],
    "hl=de&gl=AT": ["Austria", 14.126476, 47.585494, "Europe"],
    "hl=de&gl=CH": ["Switzerland", 8.208675, 46.797859, "Europe"],  # 重複2
    "hl=en-AU&gl=AU": ["Australia", 134.491, -25.732887, "Oceania"],
    "hl=en-BW&gl=BW": ["Botswana", 23.798534, -22.184032, "Africa"],
    "hl=en-CA&gl=CA": ["Canada", -108.116645, 57.91934, "North America"],  # 重複2
    "hl=en-ET&gl=ET": ["Ethiopia", 39.600801, 8.622787, "Africa"],
    "hl=en-GH&gl=GH": ["Ghana", -1.216766, 7.953456, "Africa"],
    # "hl=en-IN&gl=IN": "India",  # 重複6 除外
    "hl=en-IE&gl=IE": ["Ireland", -8.137936, 53.175449, "Europe"],
    # "hl=en-IL&gl=IL": "Israel",  # 重複2 除外
    "hl=en-KE&gl=KE": ["Kenya", 37.79594, 0.59988, "Africa"],
    # "hl=en-LV&gl=LV": "Latvia",  # 重複2 除外
    "hl=en-MY&gl=MY": ["Malaysia", 109.697623, 3.789868, "Asia"],
    "hl=en-NA&gl=NA": ["Namibia", 17.209636, -22.130326, "Africa"],
    "hl=en-NZ&gl=NZ": ["New Zealand", 171.484923, -41.811136, "Oceania"],
    "hl=en-NG&gl=NG": ["Nigeria", 8.089439, 9.594115, "Africa"],
    "hl=en-PK&gl=PK": ["Pakistan", 69.339579, 29.949752, "Asia"],
    "hl=en-PH&gl=PH": ["Philippines", 122.883933, 11.775368, "Asia"],
    "hl=en-SG&gl=SG": ["Singapore", 103.817256, 1.358761, "Asia"],
    "hl=en-ZA&gl=ZA": ["South Africa", 25.083901, -29.000341, "Africa"],
    "hl=en-TZ&gl=TZ": ["Tanzania", 34.8131, -6.275654, "Africa"],
    "hl=en-UG&gl=UG": ["Uganda", 32.36908, 1.274693, "Africa"],
    "hl=en-GB&gl=GB": ["UK", -2.865632, 54.123872, "Europe"],
    "hl=en-US&gl=US": ["USA", -96.767474, 38.294041, "North America"],  # 重複2
    "hl=en-ZW&gl=ZW": ["Zimbabwe", 29.851441, -19.004204, "Africa"],
    "hl=es-419&gl=AR": ["Argentina", -65.179807, -35.381349, "South America"],
    "hl=es-419&gl=CL": ["Chile", -71.382562, -37.73071, "South America"],
    "hl=es-419&gl=CO": ["Colombia", -73.081146, 3.913834, "South America"],
    "hl=es-419&gl=CU": ["Cuba", -79.016054, 21.622895, "North America"],
    # "hl=es-419&gl=US": "United States of America",  # 重複2 除外
    "hl=es-419&gl=MX": ["Mexico", -102.523452, 23.947537, "North America"],
    "hl=es-419&gl=PE": ["Peru", -74.382427, -9.152804, "South America"],
    "hl=es-419&gl=VE": ["Venezuela", -66.181841, 7.124224, "South America"],
    "hl=fr&gl=BE": ["Belgium", 4.640651, 50.639816, "Europe"],  # 重複2
    # "hl=fr-CA&gl=CA": "Canada",  # 重複2 除外
    "hl=fr&gl=FR": ["France", 2.719701, 47.366374, "Europe"],
    "hl=fr&gl=MA": ["Morocco", -8.456158, 29.83763, "Africa"],
    "hl=fr&gl=SN": ["Senegal", -14.473492, 14.366242, "Africa"],
    # "hl=fr&gl=CH": "Switzerland",  # 重複2 除外
    "hl=id&gl=ID": ["Indonesia", 117.240114, -2.215055, "Asia"],
    "hl=it&gl=IT": ["Italy", 12.070013, 42.796626, "Europe"],
    "hl=lv&gl=LV": ["Latvia", 24.91236, 56.850852, "Europe"],  # 重複2
    "hl=lt&gl=LT": ["Lithuania", 23.887194, 55.32611, "Europe"],
    "hl=hu&gl=HU": ["Hungary", 19.395591, 47.162775, "Europe"],
    # "hl=nl&gl=BE": "Belgium",  # 重複2 除外
    "hl=nl&gl=NL": ["Netherlands", 5.281448, 52.10079, "Europe"],
    "hl=no&gl=NO": ["Norway", 9.001427, 62.11474, "Europe"],
    "hl=pl&gl=PL": ["Poland", 19.390128, 52.127596, "Europe"],
    "hl=pt-BR&gl=BR": ["Brazil", -53.097831, -10.787777, "South America"],
    "hl=pt-PT&gl=PT": ["Portugal", -8.501044, 39.595507, "Europe"],
    "hl=ro&gl=RO": ["Romania", 24.97293, 45.852431, "Europe"],
    "hl=sk&gl=SK": ["Slovakia", 19.479052, 48.705475, "Europe"],
    "hl=sl&gl=SI": ["Slovenia", 14.804442, 46.115548, "Europe"],
    "hl=sv&gl=SE": ["Sweden", 14.783805, 60.413995, "Europe"],
    "hl=vi&gl=VN": ["Vietnam", 106.299147, 16.646017, "Asia"],
    "hl=tr&gl=TR": ["Turkey", 35.168953, 39.061603, "Asia"],
    "hl=el&gl=GR": ["Greece", 22.955558, 39.074696, "Europe"],
    "hl=bg&gl=BG": ["Bulgaria", 25.215529, 42.768903, "Europe"],
    "hl=ru&gl=RU": ["Russia", 96.686561, 61.980522, "Europe"],
    # "hl=ru&gl=UA": "Ukraine",  # 重複2 除外
    "hl=sr&gl=RS": ["Serbia", 20.789583, 44.221503, "Europe"],
    "hl=uk&gl=UA": ["Ukraine", 31.383265, 48.996567, "Europe"],  # 重複2
    "hl=he&gl=IL": ["Israel", 35.004447, 31.461101, "Asia"],  # 重複2
    "hl=ar&gl=AE": ["UAE", 44.536863, 24.122458, "Asia"],
    "hl=ar&gl=SA": ["Saudi Arabia", 44.536863, 24.122458, "Asia"],
    "hl=ar&gl=LB": ["Lebanon", 35.880161, 33.923066, "Asia"],
    "hl=ar&gl=EG": ["Egypt", 29.861901, 26.495933, "Africa"],
    # "hl=mr&gl=IN": "India",  # 重複6 除外
    "hl=hi&gl=IN": ["India", 79.611976, 22.885782, "Asia"],  # 重複6
    "hl=bn&gl=BD": ["Bangladesh", 90.238127, 23.867312, "Asia"],
    # "hl=ta&gl=IN": "India",  # 重複6 除外
    # "hl=te&gl=IN": "India",  # 重複6 除外
    # "hl=ml&gl=IN": "India",  # 重複6 除外
    "hl=th&gl=TH": ["Thailand", 101.002881, 15.118158, "Asia"],
    "hl=zh-CN&gl=CN": ["China", 104.261435, 33.465238, "Asia"],
    "hl=zh-TW&gl=TW": ["Taiwan", 120.954273, 23.753993, "Asia"],
    "hl=zh-HK&gl=HK": ["Hong Kong", 114.113805, 22.398277, "Asia"],
    "hl=ko&gl=KR": ["Korea", 127.839161, 36.38524, "Asia"]
}

if __name__ == '__main__':
    import json
    with open("nation_table.json", "w") as f:
        json.dump({k[-2:]: v[0::3] for k, v in query_list.items()}, f, indent=4)
