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
    """A function that access the traveler's destination and returns the destination
    index from the data"""
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index


# Create list of attractins for - Visiting Interesting Places feature
attractions = [[] for destination in destinations]


def add_attraction(destination, attraction):
    """A function that adds attraction to the attractions list based 
    on the chosen destination"""
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
    except SyntaxError:
        return


add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

