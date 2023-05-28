
# HTTP(S) Proxy Grabber

This Python script is used to grab HTTP(S) proxies from multiple sources and store them in a text file. It periodically updates the proxy list by fetching the proxies from various links. The script provides options to run once or run continuously at specified intervals.

## Features

-   Grabs HTTP(S) proxies from multiple sources
-   Checks the validity of each proxy before adding it to the list
-   Removes empty lines and duplicates from the proxy list
-   Supports running once or running continuously at specified intervals

## Prerequisites

-   Python 3.x
-   `requests` library (can be installed using `pip install requests`)

## Usage

### Running Once

To grab the proxies once and exit, execute the script with the following command:

`python proxy_grabber.py now` 

This will grab the proxies from the sources, update the proxy list file, and then exit.

### Running Continuously

To continuously grab the proxies at specified intervals, execute the script without any additional arguments:

`python proxy_grabber.py` 

The script will run indefinitely, periodically updating the proxy list file at the specified interval (default is 1 hour).

## Configuration

You can modify the following variables in the script to customize its behavior:

-   `links`: A list of URLs pointing to the proxy sources.
-   `output_file`: The name of the file where the proxy list will be stored.
-   `interval`: The interval (in seconds) at which the script will update the proxy list (applicable only when running continuously).

## License

This script is released under the [MIT License](https://opensource.org/license/mit).

----------

Coded by JadaDev
