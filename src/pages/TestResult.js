import React, {useEffect, useState} from "react";
import { useNavigate, useLocation } from "react-router-dom";
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
    height: 100%;
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
	font-size: 24px;
	font-weight: 600;
`;

const InfoText2 = styled.h2`
	align-self: flex-start;
	font-size: 20px;
	font-weight: 500;
	text-transform: capitalize;
`

const InfoBox = styled.div`
	background-color: white;
	width: 90%;
    padding-left: 10%;
`;

const OrigImage = styled.img`
	border: 1px solid rgb(0,0,0);
	width: 256px;
	height: 256px;
	margin-top: 20px;
	margin-bottom: 20px;
`;

const PartImage = styled.img`
	border: 2px solid rgb(0,0,0);
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

export default function TestResult(){
    const navigate = useNavigate()
    const location = useLocation();
    const [data, setData] = useState(null)
    useEffect(()=>{
        setData(location.state.data)
    },[location.state.data])
    const [checkedList, setCheckedList] = useState([]);

    if(data !== null){
        const origImage = data["origImage"]
        const origMask = data["origMask"]
        const parts = data["part"].join(", ")
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
                    <div style={{width: "100%", border: "1px solid white"}}/>
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
                        <InfoText style={{marginTop: 50}}>Original Image</InfoText>
                        <OrigImage src={`data:image/jpeg;base64,${origImage}`} />
                        <OrigImage src={`data:image/jpeg;base64,${origMask}`} />
                    </InfoBox>
                    <InfoBox>
                        <InfoText>Damaged Parts: &nbsp; {parts}</InfoText>
                        <div style={{width:"80%", border: "1px solid black", marginBottom: 10}}/>
                        {
                            infoList.map((index) => (
                                <div>
                                    <InfoText>Part: {index.part}</InfoText>
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
                                                                marginLeft: 10,
                                                                alignItems: "center"
                                                            }}
                                                        >
                                                            <input
                                                                disabled={index.checkbox_info[disable]}
                                                                type="checkbox"
                                                                value={index.part+'_'+item.value}
                                                                onChange={handleSelect}
                                                                style={{
                                                                    height: 20,
                                                                    width: 20,
                                                                }}
                                                            />
                                                            <label style={{fontSize: 20, marginLeft: 10}}>{item.value}</label>
                                                        </div>
                                                    );
                                                })
                                            }
                                        </div>
                                    </div>
                                    
                                    <InfoText>Damage Info</InfoText>
                                    <InfoText2>{index.damage_info[0]}</InfoText2>
                                    <InfoText2>{index.damage_info[1]}</InfoText2>
                                    <InfoText2>{index.damage_info[2]}</InfoText2>
                                    <InfoText2>{index.damage_info[3]}</InfoText2>
                                    <br/>
                                    <InfoText>Repair Method: <InfoText2>{index.repair_method}</InfoText2></InfoText>
                                    <InfoText>Repair Cost: <InfoText2>{index.repair_cost} Won</InfoText2></InfoText>
                                    <div style={{width:"80%", border: "1px solid black", marginBottom: 10}}/>
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