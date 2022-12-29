import React from "react";
import { StyleSheet, Text, View, Image, Platform, TouchableOpacity, Button, TouchableHighlight } from 'react-native';
import { useState } from 'react';
import { ActivityIndicator, Alert } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

function Start({navigation}) {
  const [image, setImage] = useState(true);
  return (
    <View style={styles.container}>
      <Text style={{ fontSize: 30 }}>사진촬영</Text>
      <Text style={{ margin: 5 }}>파손 부위를 촬영해주세요.</Text>

      <Image style={{ alignContent: 'center', width: 350, height: 230, marginTop: 20 }} source={require("../assets/car_damage2.png")}></Image>
      {
        image ?
          <Text style={{ alignContent: 'center', width: 350, height: 230, marginTop: 50, borderWidth: 2 }} ></Text> :
          <Image style={{ alignContent: 'center', width: 350, height: 230, marginTop: 20 }} source={require("../assets/damagecar.jpg")}></Image>
      }
      <TouchableOpacity onPress={() => {
        setImage(!image)
        setTimeout(() => {
          navigation.navigate('DamagePage1')
        }, 3000);
      }}>
        {
          image ?
            <Image style={{ alignContent: 'center', justifyContent: 'center', width: 100, height: 100, marginTop: 50, marginLeft: 130 }} source={require("../assets/camera2.webp")}></Image> :
            <ActivityIndicator style={{ alignContent: 'center', justifyContent: 'center', width: 100, height: 100, marginTop: 50, marginLeft: 130 }} size="large" />
        }
      </TouchableOpacity>
    </View>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingLeft: 30,
    paddingTop: 10
  },
  camera: {
    width: 300,
    height: 300
  },
  cameratext: {
    fontSize: 20
  },
  buttonContainer: {

  },
  button: {
    backgroundColor: '#ffffff',
  }
});
export default Start;