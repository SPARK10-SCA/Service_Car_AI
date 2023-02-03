import joblib
import numpy as np

# PART feature 압축
def get_parts(part) :
    if any(substring in part for substring in ["프런트범퍼","프런트 범퍼","앞범퍼","후론트 범퍼","후론트범퍼"]) :
        part = "Frontbumper"
    elif any(substring in part for substring in ['리어범퍼',"리어 범퍼","뒤범퍼"]) :
        part = "Rearbumper"
    elif any(substring in part for substring in ['프런트펜더',"프런트 펜더","프런트휀다","앞펜더","앞휀다","앞휀더","후론트휀다","후혼트 휀다"] ) :
       part = "Frontfender"
    elif any(substring in part for substring in ['리어펜더',"리어휀다","리어 휀다","뒤펜더","뒤휀다","뒤헨더"]) :
       part = "Rearfender"
    elif any(substring in part for substring in ['본넷',"본네트"]) :
       part = "Bonnet"
    elif part.find('트렁크') > -1 :
       part = "Trunklid"
    elif any(substring in part for substring in ['리어도어',"도어(뒤"]) :
       part = "Reardoor"
    elif any(substring in part for substring in ['프런트도어',"도어(앞","후론트 도어"]) :
       part = "Frontdoor"
    elif part.find('미러') > -1 :
       part = "Sidemirror"
    elif part.find('휠') > -1 :
       part = "FrontWheel"
    elif part.find('헤드라이트') > -1 :
       part = "Headlights"
    else :
        part = None
    return part

# SEVERITY feature 압축
def get_severity(severity) :
    if severity.find("오버홀") > -1 :
        severity = "오버홀"
    elif severity.find("교환") > -1 :
        severity = "교환"
    elif severity.find("판금") > -1 :
        severity = "판금"
    elif severity.find("수리") > -1 :
        severity = "수리"
    elif severity.find("도장") > -1 :
        severity = "도장"
    elif severity.find("조정") > -1 :
        severity = "조정"
    elif severity.find("OH") > -1 :
        severity = "OH"
    elif severity.find("탈착") > -1 :
        severity = "탈착"
    else :
        severity = None
    return severity

# outlier 제거
def delete_outlier(data, column, threshold) :
    idx = []
    It = list(data[column])
    for i in range(len(It)) :
        if(It[i] > threshold) :
            idx.append(i)
    return idx

# 모델 input 전처리
def get_model_input(MILEAGE, FIRSTDAY, REPAIRDAY, HQ, PART, SEVERITY) : 
    if any(substring in PART for substring in ["프런트범퍼","프런트 범퍼","앞범퍼","후론트 범퍼","후론트범퍼"]) :
        PART = 2
    elif any(substring in PART for substring in ['리어범퍼',"리어 범퍼","뒤범퍼"]) :
        PART = 6
    elif any(substring in PART for substring in ['프런트펜더',"프런트 펜더","프런트휀다","앞펜더","앞휀다","앞휀더","후론트휀다","후혼트 휀다"] ) :
       PART = 4
    elif any(substring in PART for substring in ['리어펜더',"리어휀다","리어 휀다","뒤펜더","뒤휀다","뒤헨더"]) :
       PART = 8
    elif any(substring in PART for substring in ['본넷',"본네트"]) :
       PART = 0
    elif PART.find('트렁크') > -1 :
       PART = 10
    elif any(substring in PART for substring in ['리어도어',"도어(뒤"]) :
       PART = 7
    elif any(substring in PART for substring in ['프런트도어',"도어(앞","후론트 도어"]) :
       PART = 3
    elif PART.find('미러') > -1 :
       PART = 9
    elif PART.find('휠') > -1 :
       PART = 1
    elif PART.find('헤드라이트') > -1 :
       PART = 5

    if SEVERITY.find("오버홀") > -1 :
        SEVERITY = 4
    elif SEVERITY.find("교환") > -1 :
        SEVERITY = 1
    elif SEVERITY.find("판금") > -1 :
        SEVERITY = 7
    elif SEVERITY.find("수리") > -1 :
        SEVERITY = 3
    elif SEVERITY.find("도장") > -1 :
        SEVERITY = 2
    elif SEVERITY.find("조정") > -1 :
        SEVERITY = 5
    elif SEVERITY.find("OH") > -1 :
        SEVERITY = 0
    elif SEVERITY.find("탈착") > -1 :
        SEVERITY = 6

    MinmaxScaler = joblib.load('MODEL_scaler.save') 
    scaledData = MinmaxScaler.transform([[MILEAGE, FIRSTDAY, REPAIRDAY, HQ]])
    modelinput = np.r_[scaledData[0], PART, SEVERITY]
    return modelinput