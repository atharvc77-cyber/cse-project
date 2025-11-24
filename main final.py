# main.py
from waste_data import waste_categories, disposal_methods

print("=== Welcome to Waste Segregation & Recycle System ===\n")

# Ask user input
waste_item = input("Enter the waste item you want to dispose: ").strip()

# Function to identify category
def identify_category(item):
    for category, items in waste_categories.items():
        if item.lower() in [i.lower() for i in items]:
            return category
    return "Unknown"

# Identify category
category = identify_category(waste_item)

# Provide disposal advice
if category != "Unknown":
    print(f"\nThe item '{waste_item}' belongs to the category: {category}")
    print(f"Recommended disposal: {disposal_methods[category]}")
else:
    print(f"\nThe item '{waste_item}' is not recognized. Please check and dispose responsibly.")

# Optional: Track waste statistics
# Simple example (can be expanded to store history)
waste_stats = {key: 0 for key in waste_categories.keys()}
if category in waste_stats:
    waste_stats[category] += 1

print("\nCurrent waste statistics (example):")
for cat, count in waste_stats.items():
    print(f"{cat}: {count}")