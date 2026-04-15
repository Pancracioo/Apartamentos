import { Image } from 'expo-image';
import { Platform, StyleSheet, View, Text} from 'react-native';

import { HelloWave } from '@/components/hello-wave';
import ParallaxScrollView from '@/components/parallax-scroll-view';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { ScrollView } from 'react-native-reanimated/lib/typescript/Animated';


export default function HomeScreen() {
  return (
    <SafeAreaView>
      <Text style={style.title}>Dashboard</Text>
      
    </SafeAreaView>
    
  );
}

 const style = StyleSheet.create({
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});
