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
    elif any(substring in part for substring in ['리어도어',"도어(뒤",'리어 도어(좌','리어 도어(우']) :
       part = "Reardoor"
    elif any(substring in part for substring in ['프런트도어',"도어(앞","후론트 도어",'도어(우','도어(좌']) :
       part = "Frontdoor"
    elif part.find('미러') > -1 :
       part = "Sidemirror"
    elif part.find('휠') > -1 :
       part = "FrontWheel"
    elif part.find('헤드라이트','램프') > -1 :
       part = "Headlights"
    else :
        part = None
    return part

# repair_method feature 압축
def get_repair_method(repair_method) :
    if repair_method.find("오버홀") > -1 :
        repair_method = "오버홀"
    elif repair_method.find("교환") > -1 :
        repair_method = "교환"
    elif repair_method.find("판금") > -1 :
        repair_method = "판금"
    elif repair_method.find("수리") > -1 :
        repair_method = "수리"
    elif repair_method.find("도장") > -1 :
        repair_method = "도장"
    elif repair_method.find("조정") > -1 :
        repair_method = "조정"
    elif repair_method.find("OH") > -1 :
        repair_method = "OH"
    elif repair_method.find("탈착") > -1 :
        repair_method = "탈착"
    else :
        repair_method = None
    return repair_method

# outlier 제거
def delete_outlier(data, column, threshold) :
    idx = []
    It = list(data[column])
    for i in range(len(It)) :
        if(It[i] > threshold) :
            idx.append(i)
    return idx

# 모델 input 전처리
def get_model_input(MILEAGE, FIRSTDAY, REPAIRDAY, HQ, PART, REPAIR_METHOD) : 
    if any(substring in PART for substring in ["FrontBumper"]) :
        PART = 2
    elif any(substring in PART for substring in ["RearBumper"]) :
        PART = 6
    elif any(substring in PART for substring in ["FrontFender(L)","FrontFender(R)"] ) :
       PART = 4
    elif any(substring in PART for substring in ["RearFender(L)","RearFender(R)"]) :
       PART = 8
    elif any(substring in PART for substring in ["Bonnet"]) :
       PART = 0
    elif PART.find("Trunklid") > -1 :
       PART = 10
    elif any(substring in PART for substring in ["RearDoor(R)", "RearDoor(L)"]) :
       PART = 7
    elif any(substring in PART for substring in ["FrontDoor(R)", "FrontDoor(L)"]) :
       PART = 3
    elif any(substring in PART for substring in ["SideMirror(R)", "SideMirror(L)"]) :
       PART = 9
    elif any(substring in PART for substring in ["FrontWheel(R)", "FrontWheel(L)"]) :
       PART = 1
    elif any(substring in PART for substring in ["HeadLights(L)", "HeadLights(R)"]) :
       PART = 5

    if REPAIR_METHOD.find("overhaul") > -1 :
        REPAIR_METHOD = 4
    elif REPAIR_METHOD.find("replace") > -1 :
        REPAIR_METHOD = 1
    elif REPAIR_METHOD.find("sheet") > -1 :
        REPAIR_METHOD = 7
    elif REPAIR_METHOD.find("repair") > -1 :
        REPAIR_METHOD = 3
    elif REPAIR_METHOD.find("painting") > -1 :
        REPAIR_METHOD = 2
    elif REPAIR_METHOD.find("1/2OH") > -1 :
        REPAIR_METHOD = 0
    elif REPAIR_METHOD.find("detach") > -1 :
        REPAIR_METHOD = 6

    MinmaxScaler = joblib.load('../weights/repair_cost/repair_cost_scaler.save') 
    scaledData = MinmaxScaler.transform([[MILEAGE, FIRSTDAY, REPAIRDAY, HQ]])
    #print(scaledData[0])
    #print(PART)
    #print(REPAIR_METHOD)
    modelinput = np.r_[scaledData[0], [PART, REPAIR_METHOD]]
    return modelinput