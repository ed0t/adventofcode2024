Goal
Demonstrate technical comprehension and fluency through an API integration exercise

Prompt
You’re planning a whirlwind tour of London for some out-of-town relatives, and they don’t have an extra moment to spare, which is why you’re going to take them on the optimal route around London’s most famous sights. That’s right – you’re going to solve the travelling salesman problem by brute force. But before you can choose the optimal route between all the sights in your itinerary, you’ll need to know how far apart they are. Fortunately, you can use the Mapbox API to compute travel times between each sight.

To authenticate to the API, you’ll need to authenticate with an access token. See documentation here:

https://docs.mapbox.com/api/overview/#access-tokens-and-token-scopes

You can use this access token:
pk.eyJ1IjoicmxhZGJyb29rIiwiYSI6ImNsb2lkdmYwcDFsdDIyanFwbDVieTNubzIifQ.zqb6pKBuEgO8RGWpM7Cdiw


Step 1: Matrix generation
At the bottom of this document, you are provided with the list of the sights and their longitude/latitude. With this, we can compute a matrix of the travel times between each point using the Mapbox Matrix API:

https://docs.mapbox.com/api/navigation/matrix/#retrieve-a-matrix

We can use the “mapbox/driving” profile to keep things consistent, so that traffic is not a factor.

Step 2: The perfect route
Now that we have a matrix of the durations between all of our sights, let’s generate every possible route visiting each sight just once, and find the route with the shortest total travel time. Return the optimal order of stops and the total time taken for the route.

Hint: itertools.permutations in Python, Stackoverflow for generating permutations

Step 3: Choose your destination
Plans often change, so we want a quick way to search for our next sight to visit. Write a function that takes a search string and the sight you're currently at, and returns the most relevant matches from the sights list (use the matrix to ensure closest sights first). The whole family will want to search for destinations, so make sure it's robust!

Step 3b (stretch goal): Explore the whole of the UK
We want all 31m UK addresses to be available to our search function. How can you optimise your function for this?


Sights
[
  ["Tower of London", "London", "EC3N 4AB"],
  ["Buckingham Palace", "London",  "SW1A 1AA"],
  ["London Eye", "Riverside Building", "County Hall", "London", "SE1 7PB"],
  ["St. Paul's Churchyard", "London", "EC4M 8AD"],
  ["Palace of Westminster", "London", "SW1A 0AA"],
  ["10 Downing St", "London", "SW1A 2AA"],
  ["The British Museum", "Great Russell St", "London", "WC1B 3DG"]
]

Sight coordinates
[
  [-0.0760706875, 51.508094], 
  [-0.1425615, 51.500978], 
  [-0.1188555, 51.5020205], 
  [-0.0979295, 51.513379], 
  [-0.124592, 51.50068575], 
  [-0.12767, 51.50354], 
  [-0.12726, 51.51801]
]
