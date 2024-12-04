import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyAe41RA1BsCJJVzxRaO3ETpLy-Y3TPF6Rs",
  authDomain: "authentication-e2734.firebaseapp.com",
  projectId: "authentication-e2734",
  storageBucket: "authentication-e2734.firebasestorage.app",
  messagingSenderId: "308380406168",
  appId: "1:308380406168:web:917fd97df66a7e2b29dbed",
  measurementId: "G-TN7BZB14R3"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const analytics = getAnalytics(app);