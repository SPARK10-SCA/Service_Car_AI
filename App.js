import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, Platform, TouchableOpacity, Button, TouchableHighlight } from 'react-native';
import { useState } from 'react';
import { ActivityIndicator, Alert } from "react-native";
import Start from "./screens/Start.js";
import DamagePage1 from './screens/DamagePage1.js';
import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import DamagePage3 from './screens/DamagePage3.js';
import DamagePage2 from './screens/DamagePage2.js';
import Repaircost from './screens/Repaircost.js';
export default function App() {
  const Stack = createStackNavigator();

  const headerOptions = {
    
  }

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Start">
        

      </Stack.Navigator>
    </NavigationContainer>
  );

}