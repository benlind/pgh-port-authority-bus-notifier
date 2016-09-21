default_buses = ['71A', '71C']  # buses to use if none are passed

def watch_for_buses(buses, direction='OUTBOUND'):
    """Notify user when buses appear on Port Authority tracker

    Args:
        buses:     a list of strings containing bus names
                   (default: ['71A', '71C'])
        direction: direction the buses are traveling
                   (options: OUTBOUND or INBOUND, default: OUTBOUND)

    Todo:
        - Customize system alert based on OS
        - Let the user specify bus stop ID
    """
    import requests, time, webbrowser, os

    buses = buses or default_buses

    print("At your service, master Wayne. I'll listen for the " + listify(buses))

    bus_url = 'http://realtime.portauthority.org/bustime/wireless/html/eta.jsp' \
              '?route=' + buses[0] + '&direction=' + direction + '&id=2566' \
              '&showAllBusses=on'
    bus_html = requests.get(bus_url).text

    while not any(bus in bus_html for bus in buses):
        # The bus is not coming yet
        time.sleep(15)

    print("A bus approaches, master Wayne. Shall I fetch your coat?")

    # Open a system dialog to notify the user
    os.system('osascript -e \'tell app "System Events" to display alert "Bus" ' \
              'message "A bus is coming!"\' &> /dev/null')

    # Open the bus list in a browser
    webbrowser.open(bus_url)


def listify(items):
    """Convert Python list to grammatically correct English list string"""
    if (len(items) == 1): return items[0]
    if (len(items) == 2): return ' and '.join(items)
    return ', '.join(items[0:-1]) + ', and ' + items[-1]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Watch for some buses.')
    parser.add_argument('buses', nargs='*', default=default_buses,
                        help='buses to watch for')
    parser.add_argument('-d', '--direction', choices=['OUTBOUND', 'INBOUND'],
                        default='OUTBOUND', help='direction the bus will travel')
    args = parser.parse_args()

    watch_for_buses(args.buses, direction=args.direction)
