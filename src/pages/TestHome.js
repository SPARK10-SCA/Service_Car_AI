import React, {useState, useEffect, useRef} from "react";
import styled from "styled-components";
import axios from "axios";

const Container = styled.div``;

export default function TestHome(){
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
				<h4>index를 입력해주세요</h4>
				<div>
					<input type='text' ref={indexRef}/>
					<button onClick={testSend}>확인</button>
				</div>
			</Container>
		);
	}	
}