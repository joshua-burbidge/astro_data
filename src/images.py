import requests
from io import BytesIO
from PIL import Image
from astroquery.skyview import SkyView
import astropy.units as u

def get_image_sdss(degree_coords, query=None):
    """
    Fetch an SDSS image for the given coordinates.

    Parameters:
    degree_coords (dict): A dictionary with 'RA' and 'DEC' keys containing the coordinates in degrees.
    query (dict, optional): Additional query parameters for the SDSS image cutout. See API documentation.

    Returns:
    image: the JPEG image.
    """
    # API ref: https://skyserver.sdss.org/dr16/en/help/docs/api.aspx#imgcutout
    base_url = "http://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?"

    if query:
        params = {**degree_coords, **query}
    else:
        params = degree_coords.copy()
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an error for bad responses

    buffer = BytesIO(response.content)
    return Image.open(buffer)

def get_image_skyview(degree_coords, options=None):
    """
    Fetch a SkyView image for the given coordinates.

    Parameters:
    degree_coords (dict): A dictionary with 'RA' and 'DEC' keys containing the coordinates in degrees.
    options (dict, optional): Additional options for the SkyView query. Properties: height, width, pixels

    Returns:
    hdu: An HDUList representing the image.
    """
    position = f"{degree_coords['RA']} {degree_coords['DEC']}"

    images = SkyView.get_images(
        position=position,
        survey=['SDSSg'],
        **(options or {})
    )

    if not images or len(images) == 0:
        raise ValueError("No images found for the given coordinates.")

    hdu_list = images[0]

    if not hdu_list or len(hdu_list) == 0:
        raise ValueError("No HDU found in the image list.")

    return hdu_list