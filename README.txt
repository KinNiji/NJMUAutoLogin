安装依赖
pip install -r requirements.txt

确保安装了Chrome浏览器，右键其快捷方式打开文件所在位置，所示第一个文件夹名即为您所安装的Chrome版本
打开下方链接，找到您安装的Chrome对应版本的内核，下载后解压，将chromedriver.exe放到lib文件夹下
http://chromedriver.storage.googleapis.com/index.html

修改配置：将config_sample.json重命名为config.json
{
  "userId": "你的账号",
  "password": "你的密码",
  "nasip": "登录页面一大串url中&nasip=的值",
  "service": "_service_0是校园网_service_1是联通_service_0是电信",
  "waiting": 此项为数字，每次重连间隔的时间
}

安装anaconda或miniconda，编辑run.bat内容第一行为其activate.bat所在路径和其所在路径
双击run.bat运行程序