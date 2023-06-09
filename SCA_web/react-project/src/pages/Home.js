import React, {useEffect, useState, useRef} from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import axios from "axios";
import ReactLoading from "react-loading";

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

    const yearRef = useRef(null);
    const companyRef = useRef(null);
    const [image, setImage] = useState(null)
	const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(()=> {
        if(data!==null){
            setLoading(false);
            navigate('/result', { 
                state : {
                    data: data 
                }
            })
        }
    }, [data])

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
	}

    const apiSend = async() => {
        const firstday = yearRef.current.value
        const company = companyRef.current.value
        if(!firstday){
            alert("연식을 입력해주세요")
        }
        else if(!company){
            alert("제조사를 입력해주세요")
        }
        else{   
            setLoading(true);
            await axios.post(
                url+"main",{
                    "img_string": image.url,
                    "firstday": firstday,
                    "company": company
                },{
                    headers: {
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Headers': '*'
                    }
                }).then((res) => {
                    setData(res.data)
                }).catch((err) => {
                    setLoading(false)
                    setImage(null)
                    alert("오류 발생! 다시 시도해주세요")
                }
            )
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
                        backgroundColor: "white",
                        borderBottom: "0.5px white solid",
                        borderRadius: 15
                    }}
                    onClick={()=>navigate("/")}
                >
                    <h4 style={{
                        color: "black",
                        fontSize: 18
                    }}>General Mode</h4>
                </button>
                <button 
                    style={{
                        width: "90%",
                        backgroundColor: "black",
                        borderBottom: "0.5px white solid"
                    }}
                    onClick={()=>navigate("/test")}
                >
                    <h4 style={{
                        color: "white",
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
                    <h2 style={{color: "black"}}>SCA</h2>
                    <h2 style={{marginTop: -10, color: "black"}}>Car Damage Detection</h2>
                    <div style={{
                        boxShadow: "1px 1px 5px 2px grey",
                        borderRadius: 10,
                        height: 260,
                        width: 260,
                        marginBottom: 30,
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
                            </div>
                            : null
                        }
                        {
                            image === null ? 
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
                            loading ? null: 
                            <img    
                                src={image.url}
                                style={{
                                    width: 260,
                                    height: 260,
                                    borderRadius: 10
                                }}
                            />
                        }
                        
                    </div>
                    {
                        loading === false & image !== null ?
                        <div style={{
                            display: "flex",
                            flexDirection: "column",
                            alignItems: "center"
                        }}>
                            <input
                                type="text"
                                ref={yearRef}
                                placeholder="연식 ex) 2020"
                                style={{
                                    height: 35,
                                    width: 180,
                                    fontSize: 20,
                                    textAlign: "center",
                                    border: "3px solid black",
                                    borderRadius: 15,
                                    marginBottom: 25,
                                }}
                            />
                            <input
                                type="text"
                                ref={companyRef}
                                placeholder="제조사"
                                style={{
                                    height: 35,
                                    width: 180,
                                    fontSize: 20,
                                    textAlign: "center",
                                    border: "3px solid black",
                                    borderRadius: 15,
                                    marginBottom: 25,
                                }}
                            />
                            <div style={{
                                display: "flex",
                                flexDirection: "row",
                                justifyContent: "center",
                                marginBottom: 15
                            }}>
                                <label 
                                    style={{
                                        backgroundColor: "#0f70e6",
                                        color: "white",
                                        padding: 12,
                                        borderRadius: 25,
                                        fontWeight: 900,
                                        fontSize: 18,
                                        marginRight: 10
                                    }}
                                    onClick={()=>setImage(null)}
                                >다시 선택</label>
                                <label 
                                    style={{
                                        backgroundColor: "#0f70e6",
                                        color: "white",
                                        padding: 12,
                                        borderRadius: 25,
                                        fontWeight: 900,
                                        fontSize: 18,
                                        marginLeft: 10
                                    }}
                                    onClick={apiSend}
                                >검사 시작</label>
                            </div>
                        </div>  
                        : null
                    }
                </div>
                
            </Right>
        </Container>
    );
}