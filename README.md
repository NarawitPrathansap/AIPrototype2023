# AIPrototype2023 
Github นี้เป็นส่วนหนึ่งของรายวิขา SC664401: การสร้างต้นแบบสำหรับระบบปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง


## Table of Contents
- [:penguin: Linux (Ubuntu) Commands](#penguin-linux-ubuntu-commands)
  - [🤖 Basic Command Line Operations](#-basic-command-line-operations)
  - [📂 Ubuntu](#-ubuntu)
- [:cloud: Azure Cloud Operations](#cloud-azure-cloud-operations)
- [:snake: Setup Environment with Miniconda](#snake-setup-environment-with-miniconda)
- [:octocat: Github setup](#octocat-github-setup)
- [:octocat: GitHub Version Control](#octocat-github-version-control)
- [:brain: Deep Learning Implementation](#brain-deep-learning-implementation)
- [⭐ Web page](#-web-page)
- [:globe_with_meridians: Web Application](#globe_with_meridians-web-application)

## :penguin: Linux (Ubuntu) Commands
### 🤖 Basic Command Line Operations
Terminal คือสะพานที่เชื่อมระหว่างคนกับคอมพิวเตอร์เครื่องอื่น ๆ และในคำสั่งสำหรับ linux จะมีสองส่วนที่สำคัญคือ {คำสั่ง} {option}

- `ls`: list ไฟล์ทั้งหมดที่อยู่ใน directory นั้น.
- `pwd`: คำสั่งไว้ check ว่าเราอยู่ตรงไหนของ terminal.
- `mkdir`: คำสั่งสำหรับสร้าง folder (directory).
- `cd`: Change the directory. คำสั่งที่ใช้สำหรับกระโดดไปมาระหว่าง folder. เช่น cd .. คือการออกมาจากโฟลเดอร์นั้น 1 step
- `rm -R`: คำสั่งสำหรับ remove folder (จะมี -R).
- `vi`: คำสั่งที่จะใช้สร้างหรือแก้ไขไฟล์.ก่อนจะเขียนไฟล์ต้องกด i ก่อน หลังจากแก้ไขหรือเขียนเสร็จแล้วให้กด esc และกด `:wq` สำหรับsaveและออกมา
- `ls -ltr`: คำสั่งที่ใช้เพื่อดูรายละเอียดของโฟลเดอร์ที่สร้าง เช่น สร้างตอนไหน หรือมีสิทธิ์แก้ไขอะไรได้บ้าง.
- `cp -R`: คำสั่งที่ใช้สำหรับ copy folder.
- `mv`: คำสั่งที่ใช้สำหรับการย้ายไฟล์.
- `code` : เป็นคำสั่งที่ใช้สำหรับรัน vscode บน linux

### 📂 Ubuntu
- [Argparse](https://github.com/NarawitPrathansap/AIPrototype2023/blob/main/firstpy.py)
- [Flask](https://github.com/NarawitPrathansap/AIPrototype2023/blob/main/firstclass.py)
- [Python subprocess](https://github.com/NarawitPrathansap/AIPrototype2023/blob/main/python_subprocess.py)
- [Web service request](https://github.com/NarawitPrathansap/AIPrototype2023/blob/main/Web_service_request.ipynb)
- [Homework](https://github.com/NarawitPrathansap/AIPrototype2023/blob/main/homework)

### :cloud: Azure Cloud Operations
Interact with VMs and manage resources on the Azure cloud platform.[Azure](https://portal.azure.com/#home)

- `ssh {Username}@{ip_address}`: คำสั่งที่ใช้ต่อเข้ากับ vm บน cloud.
- `scp -r`: คำสั่งคัดลอก directory.
- `htop`: คำสั่งที่ใช้ดูการทำงานของระบบ และเราสารมารถใช้เช็คได้ด้วยว่ามีใครเข้ามาในเครื่องของเราบ้าง.
- `screen -S {name}`: คำสั่งที่ใช้สร้าง section ใหม่ขึ้นมาซึ่งจะแยกกับ section ที่เราใช้งานอยู่ // กด Crt+A พร้อมกัน และกด d ถ้าเราต้องการออกจาก screen นั้น.
- `screen -R {name}`: คำสั่งที่ใช้สำหรับเข้าไปยัง screen // กด Crt+A พร้อมกัน และกด k ถ้าเราต้องการออกลบ screen นั้น.
- `screen -list`: คำสั่งที่ใช้สำหรับ list รายชื่อ screen ทั้งหมดที่กำลังทำงาน.
- `exit`: คำสั่งที่ใช้สำหรับออกจาก vm.

## :snake: Setup Environment with Miniconda

ติดตั้ง miniconda เพื่อใช้งาน python environment และสำหรับจัดการ package บนเครื่องเรา 
ต่อไปนี้เป็นวิธีการตั้งค่า:

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```
- `conda activate {env_name}`: เรียกใช้งาน Environment
- `conda deactivate`: ยกเลิกการใช้งาน Environment
- `conda rename -n {ชื่อเก่า} {ชื่อใหม่}`: เปลี่ยนชื่อ Environment
- `conda env list`: เช็คว่ามี Environment อะไรบ้าง
- `cat {filename}`: ใช้รวมข้อมูล file รวมถึงแสดงผลข้อมูลออกมาในรูปแบบ text
- `python {filename.py}`: ใช้งาน python

## :octocat: Github setup
```bash
cd /mnt/c # เข้าไปที่ drive c
mkdir Ubuntu #สร้างโฟลเดอร์ที่ชื่อว่า Ubuntu ใน drive c
mkdir outside #สร้างโฟลเดอร์ที่ชื่อว่า outside ที่หน้า home
ln -s mnt/c/Ubuntu /home/papapz1/outside #สร้าง symbolic link จาก outside ไป Ubuntu
git clone https://github.com/NarawitPrathansap/AIPrototype2023.git #เข้าไปใน Ubuntu แล้วโคลน github เราลงไป
```
## :octocat: GitHub Version Control
คำสั่งสำหรับใช้งาน github บน linux
```bash
git config --global user.name "Your Name" #ตั้งค่า ชื่อกับเมล github ของเรา
git config --global user.email "your_email@example.com"
git clone https://github.com/YourUsername/YourRepository.git #เข้าไปใน Ubuntu แล้วโคลน github เราลงไป
git pull # เป็นการดึงไฟล์ที่มีการเปลี่ยนแปลงใน remote มาเปลี่ยนแปลงใน local
git status # เช็คว่ามีอะไรเปลี่ยนไปบ้าง
git add {file_name} 
git commit -m "Commit message"
git push # อัพงานเราขึ้นบน github
```
## :brain: Deep Learning Implementation
- [Google Colab](https://colab.research.google.com/drive/1W0q05xSQ608i3sQaBwoY4vZvV_zOXXTK)
- [Lecture](https://github.com/NarawitPrathansap/AIPrototype2023/blob/main/Lecturedeeplr.pdf)
## ⭐ Web page
- [Web page](https://narawitprathansap.github.io/Test_webpage/)
- [Web page project]()
## :globe_with_meridians: Web application
- [Web application]()
