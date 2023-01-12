import React, {useState} from "react";
import styled from "styled-components";
import { View, Text, Image, TouchableOpacity, ScrollView } from "react-native";
import BouncyCheckbox from "react-native-bouncy-checkbox";

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

const DamageMask = styled.Image`
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

export default function DamageTest2({ navigation }) {

    const [crushed, setCrushed] = useState(false)
    const [scratched, setScratched] = useState(false)
    const [separated, setSeparated] = useState(false)
    const [breakage, setBreakage] = useState(false)

    const [answerCrushed, setAnswerCrushed] = useState(false)
    const [answerScratched, setAnswerScratched] = useState(false)
    const [answerSeparated, setAnswerSeparated] = useState(false)
    const [answerBreakage, setAnswerBreakage] = useState(false)

    return (
        <Container>
            <ScrollView style={{width: "100%"}}>
                <Box>
                    <Text style={{ fontWeight: "bold", fontSize: 20 }}>데미지 분석 결과</Text>
                    <Text>2/3</Text>
                    <ResultText style={{alignSelf: "flex-start", marginLeft: "7.5%", marginTop: 15}}>손상 파트: <Text style={{color: "green"}}>Bonnet</Text></ResultText>
                    <ImageBox>
                        <CarImage source={require("../assets/images/test_input.jpg")} />
                        {
                            breakage ? null : null
                        }
                        {
                            crushed ? null : null
                        }
                        {
                            scratched ? <DamageMask source={require("../assets/images/test_output/Bonnet_Scratched.png")} /> : null
                        }
                        {
                            separated ? <DamageMask source={require("../assets/images/test_output/Bonnet_Separated.png")} /> : null
                        }
                        {
                            answerBreakage ? <DamageMask source={require("../assets/images/test_output/Breakage_Answer.png")} /> : null
                        }
                        {
                            answerCrushed ? null : null
                        }
                        {
                            answerScratched ? <DamageMask source={require("../assets/images/test_output/Scratched_Answer.png")} /> : null
                        }
                        {
                            answerSeparated ? <DamageMask source={require("../assets/images/test_output/Separated_Answer.png")} /> : null
                        }
                        <View style={{marginLeft: 15}}>
                            <Text style={{ fontWeight: "bold" }}>정답 파손 보기</Text>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                    disabled={true}
                                    onPress={()=>setAnswerCrushed(!answerCrushed)}
                                    fillColor="gray"
                                    unfillColor="gray"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Crushed</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                    onPress={()=>setAnswerScratched(!answerScratched)}
                                    fillColor="green"
                                    unfillColor="green"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Scratched</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                    onPress={()=>setAnswerSeparated(!answerSeparated)}
                                    fillColor="green"
                                    unfillColor="green"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Separated</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                    onPress={()=>setAnswerBreakage(!answerBreakage)}
                                    fillColor="green"
                                    unfillColor="green"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Breakage</Text>
                            </View>
                        </View>
                    </ImageBox>
                
                    <SelectBox>
                        <Text style={{ fontWeight: "bold", marginRight: 10, marginTop: 15, textAlign: "center"}}>탐지된{"\n"}파손 보기</Text>
                        <View style={{marginRight: 10}}>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                        disabled={true}
                                        onPress={()=>setCrushed(!crushed)}
                                        fillColor="gray"
                                        unfillColor="gray"
                                        style={{
                                            marginRight: -15
                                        }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Crushed</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                    onPress={()=>setScratched(!scratched)}
                                    fillColor="green"
                                    unfillColor="green"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Scratched</Text>
                            </View>
                        </View>
                        <View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                    onPress={()=>setSeparated(!separated)}
                                    fillColor="green"
                                    unfillColor="green"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Separated</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                    disabled={true}
                                    onPress={()=>setBreakage(!breakage)}
                                    fillColor="gray"
                                    unfillColor="gray"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Breakage</Text>
                            </View>
                        </View>
                        
                    </SelectBox>
                    <ResultBox>

                        <ResultText>Damage 종류 : {'{'}</ResultText>
                        <ResultText2>Crushed: 감지되지 않음</ResultText2>
                        <ResultText2>Scratched: 64.8% 신뢰도</ResultText2>
                        <ResultText2>Separated: 88.8% 신뢰도</ResultText2>
                        <ResultText2>Breakage: 감지되지 않음</ResultText2>
                        <ResultText>{'},'}</ResultText>
                        <ResultText></ResultText>
                        <ResultText>파트 파손 심각도: 상</ResultText>
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
                        <ResultText>파트 파손 심각도: 상</ResultText>
                    </ResultBox>
                    
                    <View style={{
                        display: "flex",
                        flexDirection: "row",
                        justifyContent: "space-between",
                        width: "80%",
                        marginTop: 30,
                        marginBottom: 30
                    }}>
                        <TouchableOpacity onPress={() => {
                            navigation.navigate('DamageTest1')
                        }}>
                            <Text style={{ fontSize: 25 }}>{'<'} Prev</Text>
                        </TouchableOpacity>
                        <TouchableOpacity onPress={() => {
                            navigation.navigate('DamageTest3')
                        }}>
                            <Text style={{ fontSize: 25 }}>Next {'>'}</Text>
                        </TouchableOpacity>
                    </View>

                </Box>
            </ScrollView>
            
            
        </Container>
    );
}
