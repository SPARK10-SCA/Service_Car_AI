import React from "react";
import { StyleSheet, View, Text, Image } from "react-native";
import { TouchableOpacity } from "react-native-gesture-handler";
import { useState } from 'react';
import CheckBox from "expo-checkbox";

function DamagePage3({ navigation }) {

    const [Crush, isCrush] = useState(false)
    const [Scratch, isScratch] = useState(false)
    const [Separate, isSeparate] = useState(false)
    const [Break, isBreak] = useState(false)

    return (
        <View style={styles.container}>
            <View style={{ alignItems: 'center' }}>
                <Text style={{ alignItems: 'center', justifyContent: 'center', fontWeight: "bold", fontSize: 20 }}>데미지 분석 결과</Text>
                <Text style={{ alignItems: 'center', justifyContent: 'center' }}>3/3</Text>
                <View style={{ flexDirection: 'row', marginTop: 30 }}>
                    <Image style={{ alignContent: 'center', justifyContent: 'center', width: 250, height: 250 }} source={require("../assets/damage.jpg")}></Image>
                    <View style={{ paddingLeft: 15, justifyContent: 'center' }}>
                        <Text style={{ fontWeight: "bold" }}>탐지된 파손</Text>
                        <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                            <CheckBox value={Crush} onValueChange={isCrush}></CheckBox>
                            <Text style={{ paddingLeft: 10 }}>Crush</Text>
                        </View>
                        <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                            <CheckBox value={Scratch} onValueChange={isScratch}></CheckBox>
                            <Text style={{ paddingLeft: 10 }}>Scratch</Text>
                        </View>
                        <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                            <CheckBox value={Separate} onValueChange={isSeparate}></CheckBox>
                            <Text style={{ paddingLeft: 10 }}>Separate</Text>
                        </View>
                        <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                            <CheckBox value={Break} onValueChange={isBreak}></CheckBox>
                            <Text style={{ paddingLeft: 10 }}>Break</Text>
                        </View>
                    </View>
                </View>
            </View>
            <View style={styles.separator}></View>
            <TouchableOpacity style={{ marginTop: 10, paddingLeft: 30, padding: 10, borderColor: 'gray', borderWidth: 2, alignContent: 'center', justifyContent: 'center' }}>
                <Text style={{ fontSize: 20 }}>Part : 프레임 손상 (가능성 70%)</Text>
                <Text style={{ fontSize: 20 }}>Severity : 상</Text>
            </TouchableOpacity>
            <TouchableOpacity style={{ marginTop: 20, paddingLeft: 30, padding: 10, borderColor: 'gray', borderWidth: 2, alignContent: 'center', justifyContent: 'center' }}>

                <Text style={{ fontSize: 20 }}>Part : 브라켓 손상 (가능성 62%)</Text>
                <Text style={{ fontSize: 20 }}>Severity : 중</Text>
            </TouchableOpacity>
            <TouchableOpacity style={{ marginTop: 20, paddingLeft: 30, padding: 10, borderColor: 'gray', borderWidth: 2, alignContent: 'center', justifyContent: 'center' }}>

                <Text style={{ fontSize: 20 }}>Part : 레일 손상 (가능성 44%)</Text>
                <Text style={{ fontSize: 20 }}>Severity : 하</Text>
            </TouchableOpacity>

            <TouchableOpacity style={{ width: '100%', alignItems: "flex-end", paddingRight: 50, marginTop: 40 }}
                onPress={() => {
                    navigation.navigate('Repaircost')
                }}>
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

export default DamagePage3;