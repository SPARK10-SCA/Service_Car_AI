import React, {useState} from "react";
import styled from "styled-components";
import { View, Text, Image, TouchableOpacity, ScrollView } from "react-native";
import CheckBox from "expo-checkbox";

const Container = styled.View`
    flex: 1;
    background-color: white;
    align-items: center;
`;

const Box = styled.View`
    width: 100%;
    align-items: center;
`;

const ImageBox = styled.View`
    display: flex;
    flex-direction: row;
    margin-top: 20px;
    width: 85%
`;

const CarImage = styled.Image`
    width: 230px;
    height: 230px;
    border-color: black;
    border-width: 2px;
    border-radius: 10px;
`;

const SelectBox = styled.View`
    display: flex;
    flex-direction: row;
    margin-left: 15px;
    width: 85%;
    align-items: center;
`;

const AnswerMask = styled.Image`
    position: absolute;
    width: 230px;
    height: 230px;
    opacity: 0.5
`;

const BreakageMask = styled.Image`
    position: absolute;
    width: 230px;
    height: 230px;
    opacity: 0.5
`;

const CrushedMask = styled.Image`
    position: absolute;
    width: 230px;
    height: 230px;
    opacity: 0.5
`;

const ScratchedMask = styled.Image`
    position: absolute;
    width: 230px;
    height: 230px;
    opacity: 0.5
`;

const SeparatedMask = styled.Image`
    position: absolute;
    width: 230px;
    height: 230px;
    opacity: 0.5
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

    const [answerCrushed, isAnswerCrushed] = useState(false)
    const [answerScratched, isAnswerScratched] = useState(false)
    const [answerSeparated, isAnswerSeparated] = useState(false)
    const [answerBreakage, isAnswerBreakage] = useState(false)

    return (
        <Container>
            <ScrollView style={{width: "100%"}}>
                <Box>
                    <Text style={{ fontWeight: "bold", fontSize: 20 }}>데미지 분석 결과</Text>
                    <Text>2/3</Text>
                    <ResultText style={{alignSelf: "flex-start", marginLeft: "7.5%", marginTop: 15}}>손상 파트: Bonnet</ResultText>
                    <ImageBox>
                        <CarImage source={require("../assets/images/test_input.jpg")} />
                        {
                            breakage ? null : null
                        }
                        {
                            crushed ? null : null
                        }
                        {
                            scratched ? <ScratchedMask source={require("../assets/images/Bonnet_Scratched.png")} /> : null
                        }
                        {
                            separated ? <SeparatedMask source={require("../assets/images/Bonnet_Separated.png")} /> : null
                        }
                        {
                            answerBreakage ? <BreakageMask source={require("../assets/images/Breakage_Answer.png")} /> : null
                        }
                        {
                            answerCrushed ? null : null
                        }
                        {
                            answerScratched ? <ScratchedMask source={require("../assets/images/Scratched_Answer.png")} /> : null
                        }
                        {
                            answerSeparated ? <SeparatedMask source={require("../assets/images/Separated_Answer.png")} /> : null
                        }
                        <View style={{marginLeft: 15}}>
                            <Text style={{ fontWeight: "bold" }}>정답 파손 보기</Text>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <Text style={{color: "red"}}> X </Text>
                                <Text style={{ paddingLeft: 10 }}>Crushed</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <CheckBox value={answerScratched} onValueChange={isAnswerScratched}></CheckBox>
                                <Text style={{ paddingLeft: 10 }}>Scratched</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <CheckBox value={answerSeparated} onValueChange={isAnswerSeparated}></CheckBox>
                                <Text style={{ paddingLeft: 10 }}>Separated</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <CheckBox value={answerBreakage} onValueChange={isAnswerBreakage}></CheckBox>
                                <Text style={{ paddingLeft: 10 }}>Breakage</Text>
                            </View>
                        </View>
                    </ImageBox>
                
                    <SelectBox>
                        <Text style={{ fontWeight: "bold", marginRight: 10, marginTop: 15, textAlign: "center"}}>탐지된{"\n"}파손 보기</Text>
                        <View style={{marginRight: 10}}>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <Text style={{color: "red"}}> X </Text>
                                <Text style={{ paddingLeft: 10 }}>Crushed</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <CheckBox value={scratched} onValueChange={isScratched}></CheckBox>
                                <Text style={{ paddingLeft: 10 }}>Scratched</Text>
                            </View>
                        </View>
                        <View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <CheckBox value={separated} onValueChange={isSeparated}></CheckBox>
                                <Text style={{ paddingLeft: 10 }}>Separated</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <Text style={{color: "red"}}> X </Text>
                                <Text style={{ paddingLeft: 10 }}>Breakage</Text>
                            </View>
                        </View>
                        
                    </SelectBox>
                    <ResultBox>

                        <ResultText>Damage 종류 : {'{'}</ResultText>
                        <ResultText2>Crushed: 감지되지 않음</ResultText2>
                        <ResultText2>Scratched: 75.8% 신뢰도</ResultText2>
                        <ResultText2>Separated: 65.8% 신뢰도</ResultText2>
                        <ResultText2>Breakage: 감지되지 않음</ResultText2>
                        <ResultText>{'},'}</ResultText>
                        <ResultText></ResultText>
                        <ResultText>심각도: 상</ResultText>
                    </ResultBox>

                    <ResultBox>
                        <ResultText>정답 파손</ResultText>
                        <ResultText>차량 전체 Damage 종류 : {'{'}</ResultText>
                        <ResultText2>Crushed: X</ResultText2>
                        <ResultText2>Scratched: O</ResultText2>
                        <ResultText2>Separated: O</ResultText2>
                        <ResultText2>Breakage: O</ResultText2>
                        <ResultText>{'},'}</ResultText>
                        <ResultText></ResultText>
                        <ResultText>파트 심각도: 상</ResultText>
                    </ResultBox>
                    
                    <View style={{
                        display: "flex",
                        flexDirection: "row",
                        justifyContent: "space-between",
                        width: "80%",
                        marginTop: 30
                    }}>
                        <TouchableOpacity onPress={() => {
                            navigation.navigate('DamagePage1')
                        }}>
                            <Text style={{ fontSize: 25 }}>{'<'} Prev</Text>
                        </TouchableOpacity>
                        <TouchableOpacity onPress={() => {
                            navigation.navigate('DamagePage3')
                        }}>
                            <Text style={{ fontSize: 25 }}>Next {'>'}</Text>
                        </TouchableOpacity>
                    </View>

                </Box>
            </ScrollView>
            
            
        </Container>
    );
}
