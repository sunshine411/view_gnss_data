import folium
import numpy as np
import simplekml


def decimal_to_dms(decimal):
    degrees = int(decimal)
    minutes_float = abs(decimal - degrees) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60
    return degrees, minutes, seconds


def read_gps(file_path="../gps.txt"):
    with open(file_path, "r") as f:
        gps_data = [_.strip() for _ in f.readlines()]

    gps_lat = gps_data[9::15]
    gps_lon = gps_data[10::15]
    gps_alt = gps_data[11::15]

    gps_lat = [float(_.split(":")[-1]) for _ in gps_lat]
    gps_lon = [float(_.split(":")[-1]) for _ in gps_lon]
    gps_alt = [float(_.split(":")[-1]) for _ in gps_alt]
    # plt.figure(figsize=(50,50))
    # plt.plot(gps_lon, gps_lat)
    # plt.show()
    # pass
    gps_array = np.vstack([gps_lat, gps_lon]).T
    return gps_array


def gen_folium_map_trace(
    gps_coordinates, save_path="./folium_map_trace.html", marker=False
):
    # 创建地图对象，以第一个坐标为地图中心
    m = folium.Map(location=gps_coordinates[0][:2], zoom_start=13, control_scale=True)

    # 添加marker 标记点
    if marker:
        for i, (lat, lon) in enumerate(gps_coordinates[::100]):
            folium.Marker(location=(lat, lon), popup=f"{i+1}").add_to(m)

    # 绘制轨迹线
    folium.PolyLine(
        [coord[:2] for coord in gps_coordinates], color="blue", weight=2.5, opacity=1
    ).add_to(m)

    # 保存地图到HTML文件
    m.save(save_path)

    print("用于轻量级地图 的 html 文件已生成并保存为 ", save_path)


def gen_google_earth_trace(
    gps_coordinates, save_path="./google_earth_trace.kml", marker=False
):
    kml = simplekml.Kml()

    # 添加marker标记
    if marker:
        for i, (lat, lon) in enumerate(gps_coordinates[::100]):
            kml.newpoint(name=f"{i+1}", coords=[(lon, lat)])

    # 添加轨迹线
    linestring = kml.newlinestring(name="Track Line", coords=gps_coordinates[:, [1, 0]])
    linestring.style.linestyle.width = 3
    linestring.style.linestyle.color = simplekml.Color.red

    # 保存 KML 文件
    kml.save(save_path)

    print("用于google earth 的 KML 文件已生成并保存为 ", save_path)


if __name__ == "__main__":
    gps_coordinates = read_gps("../gps.txt")
    gen_google_earth_trace(
        gps_coordinates, save_path="../google_earth_trace.kml", marker=False
    )
    gen_folium_map_trace(
        gps_coordinates, save_path="../folium_map_trace.html", marker=False
    )
