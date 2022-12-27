import React from "react";
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
    let formData;

	const onChange = (e) => {
		const img = e.target.files[0];
        formData = new FormData();
		formData.append('img', img);
		console.log(formData) // FormData {}
		for (const keyValue of formData) console.log(keyValue); // ["img", File] File은 객체
	}

    const onClick = (e) => {
        axios.post(
            "http://127.0.0.1:5000/api/test",
            formData
        ).then((res) => {
            console.log(res);
        }).catch((err) => {
            console.log(err);
        })
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
                <button onClick={onClick}>확인</button>
			</div>
		</Container>
	);
}

export default App;
