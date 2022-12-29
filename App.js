import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, Platform, TouchableOpacity, Button, TouchableHighlight } from 'react-native';
import { useState } from 'react';
import { ActivityIndicator, Alert } from "react-native";
import Start from "./screen/Start.js";
import DamagePage1 from './screen/DamagePage1.js';
import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import DamagePage3 from './screen/DamagePage3.js';
import DamagePage2 from './screen/DamagePage2.js';
import Repaircost from './screen/Repaircost.js';
export default function App() {
  const Stack = createStackNavigator();

  const headerOptions = {
    headerTitle: () => (
      <Text
        style={{
          fontSize: 18,
        }}
      >
        SCA
      </Text>
    ),
    headerTitleAlign: "center",
    headerBackTitle: () => null
  }

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Start">
        <Stack.Screen options={headerOptions} name="Start" component={Start} />
        <Stack.Screen options={headerOptions} name="DamagePage1" component={DamagePage1} />
        <Stack.Screen options={headerOptions} name="DamagePage2" component={DamagePage2} />
        <Stack.Screen options={headerOptions} name="DamagePage3" component={DamagePage3} />
        <Stack.Screen options={headerOptions} name="Repaircost" component={Repaircost} />

      </Stack.Navigator>
    </NavigationContainer>
  );

}