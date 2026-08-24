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


# ---------------------------------------------------------
# Main recommendation query
# ---------------------------------------------------------

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
                   COLLECT(DISTINCT a.name) AS activities

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


# ---------------------------------------------------------
# Multi-hop graph query
# Finds destinations that share interests with a destination
# ---------------------------------------------------------

def find_similar_destinations(destination_name):

    with driver.session() as session:

        result = session.run(
            """
            MATCH (d:Destination {name: $destination_name})
                  -[:HAS_INTEREST]->(i:Interest)
                  <-[:HAS_INTEREST]-(similar:Destination)

            WHERE d <> similar

            RETURN similar.name AS destination,
                   COLLECT(DISTINCT i.name) AS shared_interests

            ORDER BY SIZE(shared_interests) DESC, destination
            """,
            destination_name=destination_name
        )

        similar_destinations = []

        for record in result:

            similar_destinations.append({
                "destination": record["destination"],
                "shared_interests": record["shared_interests"]
            })

        return similar_destinations


# ---------------------------------------------------------
# Test the recommendation query
# ---------------------------------------------------------

if __name__ == "__main__":

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

        print("\nSimilar destinations to Goa:\n")

        similar_destinations = find_similar_destinations("Goa")

        for destination in similar_destinations:

            print(
                destination["destination"],
                "| Shared interests:",
                ", ".join(destination["shared_interests"])
            )

    finally:

        driver.close()