import React from "react";
import { StyleSheet, View, Text, Image } from "react-native";
import { TouchableOpacity } from "react-native-gesture-handler";
import { useState } from 'react';
import CheckBox from "expo-checkbox";

function Repaircost({ navigation }) {

    const [Crush, isCrush] = useState(false)
    const [Scratch, isScratch] = useState(false)
    const [Separate, isSeparate] = useState(false)
    const [Break, isBreak] = useState(false)

    return (
        <View style={styles.container}>
            <View style={{ alignItems: 'center' }}>
                <Text style={{ alignItems: 'center', justifyContent: 'center', fontWeight: "bold", fontSize: 20 }}>수리비 진단 결과</Text>
                <Text style={{ alignItems: 'center', justifyContent: 'center' }}>1/3</Text>
                <View style={{ flexDirection: 'row', marginTop: 30 }}>
                    <Image style={{ alignContent: 'center', justifyContent: 'center', width: 370, height: 250 }} source={require("../assets/damage.jpg")}></Image>
                </View>
            </View>
            <View style={styles.separator}></View>
            <View style={{ marginLeft: 20, marginTop: 10 }}>

                <Text style={{ fontSize: 17 }}>파손 부위 : 우측 앞 범퍼</Text>
                <Text style={{ fontSize: 17, marginTop: 25 }}>추천 수단 : <Text>수리</Text> / <Text style={styles.graytext}>교체</Text></Text>
                <Text style={{ fontSize: 17, marginTop: 25 }}>파손 부위 : 우측 앞 범퍼</Text>
                <Text style={{ fontSize: 17, marginTop: 25 }}>정도 : 
                <Text style={styles.graytext}>강</Text> / 
                <Text style={styles.graytext}>중</Text> / 
                <Text>약</Text></Text>
                <Text style={{ fontSize: 17, marginTop: 25 }}>추천 수리 : 1. 덴트 (저렴), 2. 도색</Text>
                <Text style={{ fontSize: 12, marginTop: 50 }}>250건의 유사 사례를 기반으로 한 진단 결과</Text>
                <Text style={{ fontSize: 25, marginTop: 0 }}>예상 수리 비용 : 70000 Won</Text>
                <TouchableOpacity>
                    <Text style={{ fontSize: 15, marginTop: 10, color: 'gray', textDecorationLine: 'underline' }}>근처 수리점 정보 알아보기</Text>
                </TouchableOpacity>
            </View>

            <TouchableOpacity style={{ width: '100%', alignItems: "flex-end", paddingRight: 30, marginTop: 10 }}>
                <Text style={{ fontSize: 25 }}>Next</Text>
            </TouchableOpacity>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        paddingTop: 10,

    },
    camera: {
        width: 300,
        height: 300
    },
    cameratext: {
        fontSize: 20
    },
    buttonContainer: {

    },
    graytext: {
        color: 'gray'
    },
    button: {
        backgroundColor: '#ffffff',
    },
    separator: {
        backgroundColor: 'black',
        height: 2,
        marginTop: 15,
        margin: 20,
    },
});

export default Repaircost;