from GeoMap import GeoMap

m = GeoMap()

m.add_marker("New Delhi", popup="Capital City")
m.add_marker("Mumbai")
m.add_circle("Hyderabad", radius=10000, color="green", popup="Cyber City")

icon_url = "https://cdn-icons-png.flaticon.com/512/684/684908.png"
m.add_custom_icon_marker("Chennai", icon_url=icon_url, popup="Marina Beach City")

m.show()
