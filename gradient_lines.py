import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ratio_size = (-87.933976504, -87.527617648, 41.647708795, 42.015842432)

chi_map = plt.imread("chigao_map.png")
fig, ax = plt.subplots(figsize=(18, 14))
ax.set_xlim(ratio_size[0], ratio_size[1])
ax.set_ylim(ratio_size[2], ratio_size[3])

point_west = [[-87.675235, -87.690210], [41.624759, 42.010519], 14215]
point_pulanski = [[-87.713312, -87.728920], [41.533661, 41.997166], 12415]
point_cicero = [[-87.732058, -87.747818], [41.443951, 42.015250], 11357]
point_ashland = [[-87.662697, -87.669785], [41.721411, 41.987494], 11261]
point_halsted = [[-87.641864, -87.649610], [41.512029, 41.951209], 10018]
point_kedzie = [[-87.622096, -87.708871], [41.780131, 41.982957], 8801]
point_michigan = [[87.622096, -87.624046], [41.780131, 41.900757], 6828]
point_state = [[-87.622066, -87.628865], [41.663608, 41.911129], 6161]
point_north = [[-87.634764, -88.264933], [41.911097, 41.921170], 6035]
point_clark = [[87.630073, -87.676349], [41.853061, 42.019327], 6761]
point_lake_shore = [[-87.575086, -87.653601], [41.775499, 41.985505], 7519]
point_lawrence = [[-87.646041, -87.786691], [41.967481, 41.969620], 3078]
point_lake = [[-87.846446, -87.647282], [41.973726, 41.976107], 3026]
point_diversey = [[-87.684260, -87.820696], [41.930607, 41.932199], 3017]
point_foster = [[-87.846446, -87.647282], [41.973726, 41.976107], 3010]


def create_gradient(coord_list, map):
    all_lines = []
    for x in coord_list:
        df3 = pd.DataFrame([{'x': x[0][0], 'y': x[1][0]}, {'x': x[0][1], 'y': x[1][1]}])
        location_x = np.linspace(df3.iloc[0, 0], df3.iloc[1, 0], 1000)
        location_y = np.linspace(df3.iloc[0, 1], df3.iloc[1, 1], 1000)
        locations_weighted = pd.DataFrame({'x': location_x, 'y': location_y, 'wt': x[2]})
        all_lines.append(locations_weighted)
    df_gradient = pd.concat(all_lines)

    g = ax.scatter(df_gradient.x, df_gradient.y, c=df_gradient.wt, cmap='winter_r', s=1)
    plt.imshow(map, zorder=0, extent=ratio_size, aspect='equal')
    fig.colorbar(g)
    plt.show()
    return df_gradient


create_gradient([point_west, point_pulanski, point_cicero, point_ashland,
                 point_halsted,
                 point_kedzie,
                 point_michigan,
                 point_state,
                 point_north,
                 point_clark,
                 point_lake_shore,
                 point_lawrence,
                 point_lake,
                 point_diversey,
                 point_foster], chi_map)
