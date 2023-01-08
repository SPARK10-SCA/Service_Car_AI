import React, { useState, useEffect } from "react";
import styled from "styled-components";
import { Text, View, Image, TouchableOpacity, ActivityIndicator, Switch } from 'react-native';

const Container = styled.View`
	flex: 1;
	background-color: white;
	align-items: center;
`;

export default function Home({navigation}) {
  	const [isImage, setIsImage] = useState(false);
	const [test, setTest] = useState(false)

	const HeaderRight = () => {
		<Switch 
			trackColor={{false: 'blue', true: 'black'}}
			onValueChange={()=>setTest(!test)}
			value={test}
			style={{
				transform: [{ scaleX: 1.5 }, { scaleY: 1.5 }]
			}}
		/>
	}

	useEffect(()=>{
		navigation.setOptions({
			headerRight: HeaderRight,
		})
	})

	return (
		<Container>
			<Text style={{ 
				fontSize: 30, 
				fontFamily: "Pretendard-SemiBold",
				alignSelf: "flex-start",
				marginTop: 10,
				marginLeft: "10%"
			}}>사진촬영</Text>

			<Text style={{ 
				fontSize: 15,
				alignSelf: "flex-start",
				marginLeft: "10%"
			}}>파손 부위를 촬영해주세요.</Text>

			<View style={{
				alignItems: "center",
				width: "80%",
			}}>
				<Image 
					source={require("../assets/images/example.png")} 
					style={{ 
						width: 350,
						height: 200, 
						marginTop: 20, 
						borderColor: "black",
						borderWidth: 2,
						borderRadius: 15
					}}/>
				{
					isImage ?
					<Image 
						source={require("../assets/images/test_input.jpg")}
						style={{ 
							alignContent: 'center', 
							width: 350, 
							height: 230, 
							marginTop: 20,
							borderColor: "black",
							borderWidth: 2,
							borderRadius: 15
						}} 
					/>:
					<View style={{ 
						alignContent: 'center', 
						width: 350, 
						height: 230, 
						marginTop: 50, 
						borderColor: "black",
						borderWidth: 2,
						borderRadius: 15
					}}></View> 
				}
				<TouchableOpacity onPress={() => {
					setIsImage(true)
					setTimeout(() => {
						navigation.navigate('DamagePage1')
						setIsImage(false)
					}, 5000);
				}}>
					{
						isImage ?
							<View style={{alignItems: "center"}}>
								<ActivityIndicator style={{width: 100, height: 100, marginTop: 25}} size="large" />
								<Text>차량 파손을 측정 중입니다...</Text>
							</View>:
							<Image 
								source={require("../assets/images/shutter.png")}
								style={{
									width: 100, 
									height: 100, 
									marginTop: 25, 
								}}
							/>
					}
				</TouchableOpacity>
			</View>
			
		</Container>
	);
}