import React, {useState} from "react";
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
    width: 90%;
    height: 100%;
    float: right;
    background-color: white;
`;

const BackgroundImage = styled.img`
    width: 100%;
    height: 70%;
    margin-top: -5%;
`;

export default function Home(){
    const url = "http://127.0.0.1:8080/api/"
    let formData;
    
    const [image, setImage] = useState(null)
	const [data, setData] = useState(null);
	const [checkedList, setCheckedList] = useState([]);

	const onChange = (e) => {
        e.preventDefault();
        const fileReader = new FileReader()
		const img = e.target.files[0];
        if(img){
            fileReader.readAsDataURL(img)
        }
        fileReader.onload = () => {
            setImage({
                file: img,
                url: fileReader.result
            })
        }
        formData = new FormData();
		formData.append('img', image.file);
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
    }

    if (data == null){
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
                            marginTop: -20
                        }}>SCA</h4>
                        <div style={{width: "100%", border: "1px solid white"}}/>
                        <button style={{
                            width: "90%",
                            backgroundColor: "black",
                            borderBottom: "0.5px white solid"
                        }}>
                            <h4 style={{
                                color: "white",
                                fontSize: 18
                            }}>General Mode</h4>
                        </button>
                        <button style={{
                            width: "90%",
                            backgroundColor: "black",
                            borderBottom: "0.5px white solid"
                        }}>
                            <h4 style={{
                                color: "white",
                                fontSize: 18
                            }}>Test Mode</h4>
                        </button>
                        <button style={{
                            width: "90%",
                            backgroundColor: "black",
                            borderBottom: "0.5px white solid"
                        }}>
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
                            position: "absolute",
                            alignItems: "center",
                            backgroundColor: "white",
                            width: "40%",
                            border: "2px solid black",
                            borderRadius: 20,
                            top: "40%"
                        }}>
                            <h2>SCA</h2>
                            <h2 style={{marginTop: -10}}>Car Damage Detection</h2>
                            
                            <div style={{
                                boxShadow: "1px 1px 5px 2px grey",
                                borderRadius: 10,
                                height: 320,
                                width: 320,
                                marginBottom: 30
                            }}>
                                {
                                    image === null ? 
                                    <div style={{
                                        display: "flex",
                                        flexDirection: "column",
                                        alignItems: "center",
                                        justifyContent: "center",
                                        height: "100%"
                                    }}>
                                        <img 
                                            src={require("../assets/images/image_icon.png")}
                                            style={{
                                                width: 150,
                                                height: 150
                                            }} 
                                        />
                                        <input 
                                            id="inputImage"
                                            type='file' 
                                            accept='image/jpg,impge/png,image/jpeg' 
                                            onChange={onChange}
                                            style={{
                                                display: "none"
                                            }}
                                        />
                                        <label 
                                            htmlFor="inputImage"
                                            style={{
                                                backgroundColor: "#0f70e6",
                                                color: "white",
                                                padding: 12,
                                                borderRadius: 25,
                                                marginTop: 10,
                                                fontWeight: 900,
                                                fontSize: 18
                                            }}
                                        >이미지 업로드</label>
                                    </div>: 
                                    <img    
                                        src={image.url}
                                        style={{
                                            width: 320,
                                            height: 320,
                                            borderRadius: 10
                                        }}
                                    />
                                }
                               
                            </div>
                        </div>
                        
                    </Right>
			</Container>
		);
	}	
}