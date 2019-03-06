-- 如果test数据库不存在，就创建test数据库:
CREATE DATABASE IF NOT EXIST test;

-- 切换到test数据库
USE test;

-- 删除classes表和students表（如果存在）
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS students;

-- 创建classes表
CREATE TABLE classes (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8-mb4;

