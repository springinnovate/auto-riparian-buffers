"""Build stream network and then riparian buffer zones."""
import argparse
import os
import logging
import sys

from osgeo import gdal
from ecoshard import geoprocessing
from ecoshard import taskgraph

gdal.SetCacheMax(2**26)
_LARGEST_BLOCK = 2**26

logging.basicConfig(
    level=logging.DEBUG,
    format=(
        '%(asctime)s (%(relativeCreated)d) %(levelname)s %(name)s'
        ' [%(pathname)s.%(funcName)s:%(lineno)d] %(message)s'),
    stream=sys.stdout)
LOGGER = logging.getLogger(__name__)
logging.getLogger('ecoshard.taskgraph').setLevel(logging.INFO)


WORKSPACE_DIR = '_workspace_auto_riparian_buffers'

def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description='Auto riparian buffers')
    parser.add_argument('dem_raster_path', help='Path to DEM raster.')
    args = parser.parse_args()

    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    task_graph = taskgraph.TaskGraph(WORKSPACE_DIR, 0)
    LOGGER.debug(args.dem_raster_path)


if __name__ == '__main__':
    main()