//set REACT_NATIVE_PACKAGER_HOSTNAME=192.168.0.3

import React from "react";
import { LogBox } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import MainNav from "./Navigators/MainNav";

export default function App() {
	LogBox.ignoreAllLogs();
  	return (
		<NavigationContainer>
			<MainNav />
		</NavigationContainer>
  	);

}