## 功能: 将ROS发布的sensor_msgs/NavSatFix信息在地图上可视化

### 可以在地图上可视化，同时也可以在googleearth上可视化

### rostopic echo ${topic_name} > gps.txt

```commandline
pip install simplekml folium

python display_map.py
# 生成 folium地图的html文件和可加载到googleearth的配置文件
```



![google_earth](README.assets/google_earth.jpg)



![folium](README.assets/folium.jpg)
