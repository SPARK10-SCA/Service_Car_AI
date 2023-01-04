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

const InfoText = styled.text`
	align-self: flex-start;
	margin-left: 10%;
	font-size: 24px;
	font-weight: 600;
`;

const InfoBox = styled.div`
	background-color: white;
	width: 80%;
`;

const OrigImage = styled.img`
	border: 2px solid rgb(0,0,0);
	width: 192px;
	height: 192px;
	margin-top: 20px;
	margin-bottom: 20px;
`;

function App() {
	const url = "http://127.0.0.1:8080/api/"
	const indexRef = useRef(null)
    let formData;

	const [data, setData] = useState(null)

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
		console.log('Pressed')
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
		console.log('Pressed', indexRef.current.value)
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
		const parts = data["part"].join(", ")
		return (
			<Container>
				<h1>Car damage detection</h1>
				<Prev onClick={()=>setData(null)}><h2>이전</h2></Prev>
				<InfoText style={{marginTop: 50}}>Original Image</InfoText>
				<InfoBox>
					<OrigImage src={`data:image/jpeg;base64,${origImage}`} />
				</InfoBox>
				<InfoText>Damaged Parts: &nbsp; {parts}</InfoText>
			</Container>
		)
	}
	
}

export default App;
