import React, {useState, useRef, useEffect} from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import axios from "axios";
import ReactLoading from "react-loading"

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

    const url = "http://13.125.213.13:8000/api/"
	//const url = "http://127.0.0.1:8000/api/"

	const indexRef = useRef(null)
	const [data, setData] = useState(null);
	const [loading, setLoading] = useState(false);

	useEffect(()=>{
		if(data!==null){
			setLoading(false);
			navigate('/test_result', {
				state: {
					data: data
				}
			})
		}
	}, [data])

    const testSend = (e) => {
		const index = indexRef.current.value
		if (!index){
			alert("index값을 입력해주세요")
		}
		else{
			setLoading(true);
			axios.post(url+"test", {
				"index": index
			},{
				headers: {
					'Access-Control-Allow-Origin': '*',
					'Access-Control-Allow-Headers': '*'
				}
			}).then(res => {
				setData(res.data)		
			}).catch(err => {
				setLoading(false)
				alert("오류 발생! 다시 시도해주세요")
			})
		}
		
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
						{
                            loading ? 
                            <div style={{
                                display: "flex",
                                width: "100%",
                                height: "100%",
                                alignItems: "center",
                                justifyContent: "center"
                            }}>
                                <ReactLoading
                                    type="spin"
                                    color="#0f70e6"
                                    width={70}
                                    height={70}
                                />
                            </div> :
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
										placeholder="0-999 입력"
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
                        }
						
						
					</div>
				</div>
			</Right>
        </Container>
    );
}