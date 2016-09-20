import sys, requests, time, webbrowser, os

buses = ['71A', '71C']  # default buses to watch for

if len(sys.argv) > 1:   # user passed in buses
    buses = sys.argv[1:]

bus_url = 'http://realtime.portauthority.org/bustime/wireless/html/eta.jsp' \
          '?route=71A&direction=OUTBOUND&id=2566&showAllBusses=on'
bus_html = requests.get(bus_url).text

print("At your service, master Wayne. I'll listen for the bus.")

while not any(bus in bus_html for bus in buses):
    # The bus is not coming yet
    time.sleep(15)

print("The bus approaches, master Wayne. Shall I fetch your coat?")

# Open a system dialog to notify the user
os.system('osascript -e \'tell app "System Events" to display alert "Bus" ' \
          'message "A bus approacheth!"\' &> /dev/null')

webbrowser.open(bus_url)
