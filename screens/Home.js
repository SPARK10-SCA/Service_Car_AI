import React, { useState } from "react";
import styled from "styled-components";
import { Text, View, Image, TouchableOpacity, ActivityIndicator } from 'react-native';

const Container = styled.View`
	flex: 1;
	background-color: white;
	align-items: center;
`;

export default function Home({navigation}) {
  	const [isImage, setIsImage] = useState(false);

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
						source={require("../assets/images/input.png")}
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
						navigation.navigate('Damage1')
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