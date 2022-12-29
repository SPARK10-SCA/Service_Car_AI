import React, {useState} from "react";
import styled from "styled-components";
import { View, Text, Image, TouchableOpacity } from "react-native";
import CheckBox from "expo-checkbox";

const Container = styled.View`
    flex: 1;
    background-color: white;
    align-items: center;
`;

const ImageBox = styled.View`
    display: flex;
    flex-direction: row;
    margin-top: 20px;
    width: 85%
`;

const CarImage = styled.Image`
    width: 256px;
    height: 256px;
    border-color: black;
    border-width: 2px;
    border-radius: 10px;
`;

const SelectBox = styled.View`
    justify-content: center;
    margin-left: 15px;
`;

const AnswerMask = styled.Image`
    position: absolute;
    width: 256px;
    height: 256px;
    opacity: 1
`;

const BreakageMask = styled.Image`
    position: absolute;
    width: 256px;
    height: 256px;
    opacity: 0
`;

const CrushedMask = styled.Image`
    position: absolute;
    width: 256px;
    height: 256px;
    opacity: 0
`;

const ScratchedMask = styled.Image`
    position: absolute;
    width: 256px;
    height: 256px;
`;

const SeparatedMask = styled.Image`
    position: absolute;
    width: 256px;
    height: 256px;
    opacity: 0.4
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
    font-family: 'Pretendard-SemiBold';
    font-size: 18px;
`;

const ResultText2 = styled.Text`
    font-family: 'Pretendard-Regular';
    font-size: 16px;
    margin-left: 15px;
`;

export default function DamagePage1({ navigation }) {

    const [crushed, isCrushed] = useState(false)
    const [scratched, isScratched] = useState(false)
    const [separated, isSeparated] = useState(false)
    const [breakage, isBreakage] = useState(false)

    const [answer, isAnswer] = useState(false)

    return (
        <Container>
            <Text style={{ fontWeight: "bold", fontSize: 20 }}>데미지 분석 결과</Text>
            <Text>1/1</Text>
            <ImageBox>
                <CarImage source={require("../assets/images/test_input.jpg")} />
                {
                    answer ? <AnswerMask source={require("../assets/images/answer_mask.png")}/>: null
                }
                {
                    breakage ? <BreakageMask source={require("../assets/images/breakage_mask.png")} /> : null
                }
                {
                    crushed ? <CrushedMask source={require("../assets/images/crushed_mask.png")} /> : null
                }
                {
                    scratched ? <ScratchedMask source={require("../assets/images/scratched_mask.png")} /> : null
                }
                {
                    separated ? <SeparatedMask source={require("../assets/images/separated_mask.png")} /> : null
                }
                <SelectBox>
                    <Text style={{fontWeight: "bold"}}>정답 값</Text>
                    <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                        <CheckBox value={answer} onValueChange={isAnswer}></CheckBox>
                        <Text style={{ paddingLeft: 10 }}>Answer</Text>
                    </View>
                    <Text style={{ fontWeight: "bold", marginTop: 20 }}>탐지된 파손</Text>
                    <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                        <CheckBox value={crushed} onValueChange={isCrushed}></CheckBox>
                        <Text style={{ paddingLeft: 10 }}>Crushed</Text>
                    </View>
                    <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                        <CheckBox value={scratched} onValueChange={isScratched}></CheckBox>
                        <Text style={{ paddingLeft: 10 }}>Scratched</Text>
                    </View>
                    <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                        <CheckBox value={separated} onValueChange={isSeparated}></CheckBox>
                        <Text style={{ paddingLeft: 10 }}>Separated</Text>
                    </View>
                    <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                        <CheckBox value={breakage} onValueChange={isBreakage}></CheckBox>
                        <Text style={{ paddingLeft: 10 }}>Breakage</Text>
                    </View>
                </SelectBox>
            </ImageBox>
            <ResultBox>
                <ResultText>손상 파트:   Left Front Fender,</ResultText>
                <ResultText></ResultText>
                <ResultText>Damage 종류 : {'{'}</ResultText>
                <ResultText2>Crushed: 감지되지 않음</ResultText2>
                <ResultText2>Scratched: 9.1% area, 71.2% 신뢰도</ResultText2>
                <ResultText2>Separated: 27.5% area, 88% 신뢰도</ResultText2>
                <ResultText2>Breakage: 감지되지 않음</ResultText2>
                <ResultText>{'},'}</ResultText>
                <ResultText></ResultText>
                <ResultText>심각도: 상</ResultText>
            </ResultBox>
            
            <View style={{
                display: "flex",
                flexDirection: "row",
                justifyContent: "space-between",
                width: "80%",
                marginTop: 30
            }}>
                <TouchableOpacity onPress={() => {
                    navigation.navigate('InputImage')
                }}>
                    <Text style={{ fontSize: 25 }}>{'<'} Prev</Text>
                </TouchableOpacity>
                <TouchableOpacity onPress={() => {
                    navigation.navigate('Repaircost')
                }}>
                    <Text style={{ fontSize: 25 }}>Next {'>'}</Text>
                </TouchableOpacity>
            </View>
            
        </Container>
    );
}
