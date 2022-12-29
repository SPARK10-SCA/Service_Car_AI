import React, {useState} from "react";
import { createStackNavigator } from "@react-navigation/stack";
import AppLoading from "expo-app-loading";
import { Text } from "react-native";

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
		Jalnan: require("../assets/fonts/Jalnan.otf"),
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
            headerTitle: () => (
                <Text
                  style={{
                    fontSize: 18,
                    fontFamily: 'Jalnan'
                  }}
                >
                  SCA
                </Text>
              ),
              headerTitleAlign: "center",
              headerBackTitle: () => null
        }}>
            <Stack.Screen options={headerOptions} name="Start" component={Start} />
            <Stack.Screen options={headerOptions} name="DamagePage1" component={DamagePage1} />
            <Stack.Screen options={headerOptions} name="DamagePage2" component={DamagePage2} />
            <Stack.Screen options={headerOptions} name="DamagePage3" component={DamagePage3} />
            <Stack.Screen options={headerOptions} name="Repaircost" component={Repaircost} />
        </Stack.Navigator>
    )
}