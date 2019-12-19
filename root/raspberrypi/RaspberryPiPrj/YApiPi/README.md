YAPI
====
> YAPI 是高效、易用、功能强大的api管理平台，旨在为开发、产品、测试人员提供更优雅的接口管理服务，可以帮助开发者轻松创建、发布、维护API，YAPI还为用户提供了优秀的交互体验，开发人员只需利用平台提供的接口数据写入工具以及简单的点击操作就可以实现接口的管理

特征
---
```
基于Json5 和 Mockjs定义接口返回数据的结构和文档，效率提升多倍
扁平化权限设计，即保证大型企业级项目的管理，又保证易用性 
类似postman的接口调试 
自动化测试，支持对Response断言
MockServer除支持普通的随机mock外，还增加了Mock期望功能，根据设置的请求过滤规则，返回期望数据
支持postman,har,swagger数据导入 
```

内网部署
------

* 环境要求 
```
Nodejs ()
Mongodb 
git 
```

* 安装
```
$ npm install -g yapi-cli --registry https://registry.npm.taobao.org 
$ yapi server 
```

* 服务管理 
```
利用pm2方便服务管理维护 
$ npm install pm2 -g    // 安装pm2 
$ cd <项目目录>
$ pm2 start "vendors/server/app.js" --name yapi     // pm2 管理yapi服务 
$ pm2 info yapi         // 查看服务信息  
$ pm2 stop yapi         // 停止服务 
$ pm2 restart yapi      // 重启服务 
```

* 升级 
```
升级项目版本是非常容易，并且不会影响已有的项目数据，只会同步vendors目录下的源代码 

```