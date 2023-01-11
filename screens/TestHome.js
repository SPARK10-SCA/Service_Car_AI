import React, {useEffect, useState} from "react";
import styled from "styled-components";
import { View, Text, Alert, ActivityIndicator } from "react-native";

const Container = styled.View`
    flex: 1;
    background-color: white;
    align-items: center;
    justify-content: center;
`;

const IndexInput = styled.TextInput`
    border-color: black;
    border-width: 1px;
    width: 200px;
    height: 50px;
    padding-left: 10px;
`;

const Button = styled.TouchableOpacity`
    width: 50px;
    height: 50px;
    align-items: center;
    justify-content: center;
    border-color: black;
    border-width: 2px;
    background-color: lightgray;
`;

const ButtonText = styled.Text`

`;

const CarImage = styled.Image`
    width: 256px;
    height: 256px;
    margin-top: 30px;
    border-color: black;
    border-width: 2px;
    border-radius: 15px
`

const Button2 = styled.TouchableOpacity`
    width: 80px;
    height: 50px;
    align-items: center;
    justify-content: center;
    border-color: black;
    border-width: 2px;
    border-radius: 15px;
    margin-top: 20px;
`;

export default function TestHome({navigation}){
    const [index, setIndex] = useState(0);
    const [photo, setPhoto] = useState(false);
    const [pressed, setPressed] = useState(false)

    useEffect(()=>{
        if(pressed){
            setTimeout(()=>{
                navigation.navigate("DamageTest1");
                setPhoto(false);
            }, 5000)
        }
    },[pressed])

    return(
        <Container>
            <Text style={{fontSize: 20, marginBottom: 20}}>테스트셋 Index 입력</Text>
            <View style={{display: "flex", flexDirection: "row"}}>
                <IndexInput 
                    placeholder="1-1000"
                    onChangeText={(text)=>setIndex(Number(text))}
                />
                <Button onPress={()=>setPhoto(true)}>
                    <ButtonText>선택</ButtonText>
                </Button>
            </View>
            {
                photo ? 
                    <CarImage source={require("../assets/images/test_input.jpg")}/> : null
            }
            {
                photo ?
                    <Button2 onPress={()=>setPressed(true)}>
                        <ButtonText>다음</ButtonText>
                    </Button2> :
                    <Button2 onPress={()=>Alert.alert("알림", "사진을 먼저 선택해주세요.")}>
                        <ButtonText>다음</ButtonText>
                    </Button2>
            }
            {
                pressed ? 
                <View style={{alignItems: "center"}}>
                    <ActivityIndicator style={{width: 100, height: 100, marginTop: 25}} size="large" />
                    <Text>차량 파손을 측정 중입니다...</Text>
                </View>: null
            }
            
        </Container>
    );
}