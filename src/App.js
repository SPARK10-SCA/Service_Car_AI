import React, { useRef, useState } from "react";
import styled from "styled-components"
import axios from 'axios';

const Container = styled.div`
  	background-color: white;
	display: flex;
	flex-direction: column;
	width: 100%;
	align-items: center;
`;

const Prev = styled.button`
	background-color: white;
	border: 1px solid;
	border-radius: 20px;
	padding-left: 20px;
	padding-right: 20px;
	position: absolute;
	left: 10%;
	top: 18px;
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

function App() {
	const url = "http://127.0.0.1:8080/api/"
	const indexRef = useRef(null)
    let formData;

	const [data, setData] = useState(null);
	const [checkedList, setCheckedList] = useState([]);

	const onChange = (e) => {
		const img = e.target.files[0];
        formData = new FormData();
		formData.append('img', img);
		console.log(formData) // FormData {}
		for (const keyValue of formData) console.log(keyValue); // ["img", File] File은 객체
	}

    const apiSend = (e) => {
        axios.post(
            url+"main",
            formData
        ).then((res) => {
            console.log(res);
        }).catch((err) => {
            console.log(err);
        })
		//console.log('Pressed')
    }

	const testSend = (e) => {
        axios.post(url+"test", {
			"index": indexRef.current.value
		},{
			headers: {
				'Access-Control-Allow-Origin': '*',
				'Access-Control-Allow-Headers': '*'
			}
		}).then(res => {
			setData(res.data)
		}).catch(err => {
			console.log(err)
		})
		//console.log('Pressed', indexRef.current.value)
    }
	if (data == null){
		return (
			<Container>
				<h1>Car damage detection</h1>
				<h4>사진을 선택해주세요</h4>
				<div>
					<input type='file' 
						accept='image/jpg,impge/png,image/jpeg' 
						name='input_img' 
						onChange={onChange}>
					</input>
					<button onClick={apiSend}>확인</button>
				</div>
				<h4>index를 입력해주세요</h4>
				<div>
					<input type='text' ref={indexRef}/>
					<button onClick={testSend}>확인</button>
				</div>
	
			</Container>
		);
	}	
	else{
		const origImage = data["origImage"]
		//const origMask = data["origMask"]
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
				<Prev onClick={()=>setData(null)}><h2>이전</h2></Prev>
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
									<div>
										{
											checkValues.map((item) => {
												return (
													<div key={item.id}>
														<input
															type="checkbox"
															value={item.value}
															onChange={handleSelect}
														/>
														<label>{item.value}</label>
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
	
}

export default App;
