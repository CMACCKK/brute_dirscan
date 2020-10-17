# dirscan

### 默认扫描

```
python3 dirscan.py -u 192.168.2.206
```

![image-20201005132056137](C:\Users\19711\AppData\Roaming\Typora\typora-user-images\image-20201005132056137.png)

### 指定线程

```
python3 dirscan.py -u 192.168.2.206 -t 12
```

![image-20201005132734959](C:\Users\19711\AppData\Roaming\Typora\typora-user-images\image-20201005132734959.png)

### 指定扫描目录

```
python3 dirscan.py -u 192.168.2.206 -t 12 -e php
```

![image-20201005132824933](C:\Users\19711\AppData\Roaming\Typora\typora-user-images\image-20201005132824933.png)

指定cookie

```
python3 dirscan.py -u 192.168.2.206 -t 12 -e php -c 'user=admin'
```

![image-20201005132928457](C:\Users\19711\AppData\Roaming\Typora\typora-user-images\image-20201005132928457.png)

### Author:CMACCKK

### QQ:1971134857