import React, { useEffect } from "react";
import { Text, View, TouchableOpacity } from "react-native";
import styled from "styled-components";

const Container = styled.View`
    flex: 1;
    background-color: white;
    align-items: center;
`;

const Map = styled.Image`
    width: 100%;
    height: 40%;
`;

const CenterList = styled.Image`
    width: 100%;
    height: 74%;
`;

export default function NearCenter({navigation}){
    return(
        <Container>
            <Map source={require("../assets/images/map.png")} />
            <CenterList source={require("../assets/images/centerList.png")} />
        </Container>
    );
}