destinations = [
    "Paris, France",
    "Shanghai China",
    "Los Angeles, Usa",
    "Sao Paulo, Brazil",
    "Cairo, Egypt",
]

# Define a test traveler to check the functionality
# test_traveler is the user of the app
test_traveler = ["Erin Wilkes", "Shanghai China", ["historical site", "art"]]


def get_destination_index(destination):
    """A function that identifies each location based on index and 
    returns it's index from the list"""
    destination_index = destinations.index(destination)

    return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    
    return traveler_destination_index

