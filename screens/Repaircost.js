import React from "react";
import styled from "styled-components"
import { View, Text, TouchableOpacity, ScrollView } from "react-native";

const Container = styled.View`
    flex: 1;
    background-color: white;
    align-items: center;
`;

const CarImage = styled.Image`
    width: 256px;
    height: 256px;
    border-color: black;
    border-width: 2px;
    border-radius: 10px;
    margin-top: 15px;
`;

const ResultBox = styled.View`
    width: 85%;
    border-color: black;
    border-width: 2px; 
    border-radius: 10px;
    margin-top: 30px;
    padding-left: 15px;
    paddingVertical: 10px;
`;

const ResultText = styled.Text`
    font-family: 'Pretendard-Bold';
    font-size: 18px;
    margin-top: 8px;
`;

const ResultText2 = styled.Text`
    font-family: 'Pretendard-Regular';
    font-size: 18px;
`;

export default function RepairCost({ navigation }) {

    return (
        <Container>
            <ScrollView style={{flex: 1, width: "100%"}}>
                <View style={{width: "100%", alignItems: "center"}}>
                    <Text style={{ fontWeight: "bold", fontSize: 20, marginTop: 20 }}>수리비 분석 결과</Text>
                    <Text>1/1</Text>
                    <CarImage source={require("../assets/images/test_input.jpg")}/>
                    <ResultBox>
                        <ResultText>파손 부위:   <ResultText2>Right Front Fender</ResultText2></ResultText>
                        <ResultText>추천 수단:   <ResultText2>수리</ResultText2></ResultText>
                        <ResultText>추천 사항:   <ResultText2>판금</ResultText2></ResultText>
                        <ResultText2 style={{fontSize: 14, marginTop: 30}}>120건의 유사 사례를 기반으로 한 진단 결과</ResultText2>
                        <ResultText style={{fontFamily: "Pretendard-Bold", fontSize: 24}}>예상 수리 비용 : 200,000 Won</ResultText>
                        <TouchableOpacity onPress={()=>navigation.navigate("NearCenter")}>
                            <ResultText2 style={{ fontSize: 14, marginTop: 10, color: 'gray', textDecorationLine: 'underline' }}>근처 수리점 정보 알아보기</ResultText2>
                        </TouchableOpacity>
                    </ResultBox>
                    <ResultBox>
                        <ResultText>파손 부위:   <ResultText2>Bonnet</ResultText2></ResultText>
                        <ResultText>추천 수단:   <ResultText2>교체</ResultText2></ResultText>
                        <ResultText>추천 사항:   <ResultText2>범퍼 교체</ResultText2></ResultText>
                        <ResultText2 style={{fontSize: 14, marginTop: 30}}>162건의 유사 사례를 기반으로 한 진단 결과</ResultText2>
                        <ResultText style={{fontFamily: "Pretendard-Bold", fontSize: 24}}>예상 수리 비용 : 600,000 Won</ResultText>
                        <TouchableOpacity onPress={()=>navigation.navigate("NearCenter")}>
                            <ResultText2 style={{ fontSize: 14, marginTop: 10, color: 'gray', textDecorationLine: 'underline' }}>근처 수리점 정보 알아보기</ResultText2>
                        </TouchableOpacity>
                    </ResultBox>
                    <ResultBox>
                        <ResultText>파손 부위:   <ResultText2>Front Bumber</ResultText2></ResultText>
                        <ResultText>추천 수단:   <ResultText2>교체</ResultText2></ResultText>
                        <ResultText>추천 사항:   <ResultText2>범퍼 교체</ResultText2></ResultText>
                        <ResultText2 style={{fontSize: 14, marginTop: 30}}>250건의 유사 사례를 기반으로 한 진단 결과</ResultText2>
                        <ResultText style={{fontFamily: "Pretendard-Bold", fontSize: 24}}>예상 수리 비용 : 400,000 Won</ResultText>
                        <TouchableOpacity onPress={()=>navigation.navigate("NearCenter")}>
                            <ResultText2 style={{ fontSize: 14, marginTop: 10, color: 'gray', textDecorationLine: 'underline' }}>근처 수리점 정보 알아보기</ResultText2>
                        </TouchableOpacity>
                    </ResultBox>
                    <View style={{height: 40}}></View>
                </View>
            </ScrollView>
        </Container>
    );
}

/*
<TouchableOpacity style={{ alignSelf: "flex-end", marginTop: 15, marginBottom: 15, marginRight: "7.5%" }}>
    <Text style={{ fontSize: 25 }}>Next {'>'}</Text>
</TouchableOpacity>
*/