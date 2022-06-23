import numpy as np
import matplotlib.pyplot as plt
from descartes.patch import PolygonPatch
from shapely.geometry import MultiLineString, Polygon


def plot_shp_poly(
    shp, var_idx, strat_colors, poly_kws, bbox, figsize,
):
    """plot shapefile polygons"""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim([bbox[0], bbox[2]])
    ax.set_ylim([bbox[1], bbox[3]])
    for ci, shape in enumerate(shp.shapes()):
        points = shape.points
        parts = list(shape.parts) + [len(points)]
        exterior = points[parts[0] : parts[1]]
        interior = []
        fc = strat_colors[shp.record(ci)[var_idx]]
        for i in range(1, len(parts) - 1):
            interior.append(points[parts[i] : parts[i + 1]])
        polygon = Polygon(exterior, interior)
        patch = PolygonPatch(polygon, facecolor=fc, **poly_kws)
        ax.add_patch(patch)
    return fig, ax


def plot_shp_line(shp, line_kws, bbox, figsize):
    """plot shapefile lines"""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim([bbox[0], bbox[2]])
    ax.set_ylim([bbox[1], bbox[3]])
    lines = MultiLineString([tuple(shape.points) for shape in shp.shapes()])
    for line in lines:
        a = np.asarray(line)
        ax.plot(a[:, 0], a[:, 1], **line_kws)
    return fig, ax


def add_poly(ax, poly, poly_kws):
    """add polygon patch to ax"""
    ax.add_patch(PolygonPatch(poly, **poly_kws))
    return ax