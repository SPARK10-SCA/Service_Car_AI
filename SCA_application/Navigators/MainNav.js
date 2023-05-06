import React, {useState} from "react";
import { createStackNavigator } from "@react-navigation/stack";
import AppLoading from "expo-app-loading";
import { Text } from "react-native";
import * as Font from "expo-font"

import Start from "../screens/Start.js";
import SelectMode from "../screens/SelectMode.js";
import Home from "../screens/Home.js";
import Damage1 from "../screens/Damage1.js";
import Damage2 from "../screens/Damage2.js";
import Damage3 from "../screens/Damage3.js";
import TestHome from "../screens/TestHome.js";
import DamageTest1 from '../screens/DamageTest1.js';
import DamageTest2 from '../screens/DamageTest2.js';
import DamageTest3 from '../screens/DamageTest3.js';
import RepairCost from '../screens/RepairCost.js';
import RepairCost2 from "../screens/RepairCost2.js";
import NearCenter from "../screens/NearCenter.js";

const Stack = createStackNavigator();

export default function MainNav(){
    const [fontLoading, setFontLoading] = useState(true);
	const loadFonts = async () => {
        await Font.loadAsync({
            "Pretendard-Light": require("../assets/fonts/Pretendard-Light.otf"),
            "Pretendard-SemiBold": require("../assets/fonts/Pretendard-SemiBold.otf"),
            "Pretendard-Medium": require("../assets/fonts/Pretendard-Medium.otf"),
            "Pretendard-Bold": require("../assets/fonts/Pretendard-Bold.otf"),
            "Pretendard-Regular": require("../assets/fonts/Pretendard-Regular.otf"),
            "Pretendard-ExtraBold": require("../assets/fonts/Pretendard-ExtraBold.otf"),
            "Pretendard-Black": require("../assets/fonts/Pretendard-Black.otf"),
            Jalnan: require("../assets/fonts/Jalnan.otf")
        });
	};

    if (fontLoading) {
		return (
			<AppLoading
				startAsync={loadFonts}
				onFinish={() => { setFontLoading(false) }}
				onError={console.warn}
			/>
		);
	}
    return(
        <Stack.Navigator screenOptions={{
            headerTitleAlign: "center",
			headerBackTitle: null
        }}>
            <Stack.Screen 
				name="Start"
				options={{
					headerShown: false
				}} 
				component={Start} 
			/>
			<Stack.Screen
				name="SelectMode"
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							모드 선택
						</Text>
				  	),
					headerLeft: () => null
				}}
				component={SelectMode}
			/>
            <Stack.Screen 
				name="Home" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							차량 사진 촬영
						</Text>
				  	),
				}}
				component={Home} 
			/>
			<Stack.Screen 
				name="Damage1" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							차량 파손 진단
						</Text>
				  	),
				}}
				component={Damage1}
			/>
			<Stack.Screen 
				name="Damage2" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							차량 파손 진단
						</Text>
				  	),
				}}
				component={Damage2}
			/>
			<Stack.Screen 
				name="Damage3" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							차량 파손 진단
						</Text>
				  	),
				}}
				component={Damage3}
			/>
			<Stack.Screen 
				name="TestHome" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							테스트 이미지 선택
						</Text>
				  	),
				}}
				component={TestHome} 
			/>
            <Stack.Screen 
				name="DamageTest1" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							차량 파손 진단
						</Text>
				  	),
				}}
				component={DamageTest1}
			/>
            <Stack.Screen 
				name="DamageTest2"
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							차량 파손 진단
						</Text>
				  	),
				}}
				component={DamageTest2} 
			/>
            <Stack.Screen 
				name="DamageTest3" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							차량 파손 진단
						</Text>
				  	),
				}}
				component={DamageTest3} 
			/>
            <Stack.Screen 
				name="RepairCost" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							수리 비용 진단
						</Text>
				  	),
				}}
				component={RepairCost} 
			/>
			<Stack.Screen 
				name="RepairCost2" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							수리 비용 진단
						</Text>
				  	),
				}}
				component={RepairCost2} 
			/>
			<Stack.Screen
				name="NearCenter"
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							근처 수리점 정보
						</Text>
					),
				}}
				component={NearCenter}
			/>
        </Stack.Navigator>
    )
}