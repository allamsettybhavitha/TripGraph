from flask import Flask, render_template, request
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Neo4j connection
uri = os.getenv("COGNODB_URI")
username = os.getenv("COGNODB_USERNAME")
password = os.getenv("COGNODB_PASSWORD")

driver = GraphDatabase.driver(
    uri,
    auth=(username, password)
)


def recommend_destinations(interests):

    with driver.session() as session:

        result = session.run(
            """
            MATCH (d:Destination)-[:HAS_INTEREST]->(i:Interest)
            WHERE i.name IN $interests

            WITH d,
                 COUNT(DISTINCT i) AS matched_interests,
                 COLLECT(DISTINCT i.name) AS matched_names

            WHERE matched_interests > 0

            MATCH (d)-[:OFFERS]->(a:Activity)

            WITH d,
                 matched_interests,
                 matched_names,
                 COLLECT(DISTINCT a.name) AS activities

            RETURN d.name AS destination,
                   matched_interests,
                   matched_names,
                   activities,
                   d.location AS location,
                   d.budget AS budget,
                   d.description AS description

            ORDER BY matched_interests DESC, destination
            """,
            interests=interests
        )

        recommendations = []

        for record in result:

            recommendations.append({
                "name": record["destination"],
                "matches": record["matched_interests"],
                "matched_names": record["matched_names"],
                "activities": record["activities"],
                "location": record["location"],
                "budget": record["budget"],
                "description": record["description"]
            })

        return recommendations


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    interests = []

    if request.method == "POST":

        interests = request.form.getlist("interests")

        if interests:

            recommendations = recommend_destinations(interests)

            for recommendation in recommendations:

                recommendation["total_interests"] = len(interests)

    return render_template(
        "index.html",
        recommendations=recommendations,
        selected_interests=interests
    )


if __name__ == "__main__":

    try:

        driver.verify_connectivity()

        print("Successfully connected to CognoDB!")
        print("TripGraph connection successful!")

        app.run(debug=True)

    finally:

        driver.close()