# Meraki Data analysis through dbscan algorithm

In this code we analyze data from Meraki API. We've enhanced our Meraki data analysis toolkit by integrating the DBSCAN algorithm. This algorithm is for used in machine learning to partition data into clusters based on their distance to other points.

## Installation
Install `docker` and `docker-compose` previously.

Clone the repo
```bash
git clone https://github.com/mighidalgo/dbscan.git
```

Go to your project folder
```bash
cd dbscan
```

## Usage

Run docker compose
```bash
docker-compose up -d
```

Now you have the project up and running, enter the URL
```bash
http://localhost:8001/dbscan - dbscan algorithm.
```

## Configuration

- In order to fetch data from Meraki API, we need to set this env variables in the `docker-compose` file
  - `BASE_URL` - Required, Meraki API URL.
  - `API_KEY` - Required, Apikey to access the API.
  - `ORG_ID` - Optional, if you want the data from a specific organization of the Meraki data, set this var.
  - `EPS` - Required, the maximum distance between two samples for one to be considered as in the neighborhood of the other.
  - `MIN_SAMPLES` - Required, The number of samples (or total weight) in a neighborhood for a point to be considered as a core point.

## Example
- Run the DBSCAN analysis on your Meraki dataset to identify clusters of arbitrary shapes and sizes, and to remove noise and outliers from data sets. The output is a set of clusters of different shapes and sizes, along with any noise points that were identified.

## Additional Notes
The DBSCAN algorithm can identify clusters of arbitrary shapes, is robust to outliers (noise), and does not require the user to specify the number of clusters beforehand, making it particularly useful for exploratory data analysis where the cluster structure is unknown or complex.

## Hardware and Software requirements

You can run this project by just installing `docker` and `docker-compose` on your machine or server.
Recommendend hardware is 4 GB of ram and a dual core processor.
