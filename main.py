import pandas as pd
from tqdm import tqdm

from src.google_maps import get_geolocation, plot_map

def get_addresses():
    dentistas = pd.read_csv('dentistas.csv')
    addresses = dentistas['DOMICILIO'] + ', Rosario, Argentina'
    return addresses.to_list()


def main():
    addresses = get_addresses()
    geolocations = []
    for address in tqdm(addresses):
        geolocation = get_geolocation(address)  
        geolocations.append(geolocation)
    
    map_center_address = 'Crespo 250, Rosario, Argentina'
    map_center_geolocation = get_geolocation(map_center_address)
    plot_map(map_center_geolocation, geolocations, 'dentistas')

if __name__ == '__main__':
    main()