import React, {useEffect, useState} from "react";
import { useLocation, useNavigate } from "react-router-dom";
import styled from "styled-components";

const Container = styled.div`
  	height: 100%;
    width: 100%;
`;

const Left = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 10%;
    height: 450%;
    float: left;
    background-color: black;
`;

const Logo = styled.img`
    width: 200px;
    height: 180px;
    margin-top: -30px;
`;

const Right = styled.div`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 90%;
    float: right;
`;

const InfoText = styled.h2`
	align-self: flex-start;
	font-size: 20px;
	font-weight: 500;
	text-transform: capitalize;
`

const BlueSticker = styled.h2`
    font-size: 24px;
    background-color: #0f70e6;
    color: white;
    padding: 8px;
    border-radius: 10px;
    margin-right: 30px;
`;

const BlackSticker = styled.h2`
    width: fit-content;
    font-size: 24px;
    color: black;
`

const WhiteSticker = styled.h2`
    font-size: 20px;
    background-color: white;
    color: black;
    padding: 8px;
    border: 2px solid black;
    border-radius: 15px;
    margin-right: 15px;
`

const InfoBox = styled.div`
	background-color: white;
	width: 90%;
	padding-left: 5%;
`;

const OrigImage = styled.img`
	border: 2px solid rgb(0,0,0);
    border-radius: 15px;
    margin-top: 20px;
	width: 256px;
	height: 256px;
`;

const PartImage = styled.img`
	border: 2px solid rgb(0,0,0);
    border-radius: 15px;
	width: 256px;
	height: 256px;
	margin-top: 20px;
	margin-bottom: 20px;
`;

const DamageMask = styled.img`
	position: absolute;
	width: 256px;
	height: 256px;
	margin-top: 20px;
	border: 1px solid rgb(0,0,0);
	opacity: 0.4;
`;

export default function Result(){
    const navigate = useNavigate();
    const location = useLocation();
    const [data, setData] = useState(null)
    useEffect(()=>{
        setData(location.state.data)
    },[location.state.data])
    const [checkedList, setCheckedList] = useState([]);

    if(data !== null){
        const origImage = data["origImage"]
        const parts = data["part"]
        const infoList = data["info"]

        const checkValues = [
            {id: 1, value: "Breakage"},
            {id: 2, value: "Crushed"},
            {id: 3, value: "Scratched"},
            {id: 4, value: "Separated"}
        ]

        const handleSelect = (event) => {
            const value = event.target.value;
            const isChecked = event.target.checked;
            
            if (isChecked) {
                //Add checked item into checkList
                setCheckedList([...checkedList, value]);
            } else {
                //Remove unchecked item from checkList
                const filteredList = checkedList.filter((item) => item !== value);
                setCheckedList(filteredList);
            }
            };

        return (
            <Container>
                <Left>
                    <Logo src={require("../assets/images/car_icon.png")} />
                    <h4 style={{
                        color: "white",
                        marginTop: -60
                    }}>Service Car AI</h4>
                    <h4 style={{
                        color: "white",
                        marginTop: -20,
                        fontSize: 24,
                        marginBottom: 10
                    }}>SCA</h4>
                    <div style={{width:"80%", border: "1px solid black", marginBottom: 10}}/>
                    <button 
                        style={{
                            width: "90%",
                            backgroundColor: "black",
                            borderBottom: "0.5px white solid",
                        }}
                        onClick={()=>navigate("/")}
                    >
                        <h4 style={{
                            color: "white",
                            fontSize: 18
                        }}>General Mode</h4>
                    </button>
                    <button 
                        style={{
                            width: "90%",
                            backgroundColor: "white",
                            borderBottom: "0.5px white solid",
                            borderRadius: 15
                        }}
                        onClick={()=>navigate("/test")}
                    >
                        <h4 style={{
                            color: "black",
                            fontSize: 18
                        }}>Test Mode</h4>
                    </button>
                    <button 
                        style={{
                            width: "90%",
                            backgroundColor: "black",
                            borderBottom: "0.5px white solid"
                        }}
                        onClick={()=>navigate("/contact")}
                    >
                        <h4 style={{
                            color: "white",
                            fontSize: 18
                        }}>Contact</h4>
                    </button>
                </Left>
                <Right>
                    <InfoBox>
                        <div style={{
                            width: "60%",
                            border: "2px solid black",
                            borderRadius: 25,
                            marginTop: 30,
                            marginBottom: 20,
                            paddingLeft: 30,
                        }}>
                            <BlueSticker>Original Image</BlueSticker>
                            <OrigImage src={`data:image/jpeg;base64,${origImage}`} />
                            <BlackSticker>Damaged Parts</BlackSticker>
                            <div style={{
                                display: "flex",
                                flexDirection: "row",
                                marginTop: -15
                            }}>
                                {
                                    parts.map((item) => (
                                        <WhiteSticker>{item}</WhiteSticker>
                                    ))
                                }
                            </div>
                            
                        </div>
                    </InfoBox>
                    <InfoBox>
                        {
                            infoList.map((index) => (
                                <div style={{
                                    width: "60%",
                                    border: "2px solid black",
                                    borderRadius: 25,
                                    marginBottom: 20,
                                    paddingLeft: 30
                                }}>
                                    <BlueSticker>{index.part}</BlueSticker>

                                    <div style={{
                                        display: "flex",
                                        flexDirection: "row"
                                    }}>
                                        <PartImage src={`data:image/jpeg;base64,${index.part_img}`}/>
                                        {
                                            checkedList.find(v => v === index.part+'_Breakage') ? 
                                            <DamageMask src={`data:image/jpeg;base64,${index.damage_mask[0]}`} />:null
                                        }
                                        {
                                            checkedList.find(v => v === index.part+'_Crushed') ? 
                                            <DamageMask src={`data:image/jpeg;base64,${index.damage_mask[1]}`} />:null
                                        }
                                        {
                                            checkedList.find(v => v === index.part+'_Scratched') ?
                                            <DamageMask src={`data:image/jpeg;base64,${index.damage_mask[2]}`} />:null
                                        }
                                        {
                                            checkedList.find(v => v === index.part+'_Separated') ?
                                            <DamageMask src={`data:image/jpeg;base64,${index.damage_mask[3]}`} />:null
                                        }
                                        <div style={{
                                            display: "flex",
                                            flexDirection: "column",
                                            marginTop: 20,
                                            height: 256,
                                            justifyContent: "center"
                                        }}>
                                            {
                                                checkValues.map((item) => {
                                                    const disable = index.part+'_'+item.value+'_disable'
                                                    return (
                                                        <div 
                                                            key={item.id} 
                                                            style={{
                                                                display: "flex",
                                                                marginTop: 10, 
                                                                marginBottom: 10, 
                                                                marginLeft: 30,
                                                                alignItems: "center"
                                                            }}
                                                        >
                                                            <input
                                                                disabled={index.checkbox_info[disable]}
                                                                type="checkbox"
                                                                value={index.part+'_'+item.value}
                                                                onChange={handleSelect}
                                                                style={{
                                                                    height: 25,
                                                                    width: 25,
                                                                }}
                                                            />
                                                            <label style={{fontSize: 25, marginLeft: 10}}>{item.value}</label>
                                                        </div>
                                                    );
                                                })
                                            }
                                        </div>
                                    </div> 
                                    <BlackSticker>Damage Info</BlackSticker>
                                    <InfoText>{index.damage_info[0]}</InfoText>
                                    <InfoText>{index.damage_info[1]}</InfoText>
                                    <InfoText>{index.damage_info[2]}</InfoText>
                                    <InfoText>{index.damage_info[3]}</InfoText>
                                    <br/>
                                    <BlackSticker>Repair Method</BlackSticker>
                                    <InfoText>{index.repair_method}</InfoText>
                                    <br/>
                                    <BlackSticker>Repair Cost</BlackSticker>
                                    <InfoText>{index.repair_cost} Won</InfoText>
                                    <br/>
                                </div>
                            ))
                        }
                    </InfoBox>
                </Right>             
            </Container>
        )
    }
    else{
        return <Container></Container>
    }
}