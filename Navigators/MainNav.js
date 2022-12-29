import React, {useState} from "react";
import { createStackNavigator } from "@react-navigation/stack";
import AppLoading from "expo-app-loading";
import { Text } from "react-native";
import * as Font from "expo-font"

import Start from "../screens/Start.js";
import InputImage from "../screens/InputImage.js";
import DamagePage1 from '../screens/DamagePage1.js';
import DamagePage3 from '../screens/DamagePage3.js';
import DamagePage2 from '../screens/DamagePage2.js';
import Repaircost from '../screens/Repaircost.js';
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
              headerBackTitle: () => null,
        }}>
            <Stack.Screen 
				name="Start"
				options={{
					headerShown: false
				}} 
				component={Start} 
			/>
            <Stack.Screen 
				name="InputImage" 
				options={{
					headerTitle: () => (
						<Text
						style={{
							fontSize: 18,
							fontFamily: 'Pretendard-Bold'
						}}
						>
							차량 사진 불러오기
						</Text>
				  	),
					headerLeft: () => null
				}}
				component={InputImage} 
			/>
            <Stack.Screen 
				name="DamagePage1" 
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
				component={DamagePage1}
			/>
            <Stack.Screen 
				name="DamagePage2"
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
				component={DamagePage2} 
			/>
            <Stack.Screen 
				name="DamagePage3" 
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
				component={DamagePage3} 
			/>
            <Stack.Screen 
				name="Repaircost" 
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
				component={Repaircost} 
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