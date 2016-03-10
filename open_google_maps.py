from cStringIO import StringIO
from PIL import Image
import urllib

url = "http://maps.googleapis.com/maps/api/staticmap?center=-30.027489,-51.229248&size=800x800&zoom=14&sensor=false"
buffer = StringIO(urllib.urlopen(url).read())
maps = Image.open(buffer)
maps.show()

