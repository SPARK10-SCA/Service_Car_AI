import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import MainNav from "./Navigators/MainNav";

export default function App() {

  	return (
		<NavigationContainer>
			<MainNav />
		</NavigationContainer>
  	);

}