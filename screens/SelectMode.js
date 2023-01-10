import React from "react";
import styled from "styled-components";
import { TouchableOpacity, Text } from "react-native";

const Container = styled.View`
    flex: 1;
    background-color: white;
    align-items: center;
    justify-content: center;
`;

const Button = styled.TouchableOpacity`
    align-items: center;
    justify-content: center;
    border-color: black;
    border-width: 2px;
    border-radius: 20px;
    width: 200px;
    height: 80px;
    margin-bottom: 50px;
`;

const ButtonText = styled.Text`
    font-size: 18px;
    font-weight: bold;
`;

export default function SelectMode({navigation}){
    return(
        <Container>
            <Button onPress={()=>navigation.navigate("Home")}>
                <ButtonText>일반 모드</ButtonText>
            </Button>
            <Button onPress={()=>navigation.navigate("TestHome")}>
                <ButtonText>테스트 모드</ButtonText>
            </Button>
        </Container>
    );
}