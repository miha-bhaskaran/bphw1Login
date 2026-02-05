import React from "react";
import ProjectCard from "./ProjectCard";
import styles from "../styles/Projects.module.css";

const projectData = [
  {
    title: "Project 1",
    description: "Brief description of project 1.",
    link: "#",
  },
  {
    title: "Project 2",
    description: "Brief description of project 2.",
    link: "#",
  },
  // Add more projects here
];

const Projects = () => (
  <section id="projects" className={styles.projects}>
    <h2>Projects</h2>
    {projectData.map((project, idx) => (
      <ProjectCard key={idx} {...project} />
    ))}
  </section>
);

export default Projects;
