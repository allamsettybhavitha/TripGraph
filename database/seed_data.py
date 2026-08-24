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


def seed_database(session):

    # Clear existing database
    session.run("""
        MATCH (n)
        DETACH DELETE n
    """)

    # Create destinations, interests and activities
    session.run("""
        CREATE

        // =========================
        // DESTINATIONS
        // =========================

        (andaman:Destination {
            name: "Andaman",
            location: "Andaman and Nicobar Islands",
            budget: "₹10,000 - ₹18,000",
            description: "A tropical island destination known for beaches, water activities and marine adventures."
        }),

        (goa:Destination {
            name: "Goa",
            location: "Goa",
            budget: "₹6,000 - ₹12,000",
            description: "A popular coastal destination offering beaches, adventure activities and vibrant experiences."
        }),

        (vizag:Destination {
            name: "Vizag",
            location: "Andhra Pradesh",
            budget: "₹4,000 - ₹8,000",
            description: "A beautiful coastal city known for beaches, nature and water activities."
        }),

        (manali:Destination {
            name: "Manali",
            location: "Himachal Pradesh",
            budget: "₹8,000 - ₹15,000",
            description: "A mountain destination popular for trekking, camping and scenic natural beauty."
        }),

        (jaipur:Destination {
            name: "Jaipur",
            location: "Rajasthan",
            budget: "₹5,000 - ₹10,000",
            description: "The Pink City famous for forts, palaces, history and rich Rajasthani culture."
        }),

        (kerala:Destination {
            name: "Kerala",
            location: "Kerala",
            budget: "₹7,000 - ₹14,000",
            description: "A peaceful destination known for backwaters, greenery, sightseeing and relaxation."
        }),

        (pondicherry:Destination {
            name: "Pondicherry",
            location: "Puducherry",
            budget: "₹5,000 - ₹10,000",
            description: "A charming coastal destination combining beaches, culture, cafes and relaxing experiences."
        }),

        (ooty:Destination {
            name: "Ooty",
            location: "Tamil Nadu",
            budget: "₹5,000 - ₹10,000",
            description: "A scenic hill station known for mountains, gardens, lakes and pleasant weather."
        }),

        (munnar:Destination {
            name: "Munnar",
            location: "Kerala",
            budget: "₹6,000 - ₹12,000",
            description: "A beautiful hill destination surrounded by tea plantations, mountains and greenery."
        }),

        (rishikesh:Destination {
            name: "Rishikesh",
            location: "Uttarakhand",
            budget: "₹6,000 - ₹12,000",
            description: "An adventure destination famous for rafting, trekking, camping and natural beauty."
        }),

        (agra:Destination {
            name: "Agra",
            location: "Uttar Pradesh",
            budget: "₹4,000 - ₹8,000",
            description: "A historic city famous for the Taj Mahal, Mughal architecture and cultural heritage."
        }),

        (mysore:Destination {
            name: "Mysore",
            location: "Karnataka",
            budget: "₹5,000 - ₹9,000",
            description: "A cultural destination known for palaces, heritage, art and traditional experiences."
        }),

        (coorg:Destination {
            name: "Coorg",
            location: "Karnataka",
            budget: "₹6,000 - ₹12,000",
            description: "A peaceful hill destination famous for coffee plantations, forests and scenic landscapes."
        }),

        (hyderabad:Destination {
            name: "Hyderabad",
            location: "Telangana",
            budget: "₹4,000 - ₹9,000",
            description: "A vibrant city famous for historic monuments, culture and delicious local cuisine."
        }),

        (delhi:Destination {
            name: "Delhi",
            location: "Delhi",
            budget: "₹5,000 - ₹10,000",
            description: "A diverse destination offering historic landmarks, cultural attractions and famous food."
        }),

        (lucknow:Destination {
            name: "Lucknow",
            location: "Uttar Pradesh",
            budget: "₹4,000 - ₹8,000",
            description: "A cultural city known for heritage, traditional cuisine and historic architecture."
        }),


        // =========================
        // INTERESTS
        // =========================

        (beach:Interest {name: "Beach"}),
        (adventure:Interest {name: "Adventure"}),
        (nature:Interest {name: "Nature"}),
        (mountains:Interest {name: "Mountains"}),
        (food:Interest {name: "Food"}),
        (history:Interest {name: "History"}),
        (culture:Interest {name: "Culture"}),
        (relaxation:Interest {name: "Relaxation"}),


        // =========================
        // ACTIVITIES
        // =========================

        (scuba:Activity {name: "Scuba Diving"}),
        (snorkeling:Activity {name: "Snorkeling"}),
        (watersports:Activity {name: "Water Sports"}),
        (trekking:Activity {name: "Trekking"}),
        (sightseeing:Activity {name: "Sightseeing"}),
        (camping:Activity {name: "Camping"}),
        (forts:Activity {name: "Fort Visits"}),
        (boating:Activity {name: "Boating"}),
        (beachwalk:Activity {name: "Beach Walks"}),
        (cafes:Activity {name: "Cafe Hopping"}),
        (tea:Activity {name: "Tea Plantation Visits"}),
        (rafting:Activity {name: "River Rafting"}),
        (temples:Activity {name: "Temple Visits"}),
        (palace:Activity {name: "Palace Visits"}),
        (foodtour:Activity {name: "Food Tours"}),
        (streetfood:Activity {name: "Street Food"}),
        (museums:Activity {name: "Museum Visits"}),
        (heritage:Activity {name: "Heritage Walks"}),
        (naturewalk:Activity {name: "Nature Walks"}),
        (gardens:Activity {name: "Garden Visits"}),


        // =========================
        // DESTINATION -> INTERESTS
        // =========================

        // Andaman
        (andaman)-[:HAS_INTEREST]->(beach),
        (andaman)-[:HAS_INTEREST]->(adventure),
        (andaman)-[:HAS_INTEREST]->(relaxation),

        // Goa
        (goa)-[:HAS_INTEREST]->(beach),
        (goa)-[:HAS_INTEREST]->(adventure),
        (goa)-[:HAS_INTEREST]->(relaxation),

        // Vizag
        (vizag)-[:HAS_INTEREST]->(beach),
        (vizag)-[:HAS_INTEREST]->(nature),

        // Manali
        (manali)-[:HAS_INTEREST]->(adventure),
        (manali)-[:HAS_INTEREST]->(nature),
        (manali)-[:HAS_INTEREST]->(mountains),

        // Jaipur
        (jaipur)-[:HAS_INTEREST]->(history),
        (jaipur)-[:HAS_INTEREST]->(culture),

        // Kerala
        (kerala)-[:HAS_INTEREST]->(nature),
        (kerala)-[:HAS_INTEREST]->(relaxation),

        // Pondicherry
        (pondicherry)-[:HAS_INTEREST]->(beach),
        (pondicherry)-[:HAS_INTEREST]->(culture),
        (pondicherry)-[:HAS_INTEREST]->(relaxation),

        // Ooty
        (ooty)-[:HAS_INTEREST]->(nature),
        (ooty)-[:HAS_INTEREST]->(mountains),
        (ooty)-[:HAS_INTEREST]->(relaxation),

        // Munnar
        (munnar)-[:HAS_INTEREST]->(nature),
        (munnar)-[:HAS_INTEREST]->(mountains),
        (munnar)-[:HAS_INTEREST]->(relaxation),

        // Rishikesh
        (rishikesh)-[:HAS_INTEREST]->(adventure),
        (rishikesh)-[:HAS_INTEREST]->(nature),
        (rishikesh)-[:HAS_INTEREST]->(mountains),

        // Agra
        (agra)-[:HAS_INTEREST]->(history),
        (agra)-[:HAS_INTEREST]->(culture),

        // Mysore
        (mysore)-[:HAS_INTEREST]->(history),
        (mysore)-[:HAS_INTEREST]->(culture),

        // Coorg
        (coorg)-[:HAS_INTEREST]->(nature),
        (coorg)-[:HAS_INTEREST]->(mountains),
        (coorg)-[:HAS_INTEREST]->(relaxation),

        // Hyderabad
        (hyderabad)-[:HAS_INTEREST]->(food),
        (hyderabad)-[:HAS_INTEREST]->(history),
        (hyderabad)-[:HAS_INTEREST]->(culture),

        // Delhi
        (delhi)-[:HAS_INTEREST]->(food),
        (delhi)-[:HAS_INTEREST]->(history),
        (delhi)-[:HAS_INTEREST]->(culture),

        // Lucknow
        (lucknow)-[:HAS_INTEREST]->(food),
        (lucknow)-[:HAS_INTEREST]->(history),
        (lucknow)-[:HAS_INTEREST]->(culture),


        // =========================
        // DESTINATION -> ACTIVITIES
        // =========================

        // Andaman
        (andaman)-[:OFFERS]->(scuba),
        (andaman)-[:OFFERS]->(snorkeling),
        (andaman)-[:OFFERS]->(watersports),

        // Goa
        (goa)-[:OFFERS]->(scuba),
        (goa)-[:OFFERS]->(watersports),
        (goa)-[:OFFERS]->(beachwalk),
        (goa)-[:OFFERS]->(cafes),

        // Vizag
        (vizag)-[:OFFERS]->(watersports),
        (vizag)-[:OFFERS]->(beachwalk),
        (vizag)-[:OFFERS]->(naturewalk),

        // Manali
        (manali)-[:OFFERS]->(trekking),
        (manali)-[:OFFERS]->(camping),
        (manali)-[:OFFERS]->(naturewalk),

        // Jaipur
        (jaipur)-[:OFFERS]->(forts),
        (jaipur)-[:OFFERS]->(sightseeing),
        (jaipur)-[:OFFERS]->(heritage),

        // Kerala
        (kerala)-[:OFFERS]->(boating),
        (kerala)-[:OFFERS]->(sightseeing),
        (kerala)-[:OFFERS]->(naturewalk),

        // Pondicherry
        (pondicherry)-[:OFFERS]->(beachwalk),
        (pondicherry)-[:OFFERS]->(cafes),
        (pondicherry)-[:OFFERS]->(sightseeing),

        // Ooty
        (ooty)-[:OFFERS]->(sightseeing),
        (ooty)-[:OFFERS]->(naturewalk),
        (ooty)-[:OFFERS]->(gardens),

        // Munnar
        (munnar)-[:OFFERS]->(tea),
        (munnar)-[:OFFERS]->(trekking),
        (munnar)-[:OFFERS]->(naturewalk),

        // Rishikesh
        (rishikesh)-[:OFFERS]->(rafting),
        (rishikesh)-[:OFFERS]->(trekking),
        (rishikesh)-[:OFFERS]->(camping),

        // Agra
        (agra)-[:OFFERS]->(sightseeing),
        (agra)-[:OFFERS]->(heritage),
        (agra)-[:OFFERS]->(museums),

        // Mysore
        (mysore)-[:OFFERS]->(palace),
        (mysore)-[:OFFERS]->(sightseeing),
        (mysore)-[:OFFERS]->(heritage),

        // Coorg
        (coorg)-[:OFFERS]->(naturewalk),
        (coorg)-[:OFFERS]->(sightseeing),
        (coorg)-[:OFFERS]->(camping),

        // Hyderabad
        (hyderabad)-[:OFFERS]->(foodtour),
        (hyderabad)-[:OFFERS]->(streetfood),
        (hyderabad)-[:OFFERS]->(heritage),

        // Delhi
        (delhi)-[:OFFERS]->(foodtour),
        (delhi)-[:OFFERS]->(streetfood),
        (delhi)-[:OFFERS]->(museums),
        (delhi)-[:OFFERS]->(heritage),

        // Lucknow
        (lucknow)-[:OFFERS]->(foodtour),
        (lucknow)-[:OFFERS]->(streetfood),
        (lucknow)-[:OFFERS]->(heritage)
    """)


try:

    driver.verify_connectivity()

    with driver.session() as session:
        seed_database(session)

    print("TripGraph database seeded successfully!")

finally:

    driver.close()