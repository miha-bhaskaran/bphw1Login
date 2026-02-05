import React from "react";
import styles from "../styles/Header.module.css";
import profilePic from "../images/profile.jpg"; // Add your picture here

const Header = () => (
  <header className={styles.header}>
    <img src={profilePic} alt="Miha Bhaskaran" className={styles.profilePic} />
    <h1>Miha Bhaskaran</h1>
    <p className={styles.blurb}>
      I'm a Deep Learning Enthusiast passionate about building projects that combine AI and creativity.
    </p>
  </header>
);

export default Header;
