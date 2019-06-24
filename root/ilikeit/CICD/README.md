Continuous Integration (CI) -> Continous Delivery (CD) -> Continuous Deployment(CD)
===================================================================================

Continuous Integration (CI) 持续集成
------------------------------------

> 持续集成 (Continous integration, 简称CI), 持续集成的目的就是让产品可以快速迭代，代码集成到主干master之前，必须通过自动化测试，主要有一个测试用例失败，就不能集成。
> Martin Fowler讲过：“持续集成并不能消除Bug,而是让Bug非常容易发现和改正.”

![Continus integration](/imgs/ilikeit/CIDI/continuous_integration.png?raw=true)


Continuous delivery (CD) 持续交付
---------------------------------

> 持续交付 (Continuous delivery) 是指频繁将软件新版本，交付给质量团队，以供评审。如果拼深通过，代码就进入生产阶段


Continuous deployment (CD) 持续部署
-----------------------------------

> 持续部署 (Continuous deployment) 是持续交付的下一步，是指代码通过评审以后，自动部署到生产环境. 持续部署的前提是能自动完成测试、构建、部署

![delivery deployment](/imgs/ilikeit/CIDI/delivery_deployment.png?raw=true)

```
提交: 开发者向代码库提交代码 -> commit 

测试：代码库对commit操作配置钩子(hook),只要提交代码或者合并进主干，就会跑自动化测试.
    测试分类:
        单元测试：针对函数或模块的测试
        集成测试：针对整体产品的某个功能的测试
        端对端测试：从用户界面直达数据库全链路测试

构建：通过测试，代码就可以合并进主干，就算可以交付，交付后，就先进行构建(build).构建是指将源代码转换为可以运行的实际代码，比如安装依赖，配置各种资源。
    常用的构建工具:
        Jenkins -- 开源软件
        Strider -- 开源软件

测试：构建完成就要进行第二轮测试，如果第一轮已经覆盖所有的测试内容，第二轮就可以省略。第二轮测试是全面测试，单元测试和集成测试都要跑，有条件的话也要端对端测试，所有测试以自动化为主。需要强调的是，新版本的每一个更新点都必须测试到，如果测试的覆盖率不高，进入后面的部署阶段后，很可能会出现严重的问题。

部署：当前就是可以直接部署的版本 (artifact). 将这个版本的所有文件打包 (tar filename.tar *) 存档，发送到生产服务器.生产服务器将打包文件，解包成本地的一个目录，再将运行路径的符号链接 (symlink)指向这个目录，然后重新启动应用。
    部署工具:
        Ansible
        Chef
        Puppet 

回滚: 一旦当前版本发生问题，就要回滚到上一版本的构建结果，最简单的做法就是修改一下符号连接，指向上一个版本的目录
```

Jenkins CI 持续集成
------------------
```
This is the Debian package repository of Jenkins to automate installation and upgrade. To use this repository, first add the key to your system:
$ wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

Then add the following entry in your /etc/apt/sources.list:
$ deb https://pkg.jenkins.io/debian-stable binary/

Update your local package index, then finally install Jenkins:
$ sudo apt-get update 
$ sudo apt-get install jenkins 

Jenkins will start automatically on port 8080.
第一次启动Jenkins，Jenkins会自动生成一个随机口令，访问http://localhost:8080/ 
$ sudo systemctl status jenkins 
```

Jenkins For Continuous Integration
----------------------------------
> Continuous Integration is the most important part of DevOps that is used to integrate various DevOps stages. Jenkins is        the most famous Continuous Integration tool

* What is Jenkins?
> Jenkins is an open source automation tool written in Java with plugins built for Continous Integration purpose. Jenkins        is used to build and test your software projects continously making it easier for developers to integrate changes to the         project, and making it easier for users to obatin a fresh build.
> Jenkins integrates development life-cycle processes of all kinds, including build, document, test, package, stage,             deploy, static analysis and much more.
    - Advantages of Jenkins include:
        * It is an open source tool with great community support
        * It is easy to install
        * It has 1000+ plugins to ease your work. If a plugin does not exist, you can code it and share with the community.
        * Jenkins is widespread, with more than 147,000 active installations and over 1 million users around the world.
        * Jenkins is interconnected with well over 1,000 plugins that allow it to integrate with most of the development,        testing and deployment tools.

* What is Continuous Integration?
> Continuous Integration is a development practice in which the developers are required to commit changes to the source code in a shared repository several times a day of more frequently.

![Continuous Integration With Jenkins](/imgs/ilikeit/CIDI/ci_with_jenkins.png?raw=true)
    
    - First, a developer commits the code to the source code repository, Meanwhile, the Jenkins server checks the repository at regular intervals for changes.
    - Soon after a commit occurs, the Jenkins server detects the changes that have occurred in the source code repository. Jenkins will pull those changes and will sart preparing a new build.
    - If the build fails, then the concerned team will be notified.
    - If built is successful, then Jenkins deploys the built in the test server.
    - After testing,Jenkins generates a feedback and then notifies the developers about the build and test results.
    - It will continue to check the source code repository for changes made in the source code and the whole process keeps on repeating.

* Install Jenkins
    - 1. Install Java Version 8 - Jenkins is Java Based application, hence Java is a must.
    - 2. Install Apache Tomcat Version 9 - Tomcat is requirement to deploy Jenkins war file.
    - 3. Download Jenkins war File - This war is required to install Jenkins.
    - 4. Deploy Jenkins war File - Jenkins war file needs to be deployed using Tomcat to run Jenkins 
    - 5. Install Suggested Plugins - Install a list of plugins suggested by Jenkins.

* Download Jenkins war File:
    - Now download Jenkins war file by using wget command:
    - $ wget http://updates.jenkins-ci.org/latest/jenkins.war 

* Deploy Jenkins war file 
    - To deploy Jenkins war file that you have downloaded in the previous step, open your browser and access localhost:8080 again. Now click on the Manager App.
    - Now you will be directed to Tomcat web application manager page. When you scroll down you will find an option called WAR file to deploy.
    - Now click on "/jenkins" or http://localhost:8080:jenkins

* Install Suggested Plugins 
    - In order to unlock Jenkins first copy the part that. This is the location that contains your one time password for Jenkins i.e: /home/pi/.jenkins/secrets/initiaAdminPassword. 
    - Install Suggested Plugins 
    - Create First Admin User

* Congratulations!
    - Jenkins is ready now, once you click on start using Jenkins you will be directed to Jenkins dashboard.

Continuous Integration Using Jenkins
------------------------------------

* Jenkins Distributed Architecture 
> Jenkins uses a Master-Slave architecture to manage distributed builds. In this architecture, Master and Slave communicate through TCP/IP protocol.
    - Jenkins Master (The Main Jenkins server is the Master)
        * Scheduling build jobs.
        * Dispatching builds to the slaves for the actual execution
        * Monitor the slaves (possibly taking them online and offline as required) 
        * Recording and presenting the build results.
        * A Master instance of Jenkins can also execute build jobs directly
    - Jenkins Slave (Slave is a Java executable that runs on a remote machine.)
        * It hears requests from the Jenkins Master instance.
        * Slaves can run on a variety of operating systems.
        * The job of a Slave is to do as they are told to, which involves executing build jobs dispatched by the Master.
        * You can configure a project to always run on a particular Slave machine, or a particular type of Slave machine. or simply let Jenkins next available Slave.

![Jenkins Distributed Architecture](/imgs/ilikeit/CIDI/Jenkins_Distributed_Architecture.png?raw=true)

* Which Jenkins is used for testing in different environment
![Jenkins Distributed Testing](/imgs/ilikeit/CIDI/Jenkins-Distributed-Testing.png?raw=true)
    - Jenkins checks the Git repository at periodic intervals for any changes made in the source code.
    - Each builds requires a different testing environment which is not possible for a single Jenkins server.In order to perform testing in different environments Jenkins uses various Slaves as shown in the diagram.
    - Jenkins Master requests these Slaves to perform testing and to generate test reports.

* Jenkins Build Pipeline (The Jenkins Pipeline gives you an overview of where tests are up to)
![Jenkins Build Pipeline](/imgs/ilikeit/CIDI/Jenkins-build-Pipeline.png?raw=true)

* Create a new job in Jenkins
    - Freestyle Project
        * Freestyle build jobs are general-purpose build jobs, which provides maximum flexibility.
    - Multiconfiguration Job
        * 
    - Monitor an External Job 
    - Maven Project 

Jenkins and Python
------------------
> setting up a continuous integration server, Jenkins, with our Python applications
    - install Jenkins on Ubuntu 
    - clone and install a Python application in a virtualenv 
    - run tests using nose and publish tests results, code coverage and pylint reports
    - have Github notify Jenkins when new code is pushed 

> Setup a Jenkins job 
```
1. Create a new job and call it something without spaces! Jenkins creates a directory of the same name on the filesystem, but pip (or virtualenv?) will choke on spaces. Then select "Build a free-style software project".
```

Jenkins Abnormal Problem
------------------------
* Stop Jenkins log from becoming huge
    - /var/log/jenkins.log has started getting very large, very quickly, full of exceptions about DNS resolution. 
