import React, {useEffect, useState} from "react";
import { useLocation } from "react-router-dom";
import styled from "styled-components";

const Container = styled.div`
  	background-color: white;
	display: flex;
	flex-direction: column;
	width: 100%;
	align-items: center;
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
	width: 100%;
	padding-left: 20%;
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

export default function Result(){
    const location = useLocation();
    const [data, setData] = useState(null)
    useEffect(()=>{
        setData(location.state.data)
    },[location.state.data])
    const [checkedList, setCheckedList] = useState([]);

    if(data !== null){
        const origImage = data["origImage"]
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
                <h1>Car damage detection</h1>
                <InfoBox>
                    <InfoText style={{marginTop: 50}}>Original Image</InfoText>
                    <OrigImage src={`data:image/jpeg;base64,${origImage}`} />
                </InfoBox>
                <InfoBox>
                    <InfoText>Damaged Parts: &nbsp; {parts}</InfoText>
                    <hr/>
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
                                <hr/>
                            </div>
                            
                        ))
                    }
                </InfoBox>
                
            </Container>
        )
    }
    else{
        return <Container></Container>
    }
}