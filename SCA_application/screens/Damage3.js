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
    opacity: 0.4;
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

export default function Damage1({ navigation }) {

    const [crushed, setCrushed] = useState(false)
    const [scratched, setScratched] = useState(false)
    const [separated, setSeparated] = useState(false)
    const [breakage, setBreakage] = useState(false)

    return (
        <Container>
            <ScrollView style={{width: "100%"}}>
                <Box>
                    <Text style={{ fontWeight: "bold", fontSize: 20 }}>데미지 분석 결과</Text>
                    <Text>3/3</Text>
                    <ResultText style={{alignSelf: "flex-start", marginLeft: "7.5%", marginTop: 15}}>손상 파트: <Text style={{color: "green"}}>Front Bumper</Text></ResultText>
                    <ImageBox>
                        <CarImage source={require("../assets/images/input.png")} />
                        {
                            breakage ? <DamageMask source={require("../assets/images/output/Front_Bumper_Breakage.png")} /> : null
                        }
                        {
                            crushed ? null : null
                        }
                        {
                            scratched ? <DamageMask source={require("../assets/images/output/Front_Bumper_Scratched.png")} />: null
                        }
                        {
                            separated ? null : null
                        }


                    </ImageBox>
                
                    <SelectBox>
                        <Text style={{ fontWeight: "bold", marginRight: 10, marginTop: 15, textAlign: "center"}}>탐지된{"\n"}파손 보기</Text>
                        <View style={{marginRight: 10}}>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox
                                    disabled={true} 
                                    onPress={()=>setCrushed(!crushed)}
                                    fillColor="grey"
                                    unfillColor="grey"
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
                                    disabled={true}
                                    onPress={()=>setSeparated(!separated)}
                                    fillColor="grey"
                                    unfillColor="grey"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Separated</Text>
                            </View>
                            <View style={{ flexDirection: 'row', paddingTop: 15 }}>
                                <BouncyCheckbox 
                                    onPress={()=>setBreakage(!breakage)}
                                    fillColor="green"
                                    unfillColor="green"
                                    style={{
                                        marginRight: -15
                                    }}
                                />
                                <Text style={{ paddingLeft: 10 }}>Breakage</Text>
                            </View>
                        </View>
                        
                    </SelectBox>
                    <ResultBox>
                        <ResultText>탐지된 파손</ResultText>
                        <ResultText>Damage 종류 : {'{'}</ResultText>
                        <ResultText2>Crushed: 발견되지 않음</ResultText2>
                        <ResultText2>Scratched: 76.3% 신뢰도</ResultText2>
                        <ResultText2>Separated: 발견되지 않음</ResultText2>
                        <ResultText2>Breakage: 84.9% 신뢰도</ResultText2>
                        <ResultText>{'},'}</ResultText>
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
                            navigation.navigate('Damage2')
                        }}>
                            <Text style={{ fontSize: 25 }}>{'<'} Prev</Text>
                        </TouchableOpacity>
                        <TouchableOpacity onPress={() => {
                            navigation.navigate('RepairCost2')
                        }}>
                            <Text style={{ fontSize: 25 }}>Next {'>'}</Text>
                        </TouchableOpacity>
                    </View>
                </Box>
            </ScrollView>
            
            
        </Container>
    );
}
