import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

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

            MATCH (d)-[:OFFERS]->(a:Activity)

            RETURN d.name AS destination,
                   matched_interests,
                   matched_names,
                   d.location AS location,
                   d.budget AS budget,
                   d.description AS description,
                   collect(a.name) AS activities

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
                "location": record["location"],
                "budget": record["budget"],
                "description": record["description"],
                "activities": record["activities"]
            })

        return recommendations


try:

    print("Recommendations for Beach + Adventure:\n")

    recommendations = recommend_destinations(
        ["Beach", "Adventure"]
    )

    for recommendation in recommendations:

        print(
            recommendation["name"],
            "| Matches:",
            recommendation["matches"],
            "| Matched:",
            ", ".join(recommendation["matched_names"]),
            "| Location:",
            recommendation["location"],
            "| Budget:",
            recommendation["budget"],
            "| Activities:",
            ", ".join(recommendation["activities"])
        )

finally:

    driver.close()