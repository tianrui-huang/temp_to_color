# temp_to_color

## 简介 
在GNU/Linux平台上，使用Nvidia显卡。实时监控CPU与GPU温度，并以此用OpenRGB的SDK服务来分别控制风扇和显卡的RGB灯的颜色（实际上是主板上的两个接口信息，如果显卡是独立控光的就不能用，如果机子用了更多接口，就改下部分代码即可） 

## 部署方法 
**注**：本项目原生支持的是基于Linux的系统，具体影响在sensor/下的数据获取接口上，如果使用Windows系统，更改对接接口应该可以实现移植。 

1. 项目基于OpenRGB,需要前往 <https://openrgb.org> 获取最新版OpenRGB 
2. 在Setting中开启登录时启动服务器并将IP和端口设为127.0.0.1:6742 
3. 拉取本项目 
4. 启动OpenRGB扫描自己的设备，并认真阅读本项目代码，修改代码中和自己设备不一致的地方 
5. 编辑 `~/.config/systemd/user/rgbd.service`,设置系统服务 
6. 运行 `systemctl --user daemon-reload`,重载服务状态，`systemctl --user enable rgbd.service`来自启 

## 项目能力 
能平滑地让颜色随温度变化 

## 展望 
未来会给它加上动态光效，而不只是纯色的 
