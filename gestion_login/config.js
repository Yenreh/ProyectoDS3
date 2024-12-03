import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getAnalytics, isSupported } from "firebase/analytics";

// Your Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAe41RA1BsCJJVzxRaO3ETpLy-Y3TPF6Rs",
  authDomain: "authentication-e2734.firebaseapp.com",
  projectId: "authentication-e2734",
  storageBucket: "authentication-e2734.firebasestorage.app",
  messagingSenderId: "308380406168",
  appId: "1:308380406168:web:917fd97df66a7e2b29dbed",
  measurementId: "G-TN7BZB14R3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase Auth
export const auth = getAuth(app);

// Declare analytics here first
let analytics;

// Only initialize Firebase Analytics if running in a browser environment
if (typeof window !== "undefined") {
  // Check if Firebase Analytics is supported
  isSupported().then((supported) => {
    if (supported) {
      analytics = getAnalytics(app);  // Assign to analytics if supported
    } else {
      console.log("Firebase Analytics is not supported in this environment.");
    }
  });
} else {
  console.log("Not in a browser environment, Firebase Analytics will not be initialized.");
}

// Export analytics outside the conditional block
export { analytics };
