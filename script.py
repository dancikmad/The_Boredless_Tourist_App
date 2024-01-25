destinations = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt",
]

# Define a test traveler to check the functionality
# test_traveler is the user of the app
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]


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
attractions = [[] for _ in destinations]


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
add_attraction(
    "Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]]
)
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# Feature: Finding the Best Places to Go
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    # Ommiting tags showing to the user
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest


# Feature: Connecting people with the attractions that they are interested in
def get_attractions_for_traveler(traveler):
    # Separate traveler's data
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    # Display a welcome message to the user when they open the application
    interest_string = (
        "Hi "
        + traveler[0]
        + ", we think you'll like thesse places around "
        + traveler_destination
        + ": "
    )

    '''If last attraction in list add a period, else add a comma plus a space'''
    for i in range(len(traveler_attractions)):
        '''Extra logic check to see if attraction we are on is the last one 
        < If it is format the interest_string differently '''
        if traveler_attractions[-1] == traveler_attractions[i]:
            interest_string += "the " + traveler_attractions[i] + "."
        else:
            interest_string += "the " + traveler_attractions[i] + ", "
            
    return interest_string