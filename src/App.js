import React from "react";
import styled from "styled-components"

const Container = styled.div`
  	background-color: white;
	display: flex;
	flex-direction: column;
	position: relative;
	width: 100%;
	align-items: center;
`;

function App() {
	const onChange = (e) => {
		const img = e.target.files[0];
		const formData = new FormData();
		formData.append('img', img);
		console.log(formData) // FormData {}
		for (const keyValue of formData) console.log(keyValue); // ["img", File] File은 객체
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
			</div>
		</Container>
	);
}

export default App;
