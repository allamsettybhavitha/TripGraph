# TripGraph – Graph-Based Travel Recommendation System

## 📌 Project Overview

TripGraph is a web-based travel recommendation system that recommends travel destinations based on the user's selected interests.

The system uses a graph database to connect destinations with their interests and activities. Users can select one or more interests such as Beach, Adventure, Nature, Mountains, Food, History, Culture and Relaxation.

TripGraph analyzes the relationships in the graph and displays destinations that match the user's interests.

---

## 🎯 Problem Statement

Choosing a travel destination based on multiple personal interests can be difficult.

Traditional travel websites may provide large amounts of information, but users still need to manually compare destinations.

TripGraph solves this problem by allowing users to select their interests and automatically finding destinations that match those preferences.

---

## 💡 Solution

TripGraph represents travel information as a graph.

Each destination is connected to:

- The interests it satisfies
- The activities it offers

When a user selects interests, the system searches the graph and calculates how many of those interests match each destination.

The destinations are displayed along with:

- Match score
- Matched interests
- Location
- Estimated budget
- Description
- Activities

---

## 🛠️ Technologies Used

- Python
- Flask
- Neo4j / CognoDB
- Cypher Query Language
- HTML5
- CSS3
- Jinja2
- python-dotenv

---

## 🧩 System Architecture

```text
User
  ↓
Flask Web Application
  ↓
Python Recommendation Logic
  ↓
Neo4j / CognoDB
  ↓
Cypher Query
  ↓
Destination Recommendations
  ↓
HTML Recommendation Cards