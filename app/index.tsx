

import { StyleSheet, Text, View } from "react-native";

export default function Index() {
  return (
 
      <View style={styles.container}>
        <Text style={styles.layout}>Hello, World!</Text>
        
      </View>

  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  layout: {
    marginBottom: 20,
  },
  button:{
    margin: 10,
    width: 100,
    
  }
});
