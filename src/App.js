import React, { useRef } from "react";
import styled from "styled-components"
import axios from 'axios';

const Container = styled.div`
  	background-color: white;
	display: flex;
	flex-direction: column;
	position: relative;
	width: 100%;
	align-items: center;
`;

function App() {
	const url = "http://127.0.0.1:10250/api/"
	const indexRef = useRef(null)
    let formData;
	

	const onChange = (e) => {
		const img = e.target.files[0];
        formData = new FormData();
		formData.append('img', img);
		console.log(formData) // FormData {}
		for (const keyValue of formData) console.log(keyValue); // ["img", File] File은 객체
	}

    const apiSend = (e) => {
        axios.post(
            url+"test",
            formData
        ).then((res) => {
            console.log(res);
        }).catch((err) => {
            console.log(err);
        })
		console.log('Pressed')
    }

	const testSend = (e) => {
        fetch(url+"test", {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': '*',
				'Access-Control-Allow-Headers': '*'
			},
			body: JSON.stringify({
				"index": indexRef.current.value
			})
		}).then(res => {
			console.log(res)
		}).catch(err => {
			console.log(err)
		})
		console.log('Pressed', indexRef.current.value)
    }

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

export default App;
