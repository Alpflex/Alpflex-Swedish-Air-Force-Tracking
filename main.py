from myimport import *

auth = tweepy.OAuthHandler("api", "api")
auth.set_access_token("api", "api")


# Create API object
apiTwitter = tweepy.API(auth)

# Verify geopy, Nominatim
geolocator = Nominatim(user_agent="plane-app")

# Verify twitter Authentication
try:
    apiTwitter.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")




def main():
    limit = 1
    for follower in tweepy.Cursor(apiTwitter.search_tweets, q="svfm").items(limit):
        apiTwitter.create_friendship(screen_name=follower.author.screen_name)
        print(follower)

    a = 1
    # While loop, always runs
    while a < 2:

        a += 1
        Search()


def Search():
    # tandom = random.randint(3600, 7200)
    # print(tandom)
    time.sleep(3)



    # OpenSkyApi credentials
    api = OpenSkyApi("api", "api")
    states = api.get_states()
         #for loop, using icao24 to find airplane

    for s in states.states:

        if "SVF" in s.callsign[0:5] and s.origin_country == "Sweden":

            callsign  = s.callsign
            icao24 = s.icao24
            longitude = s.longitude
            latitude = s.latitude
            origin_country = s.origin_country

            # converting int or float to string
            var0 = "Callsign: " + callsign
            var1 = 'Icao24: ' + icao24
            var2 = "Longitude: " + str(longitude)
            var4 = "Latitude: " + str(latitude)
            var5 = "Country: " + origin_country

            list = (latitude, longitude)

            location = geolocator.reverse(list)

            # converting to string
            text = var0, "\n" + var1, "\n" + var5, "\n" + var2, "\n" + var4, "\n" + location.address, "\n" "#svfm #swaf #flygvapnet #sweden"
            str1 = functools.reduce(operator.add, (text))

            print(str1)
            print(location.address)
            """
            # create a map object with a desired initial map center and initial map zoom
            m = folium.Map(location=[latitude, longitude],
                           zoom_start=13)
    
            # save the map as html
            mapFname = 'output.html'
            m.save(mapFname)

            mapUrl = 'file://{0}/{1}'.format(os.getcwd(), mapFname)

            # download gecko driver for firefox from here - https://github.com/mozilla/geckodriver/releases

            # use selenium to save the html as png image
            driver = webdriver.Firefox()
            driver.get(mapUrl)
            # wait for 5 seconds for the maps and other assets to be loaded in the browser
            time.sleep(5)
            driver.save_screenshot('output.png')
            driver.quit()
            """
            # Posting result on twitter
            #media = apiTwitter.media_upload("output.png")
            #apiTwitter.update_status(str1, media_ids=[media.media_id])


            apiTwitter.update_status(str1)

            time.sleep(5)



main()




"""
f = open("text.txt", "r")

var = f.readline().rstrip()
var2 = f.readline().rstrip()

print(var)
print(var2)




with open('text.txt', 'r') as file:
    data = file.read().rstrip()

    #print(data)


#content = f.readlines()
#print(content[2])
#content2 = content[2]
#print(content2)
#print(f.readline())
#f.close()
#print(content2)






"""







