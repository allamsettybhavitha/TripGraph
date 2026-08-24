# TripGraph – Graph-Based Travel Recommendation System

## 📌 Project Overview

TripGraph is a web-based travel recommendation system that recommends travel destinations based on the user's selected interests.

The system uses a graph database to connect destinations with their interests and activities. Users can select one or more interests such as Beach, Adventure, Nature, Mountains, Food, History, Culture and Relaxation.

TripGraph analyzes the relationships in the graph and displays destinations that best match the user's interests.

---

## 🎯 Problem Statement

Choosing a travel destination based on multiple personal interests can be difficult.

Traditional travel websites provide a large amount of information, but users still need to manually compare destinations based on their preferences.

TripGraph solves this problem by allowing users to select one or more interests and automatically recommending destinations using graph relationships.

---

## 💡 Solution

TripGraph represents travel information as a graph database.

Each destination is connected to:

- Interests it satisfies
- Activities it offers

When a user selects interests, the application searches the graph and finds destinations connected to those interests.

The system displays:

- Match score
- Matched interests
- Location
- Estimated budget
- Destination description
- Available activities

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
   │
   ▼
Flask Web Application
   │
   ▼
Python Recommendation Logic
   │
   ▼
Neo4j / CognoDB
   │
   ▼
Cypher Query
   │
   ▼
Destination Recommendations
   │
   ▼
HTML Recommendation Cards
```

---

## 🗄️ Graph Database Model

TripGraph uses three main node types:

- Destination
- Interest
- Activity

### Relationships

```text
Destination ──HAS_INTEREST──> Interest

Destination ─────OFFERS─────> Activity
```

### Example Graph

```text
                    Beach
                      ▲
                      │
                HAS_INTEREST
                      │
Adventure ◄── Andaman ──► Relaxation
                      │
                  OFFERS
          ┌───────────┼────────────┐
          │           │            │
      Scuba Diving  Snorkeling  Water Sports
```

This graph directly represents the relationships between destinations, interests and activities.

---

## 🧠 Why a Graph Database?

TripGraph is built around relationships rather than isolated data.

The main purpose of the application is to discover connections between destinations, user interests and travel activities. A graph database is suitable because these relationships are stored directly as connections between nodes.

For example, every destination can be connected to multiple interests and multiple activities:

```text
Goa ──HAS_INTEREST──> Beach

Goa ──HAS_INTEREST──> Adventure

Goa ─────OFFERS─────> Scuba Diving

Goa ─────OFFERS─────> Water Sports
```

Instead of searching through multiple relational tables, Neo4j/CognoDB allows the application to traverse connected nodes and relationships directly.

### Multi-Hop Traversal

TripGraph also performs a multi-hop graph traversal to find destinations that share common interests.

The traversal pattern is:

```text
Destination
      │
      ▼
HAS_INTEREST
      │
      ▼
Interest
      ▲
      │
HAS_INTEREST
      │
      │
Destination
```

For example, when searching for destinations similar to Goa:

```text
Goa
 │
 ├── Beach ───────► Andaman
 │               ► Pondicherry
 │               ► Vizag
 │
 ├── Adventure ───► Manali
 │               ► Rishikesh
 │               ► Andaman
 │
 └── Relaxation ──► Kerala
                 ► Coorg
                 ► Ooty
                 ► Munnar
```

This is a 2-hop traversal:

```text
Goa → Interest ← Similar Destination
```

The application uses this graph traversal to identify destinations connected through shared interests.

### Why Not a Relational Database?

A relational database could store destinations, interests and activities in separate tables and connect them using foreign keys.

However, relationship-focused queries require repeated JOIN operations when exploring connected data.

In TripGraph, the graph database makes it easier to represent and query relationships because destinations are directly connected to interests and activities.

Therefore, a graph database is a natural fit for this recommendation system.

---

## ⚙️ Recommendation Logic

The user selects one or more travel interests.

Example:

```text
Beach
Adventure
Nature
```

The application executes a parameterized Cypher query to find destinations connected to those interests.

For every destination, the system:

1. Matches the selected interests.
2. Counts the matched interests.
3. Collects the matched interest names.
4. Retrieves destination activities.
5. Retrieves location, budget and description.
6. Sorts destinations by the number of matched interests.

### Match Score Formula

```text
Match Score =
Matched Interests / Selected Interests × 100
```

### Example

User selects:

```text
Beach
Adventure
Nature
```

Andaman matches:

```text
Beach
Adventure
```

Therefore:

```text
2 / 3 × 100 = 67%
```

The application displays:

```text
2/3 Match

Match Score: 67%

Matched Interests:
Beach, Adventure
```

If a destination matches all selected interests, it is displayed as:

```text
🏆 Best Match
```

---

## ✨ Features

- Select one or multiple travel interests
- Graph-based destination recommendations
- Parameterized Cypher queries
- Match score calculation
- Best Match identification
- Matched interests display
- Destination location
- Estimated budget
- Destination description
- Activity recommendations
- Multi-hop destination similarity query
- Responsive user interface
- Flask and Neo4j/CognoDB integration

---

## 📊 Example Recommendations

### Beach

```text
Andaman
Goa
Pondicherry
Vizag
```

### Food

```text
Delhi
Hyderabad
Lucknow
```

### Nature

```text
Coorg
Kerala
Manali
Munnar
Ooty
Rishikesh
Vizag
```

### Beach + Adventure

```text
Andaman   2/2
Goa       2/2
Manali    1/2
Rishikesh 1/2
Vizag     1/2
```

### Beach + Adventure + Nature

```text
Andaman       2/3
Goa           2/3
Manali        2/3
Rishikesh     2/3
Vizag         2/3
Coorg         1/3
Kerala        1/3
Munnar        1/3
Ooty          1/3
Pondicherry   1/3
```

Results are ordered according to the number of matched interests.

---

## 📁 Project Structure

```text
TripGraph/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   ├── seed_data.py
│   └── queries.py
│
└── templates/
    └── index.html
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/allamsettybhavitha/TripGraph.git
cd TripGraph
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

```text
COGNODB_URI=your_database_uri
COGNODB_USERNAME=your_username
COGNODB_PASSWORD=your_password
```

**Do not upload or commit the `.env` file.**

### 5. Seed the database

```bash
python database/seed_data.py
```

Expected output:

```text
TripGraph database seeded successfully!
```

### 6. Run the Flask application

```bash
python app.py
```

### 7. Open the application

```text
http://127.0.0.1:5000
```

---

## 🔍 Testing

The graph recommendation query can be tested independently.

Run:

```bash
python database/queries.py
```

Example output:

```text
Recommendations for Beach + Adventure:

Andaman | Matches: 2 | Matched: Beach, Adventure
Goa | Matches: 2 | Matched: Beach, Adventure
Manali | Matches: 1 | Matched: Adventure
Pondicherry | Matches: 1 | Matched: Beach
Rishikesh | Matches: 1 | Matched: Adventure
Vizag | Matches: 1 | Matched: Beach
```

The multi-hop similarity query also returns destinations that share interests with Goa.

Example:

```text
Similar destinations to Goa:

Andaman | Shared interests: Beach, Adventure, Relaxation
Pondicherry | Shared interests: Beach, Relaxation
Coorg | Shared interests: Relaxation
Kerala | Shared interests: Relaxation
Manali | Shared interests: Adventure
Munnar | Shared interests: Relaxation
Ooty | Shared interests: Relaxation
Rishikesh | Shared interests: Adventure
Vizag | Shared interests: Beach
```

---

## 🔐 Security

Database credentials are stored in the `.env` file and are not included in the project repository.

The `.gitignore` file excludes sensitive and unnecessary files such as:

```text
.env
venv/
__pycache__/
*.pyc
```

Never commit database credentials, passwords or other sensitive information to GitHub.

---

## 👩‍💻 Author

**Bhavitha Allamsetty**

TripGraph – Graph-Based Travel Recommendation System

Built using Python, Flask and Neo4j/CognoDB.

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