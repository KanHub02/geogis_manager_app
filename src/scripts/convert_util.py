import os
import glob
import rasterio


def convert_jp2_to_tiff(jp2_file_path, tiff_file_path):

    """jp2 file path must be a directory with .jp2 files"""

    jp2_directory = jp2_file_path

    output_geotiff_path = tiff_file_path

    jp2_files = glob.glob(os.path.join(jp2_directory, "*.jp2"))

    with rasterio.open(jp2_files[0]) as src:
        profile = src.profile

        profile.update(driver="GTiff")

        with rasterio.open(output_geotiff_path, "w", **profile) as dst:
            for jp2_file in jp2_files:
                with rasterio.open(jp2_file) as src:
                    data = src.read(1)
                    dst.write(data, 1)

    print("Conversion complete.")


# convert_jp2_to_tiff("get_data/data/", "get_data/1.tiff")
