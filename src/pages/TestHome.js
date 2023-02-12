import React, {useState, useRef} from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import axios from "axios";

const Container = styled.div`
    height: 100%;
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
    align-items: center;
	justify-content: center;
    width: 90%;
    height: 100%;
    float: right;
    background-color: white;
`;

const BackgroundImage = styled.img`
    width: 120%;
    height: 100%;
    left: 10%;
    position: absolute;
`;

export default function Home(){
    const navigate = useNavigate();

    const url = "http://127.0.0.1:8080/api/"

	const indexRef = useRef(null)
	const [data, setData] = useState(null);

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
			if(data!=null){
				navigate("/test_result", {
					state: {
						data: data
					}
				})
			}
		}).catch(err => {
			console.log(err)
		})
		//console.log('Pressed', indexRef.current.value)
    }

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
				<BackgroundImage src={require("../assets/images/background.jpg")} />
				<div style={{  
					display:"flex",
					flexDirection: "column",
					alignItems: "center",
					backgroundColor: "white",
					width: 500,
					height: "auto",
					border: "2px solid black",
					borderRadius: 20,
					opacity: 0.99
				}}>
					<h2>SCA</h2>
					<h2 style={{marginTop: -10}}>Car Damage Detection</h2>
					
					<div style={{
						boxShadow: "1px 1px 5px 2px grey",
						borderRadius: 10,
						height: 260,
						width: 260,
						marginBottom: 30
					}}>

						<div style={{
							display: "flex",
							flexDirection: "column",
							alignItems: "center",
							justifyContent: "center",
							height: "100%",
						}}>
							<img 
								src={require("../assets/images/image_icon.png")}
								style={{
									width: 150,
									height: 150
								}} 
							/>
							<div style={{
								display: "flex",
								flexDirection: "row",
								alignItems: "center",
								border: "2px solid black",
								width: "75%",
								height: 35,
								borderRadius: 25,
								backgroundColor: "#0f70e6"
							}}>
								<input
									type="text"
									ref = {indexRef}
									placeholder="1-1000 입력"
									style={{
										border: "0px",
										width: "70%",
										height: "90%",
										fontSize: 18,
										paddingLeft: 10,
										marginRight: 8,
										borderTopLeftRadius: 18,
										borderBottomLeftRadius: 18
									}}
								/>
								<label 
									style={{
										fontSize: 15,
										fontWeight: 600,
										color: "white",
									}}
									onClick={testSend}
								>확인</label>
							</div>
						</div>
						
					</div>
				</div>
			</Right>
        </Container>
    );
}