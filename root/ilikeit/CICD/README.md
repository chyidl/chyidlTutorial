Continuous Integration (CI) -> Continous Delivery (CD) -> Continuous Deployment(CD)
===================================================================================

Continuous Integration (CI) 持续集成
------------------------------------

> 持续集成 (Continous integration, 简称CI), 持续集成的目的就是让产品可以快速迭代，代码集成到主干master之前，必须通过自动化测试，主要有一个测试用例失败，就不能集成。
> Martin Fowler讲过：“持续集成并不能消除Bug,而是让Bug非常容易发现和改正.”

![Continus integration](/imgs/ilike/CIDI/continuous_integration.png?raw=true)


Continuous delivery (CD) 持续交付
---------------------------------

> 持续交付 (Continuous delivery) 是指频繁将软件新版本，交付给质量团队，以供评审。如果拼深通过，代码就进入生产阶段


Continuous deployment (CD) 持续部署
-----------------------------------

> 持续部署 (Continuous deployment) 是持续交付的下一步，是指代码通过评审以后，自动部署到生产环境. 持续部署的前提是能自动完成测试、构建、部署

![delivery deployment](/imgs/ilike/CIDI/delivery_deployment.png?raw=true)

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

```
