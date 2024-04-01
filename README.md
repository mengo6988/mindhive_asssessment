# mindhive_asssessment

Mindhive Assessment: Subway Finder
This is a rest API to find subway outlets in Kuala Lumpur. Data was scraped from https://www.subway.com.my/find-a-subway

Table of Contents

Installation: #installation
Usage: #usage
Contributing: #contributing
# Installation

To get started with this project, you'll need Python 3 and pip (the package installer for Python) installed on your system.

Clone the repository:

Bash
git clone https://github.com/your-username/your-repository-name.git
Use code with caution.

 Install dependencies:

Navigate to the project directory and install the required Python packages listed in the requirements.txt file:

Bash
cd your-repository-name
pip3 install -r requirements.txt

 Usage

This project provides two scripts:

seed.py: This script is used to populate your database with initial data (if applicable).
Run it using:

Bash
python3 seed.py

 app.py: This script runs the main application server.
Start the server with:

Bash
python3 app.py

Contributing


# Additional Notes

Replace api-key in index.html if you want to test out the google maps API as well.
src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY_HERE&callback=initMap"
https://developers.google.com/maps/documentation/javascript/overview
