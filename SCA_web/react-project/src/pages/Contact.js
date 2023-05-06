import React from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";

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

const Card = styled.div`
    display: flex;
    align-self: flex-start;
    margin-left: 10%;
    flex-direction: row;
    background-color: white;
    opacity: 0.99;
    padding: 10px;
    border-radius: 15px;
    width: 500px;
    margin-top: 1%;
    margin-bottom: 1%;
`;

const CardImage = styled.img`
    width: 100px;
    height: 120px;
    border-radius: 15px;
`;

export default function Home(){
    const navigate = useNavigate();

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
                            backgroundColor: "black",
                            borderBottom: "0.5px white solid",
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
                            backgroundColor: "white",
                            borderBottom: "0.5px white solid",
                            borderRadius: 15
                        }}
                        onClick={()=>navigate("/contact")}
                    >
                        <h4 style={{
                            color: "black",
                            fontSize: 18
                        }}>Contact</h4>
                    </button>
                </Left>
                <Right>
                    <BackgroundImage src={require("../assets/images/background.jpg")} />
                    <Card>
                        <CardImage src={require("../assets/images/hyunbin.jpg")} />
                        <div style={{
                            display: "flex",
                            flexDirection: "column",
                            marginLeft: 10
                        }}>
                            <label style={{fontSize: 24, fontWeight: 800, marginBottom: 15}}>Leader / Dev</label>
                            <label style={{fontSize: 20}}>Hyunbin Song</label>
                            <label>shbin0519@gmail.com</label>
                        </div>
                    </Card>
                    <Card>
                        <CardImage src={require("../assets/images/minji.jpg")} />
                        <div style={{
                            display: "flex",
                            flexDirection: "column",
                            marginLeft: 10
                        }}>
                            <label style={{fontSize: 24, fontWeight: 800, marginBottom: 15}}>Dev</label>
                            <label style={{fontSize: 20}}>Minji Park</label>
                            <label>mj.park@g.skku.edu</label>
                        </div>
                    </Card>
                    <Card>
                        <CardImage src={require("../assets/images/seongwan.jpg")} />
                        <div style={{
                            display: "flex",
                            flexDirection: "column",
                            marginLeft: 10
                        }}>
                            <label style={{fontSize: 24, fontWeight: 800, marginBottom: 15}}>Dev</label>
                            <label style={{fontSize: 20}}>Seongwan Park</label>
                            <label>dreamnawas@g.skku.edu</label>
                        </div>
                    </Card>
                    <Card>
                        <CardImage src={require("../assets/images/sangyun.jpg")} />
                        <div style={{
                            display: "flex",
                            flexDirection: "column",
                            marginLeft: 10
                        }}>
                            <label style={{fontSize: 24, fontWeight: 800, marginBottom: 15}}>Dev</label>
                            <label style={{fontSize: 20}}>Sangyun Shin</label>
                            <label>sangyun0914@g.skku.edu</label>
                        </div>
                    </Card>           
                </Right>
        </Container>
    );
}