![Django](https://img.shields.io/badge/Django-3.2-green) ![SQL Server](https://img.shields.io/badge/SQL%20Server-2019-blue) ![HTML5](https://img.shields.io/badge/HTML5-orange) ![CSS3](https://img.shields.io/badge/CSS3-blue) ![JavaScript](https://img.shields.io/badge/JavaScript-yellow)
![pythonanywhere](https://www.pythonanywhere.com/)
# Go Cheap 🚗💸

Go Cheap is a web-based ride comparison platform designed to help users find the most affordable and suitable trip by comparing offers from multiple ride-hailing companies in one unified interface.

---

## 📌 Project Description

In today’s fast-paced world, users often need to open multiple ride-hailing applications to compare prices, trip durations, and available drivers. Go Cheap solves this problem by collecting and displaying trip details from different companies in a single platform.

The system allows users to register, log in, search for trips by selecting pickup and destination locations, and compare ride options from:

* Uber
* inDrive
* DiDi

Each option is presented clearly, enabling users to make an informed decision quickly and efficiently.

---

## 🔐 Authentication & Security

* Secure Login & Registration system
* Session-based authentication
* Logout functionality that safely redirects users back to the login page

### 🛡️ Backend Security

The backend is built using Django, which provides a high level of security by default, including:

* Built-in protection against SQL Injection
* Cross-Site Request Forgery (CSRF) protection
* Secure authentication and authorization mechanisms
* Safe handling of user credentials and sessions

---

## 🏠 Website Structure

The website is structured into the following main sections:

* Home: Introduction and overview of the platform
* Services: Core functionality for trip search and comparison
* About: Explanation of the project idea and objectives
* Contact: Communication section

---

## 🚕 Services – Trip Search & Comparison

Within the Services section, users can:

* Select a Pickup Location
* Select a Destination
* Click Search to retrieve available trip options

The system then displays available rides in a card-based layout for easy comparison.

---

## 🧾 Trip Card Information

Each trip card contains the following details:

* Company Logo
* Driver Name
* Trip Price
* Car Model
* Estimated Trip Duration
* Distance

### 🔗 Trip Selection

Each card includes a button that redirects the user to the official website link of the selected ride-hailing company, allowing the user to complete the booking process.

---

## 🗄️ Database & Data Management

* Microsoft SQL Server is used as the primary Database Management System
* Stores:

  * User accounts and authentication data
  * Trip-related data
  * User preferences and system records
* Integrated seamlessly with Django ORM for secure and efficient data handling

---

## 🧩 System Architecture & Technologies

### 🔹 Frontend Development

* HTML5 for structure
* CSS3 for styling
* JavaScript for interactivity
* Bootstrap for responsive and modern UI components

### 🔹 Backend Development

* Django Framework (Python)
* Django Authentication System
* Secure server-side logic and data validation

### 🔹 Database Layer

* Microsoft SQL Server
* Structured relational data storage

---

## 📘 User Manual

A complete User Manual has been created and uploaded as a PDF file named:

User Manual (PDF)

The document includes detailed usage instructions and screenshots explaining how users interact with the system.

---

## 🌐 Live Demo

You can access the live demo of the project here:

🔗 [https://kero-2005-samir.github.io/Go-cheap-project/](https://kero-2005-samir.github.io/Go-cheap-project/)

---

## 🚀 Future Enhancements

In future versions of Go Cheap, the following features can be added to improve the system:
* Real-time API integration with ride-hailing companies
* In-app trip booking without redirection
* Online payment support
* Price history and smart price comparison
* User ratings and reviews for drivers and companies
* Mobile application version (Android & iOS)
* Location detection using GPS
* AI-based recommendations for the cheapest and fastest trip

---

## 👥 Team Information

Team Name: NULL POINTERS

### Team Members & Roles

* Beshoy Karam – Team Leader & Backend Developer
* Kerolous Samir – Frontend Developer
* Ahd Montaser – Database Engineer
* Ahmed Altigany – UI/UX Designer
* Sherif Abd Almoaty – Software Tester

---

## 🎯 Project Objective

The primary objective of Go Cheap is to:

* Help users find the most cost-effective ride
* Eliminate the need to switch between multiple ride-hailing applications
* Provide a clean, secure, and user-friendly comparison experience
