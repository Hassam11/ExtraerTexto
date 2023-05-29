// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {getStorage, ref, uploadBytes, getDownloadURL} from "firebase/storage"
import { v4 } from "uuid";


// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyANcygVKrh2xLlyAIDe3s1DL3uZjbr1Mvw",
  authDomain: "guardarimagenes-fa954.firebaseapp.com",
  projectId: "guardarimagenes-fa954",
  storageBucket: "guardarimagenes-fa954.appspot.com",
  messagingSenderId: "877929087283",
  appId: "1:877929087283:web:3472cdaf7d6d27bb15fe46"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const storage = getStorage(app)


export async function uploadFile(file){
    const storageRef = ref(storage, v4())
    await uploadBytes(storageRef, file)
    const url = await getDownloadURL(storageRef)
    return url
}

