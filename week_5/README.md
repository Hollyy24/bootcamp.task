# Week 5 Assignment 

### Task 2 : 
---

####

```
CREATE DATABASE website;
```

- !["test"](screenshot/2-1-1.png)

####


```
    Create TABLE member(   
        id bigint NOT NULL AUTO_INCREMENT,  
        name varchar(255) NOT NULL,  
        username varchar(255) NOT NULL,  
        password varchar(255) NOT NULL,  
        follower_count int unsigned NOT NULL DEFAULT '0',  
        time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,) ;
```
- ![图片alt](screenshot/2-2-1.png)
  
---
### Task 3: 
---
####

```
    INSERT INTO member(name,username,password)
    VALUES
    ('test','test','test');
```
- ![alt](screenshot/3-1-1.png)

####

```
    INSERT INTO member(name,username,password)
    VALUES
    ('Holly','H','h1234');
```
- ![alt](screenshot/3-1-2.png)
####
  
```
    INSERT INTO member(name,username,password)
    VALUES
    ('lily','Lily','lily1234');
    ('steven','S','s1234');
    ('John','JJ','JJ1234');

```
- ![alt](screenshot/3-1-3.png)

####

```
    SELECT * FROM member;
```
   * ![图片alt](screenshot/3-2-1.png)
####


```
    SELECT * FROM member ORDER BY time DESC;
```

- - ![图片alt](screenshot/3-3-1.png)
####


```
    SELECT * FROM member ORDER BY time DESC LIMIT 1,3;
```

![图片alt](screenshot/3-4-1.png)
####

```
    SELECT * FROM member WHERE username='test';
```

![图片alt](screenshot/3-5-1.png)
####

```
    SELECT * FROM member 
    WHERE name REGEXP 'es';
```

- ![图片alt](screenshot/3-6-1.png)
####

```
    SELECT * FROM member 
    WHERE username ='test' AND password = 'test';
```
- ![图片alt](screenshot/3-7-1.png)
####


```
    UPDATE member
    SET name = 'test2' 
    WHERE username = 'test';
```

- ![图片alt](screenshot/3-8-1.png)
####

---
### Task4
---
####

```
    SELECT COUNT(*)
    FROM member;
```
- ![图片alt](screenshot/4-1-1.png)
####

```
    SELECT SUM(follower_count)
    FROM member;
```
- ![图片alt](screenshot/4-2-1.png)
####


```
    SELECT AVG(follower_count)
    FROM member;
```

- ![图片alt](screenshot/4-3-1.png)
####

```
    SELECT AVG(follower_count)
    FROM(
        SELECT follower_count
        FROM member
        ORDER BY follower_count DESC
        LIMIT 2)
        AS avg_follower;
```

- ![图片alt](screenshot/4-4-1.png)
####

---
### Task5
---
####

```
    CREATE TABLE message(
        id BIGINT AUTO_INCREMENT PRIMARY  KEY,
        member_id BIGINT NOT NULL,
        content VARCHAR(255) NOT NULL,
        like_count INT NOT NULL DEFAULT 0.
        time DATETIME NOOT NULL DEFAULT CURRENT_TIMESTAMP.
        CONSTRAINY FK_member FOREGIN KEY ( member_id)
        REFERENCES member(id)
    );
```
- ![图片alt](screenshot/5-1-1.png)
- ![图片alt](screenshot/5-1-2.png)
####

```
    SELECT message.* member.name
    FROM message 
    LEFT JOIN member
    ON message.member_id = member.id;
```
- ![图片alt](screenshot/5-2-1.png)
####

```
    SELECT message.*, member.name
    FROM message
    LEFT JOIN  member
    ON message.member_id = member.id
    WHERE member.username = 'test';
```
- ![图片alt](screenshot/5-3-1.png)
####

```
    方法一：

        SELECT AVG(message.like_count)
        FROM (
            SELECT message.X, member.username
            LEFT JOIN member
            ON message.member_id = member.id
            WHERE member.username = 'test')
        AS result;

    方法二：

        SELECT AVG(message.like_count)
        FROM message
        LEFT JOIN member
        ON message.member_id = member.id
        WHERE member.username = 'test';


```
- 方法一
  - ![图片alt](screenshot/5-4-2.png)
- 方法二
  - ![图片alt](screenshot/5-4-1.png)

####

```
    SELECT member.username, AVG(message.like_count) AS result
    FROM message
    LEFT JOIN member
    ON message.member_id = member.id
    GROUP BY  member.username;
```

- ![图片alt](screenshot/5-5-1.png)
