
# Library Book Recommendation System
# Using Rule-Based Artificial Intelligence

books = [
    {
        "title": "Python Programming",
        "genre": "technology",
        "purpose": "study",
        "level": "beginner"
    },
    {
        "title": "A Brief History of Time",
        "genre": "science",
        "purpose": "knowledge",
        "level": "intermediate"
    },
    {
        "title": "Harry Potter",
        "genre": "fantasy",
        "purpose": "entertainment",
        "level": "beginner"
    },
    {
        "title": "Introduction to AI",
        "genre": "technology",
        "purpose": "study",
        "level": "intermediate"
    },
    {
        "title": "The Theory of Everything",
        "genre": "science",
        "purpose": "knowledge",
        "level": "beginner"
    }
]

print("===================================")
print(" LIBRARY BOOK RECOMMENDATION SYSTEM")
print("       Rule-Based AI Project")
print("===================================")

# Get user preferences
genre = input(
    "Enter preferred genre (science/technology/fantasy): "
).lower()

purpose = input(
    "Enter purpose (study/knowledge/entertainment): "
).lower()

level = input(
    "Enter reading level (beginner/intermediate): "
).lower()

# Apply rules and calculate scores
recommendations = []

for book in books:
    score = 0
    reasons = []

    # Rule 1: Genre matching
    if book["genre"] == genre:
        score += 2
        reasons.append("Genre matches")

    # Rule 2: Purpose matching
    if book["purpose"] == purpose:
        score += 2
        reasons.append("Purpose matches")

    # Rule 3: Reading level matching
    if book["level"] == level:
        score += 1
        reasons.append("Reading level matches")

    if score > 0:
        recommendations.append(
            (book["title"], score, reasons)
        )

# Sort books by score, highest first
recommendations.sort(
    key=lambda item: item[1],
    reverse=True
)

# Display recommendations
print("\n--- Recommended Books ---")

if recommendations:
    for title, score, reasons in recommendations:
        print("\nBook:", title)
        print("Match Score:", score, "/ 5")
        print("Reason:", ", ".join(reasons))
else:
    print("No matching books found.")
    print("Try changing your preferences.")

print("\nThank you for using our system!")
