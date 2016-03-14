from cStringIO import StringIO
from PIL import Image
import urllib

url = "https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap"
# url = "http://maps.googleapis.com/maps/api/staticmap?center=-30.027489,-51.229248&size=800x800&zoom=14&sensor=false"
buffer = StringIO(urllib.urlopen(url).read())
maps = Image.open(buffer)
maps.show()

# https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
# &markers=color:blue%7Clabel:S%7C40.702147,-74.015794
# &markers=color:green%7Clabel:G%7C40.711614,-74.012318
# &markers=color:red%7Clabel:C%7C40.718217,-73.998284
# &key=YOUR_API_KEY


