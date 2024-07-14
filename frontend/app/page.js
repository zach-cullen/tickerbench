"use client"

import styles from "./page.module.css";
import { useState } from "react";
// import { useRouter } from 'next/router';

export default function Home() {

  // Initialize state for form inputs
  const [formData, setFormData] = useState({
    message: '',
  });

  const [echo, setEcho] = useState({
    sound: '',  
  })

  // Handle input change
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent default form submission
    setEcho({sound: formData.message});
  };

  return (
    <main className={styles.main}>
      <form onSubmit={handleSubmit} >
        <input 
          type="text"
          id="message"
          name="message"
          value={formData.message}
          onChange={handleInputChange}
          placeholder="Say Something"
        />
        <button>
          Send It.
        </button>
      </form>
      <h1>{echo.sound}</h1>
    </main>
  );
}
