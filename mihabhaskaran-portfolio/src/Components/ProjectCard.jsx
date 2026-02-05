import React from "react";
import styles from "../styles/ProjectCard.module.css";

const ProjectCard = ({ title, description, link }) => (
  <div className={styles.project}>
    <h3>{title}</h3>
    <p>{description}</p>
    {link && <a href={link}>View Project</a>}
  </div>
);

export default ProjectCard;
