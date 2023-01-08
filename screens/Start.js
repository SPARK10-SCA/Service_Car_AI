import React, {useEffect} from "react";
import styled from "styled-components";
import { Text, Image } from "react-native";

const Container = styled.View`
    flex: 1;
    background-color: black;
    align-items: center;
    justify-content: center;
`;

export default function Start({navigation}){
    useEffect(()=>{
        setTimeout(()=>{
            navigation.navigate("Home");
        }, 1500)
    }, [])
    
    return(
        <Container>
            <Image source={require("../assets/images/car_icon.png")}/>
            <Text style={{
                fontFamily: 'Jalnan',
                fontSize: 40,
                color: "white"
            }}>
                SCA
            </Text>
            <Text style={{
                fontFamily: 'Jalnan',
                fontSize: 18,
                color: "white"
            }}>
                Service Car AI
            </Text>
        </Container>
    );
}