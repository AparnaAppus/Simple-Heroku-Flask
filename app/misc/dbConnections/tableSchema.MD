# Table Queries

### Connect

```Bash
$ heroku pg:psql postgresql-solid-91624 --app sensor-directory-application
```



#### List Tables

```bash
\dt
```

### Tables Created

- **sensorassetlist**

```sql
CREATE TABLE dept_tb(
   id SERIAL NOT NULL PRIMARY KEY,
   name VARCHAR,
   description VARCHAR,
   procurelink VARCHAR,
   referlink VARCHAR,
   appoxcost VARCHAR,
   existingasset VARCHAR,
   commuprotocol VARCHAR,
   range VARCHAR,
   type VARCHAR,
   remarks VARCHAR,
   category VARCHAR,
   application VARCHAR,
   images VARCHAR,
   );

insert into sensorassetlist values (
  1,'RF receiver for active RFID (Sunrom)','This RF Receiver listens on 433 Mhz frequency for our Active rfids transmitter tags. When valid tag is detected in its range of around 25 meters, it outputs a unique 16 bit ID of the tag in serial ASCII data format at 9600 bps baud rate. It supports as many as 64 tags in same premises.','http://www.sunrom.com/p/rf-receiver-for-active-rfid,file:///C:/Users/HP/Downloads/sunrom-227686%20','Rs.300','Yes','RF','25m','Active','NULL','assetTag','Race timing,Attendee Tracking,Logistics & Supply Chain Visibility.. etc','\static\img\assettag1.jpg');

select id,name,description,procurelink,referlink,appoxcost,existingasset,commuprotocol,range,type,remarks,category,application,images from sensorassetlist where category = 'required ones';

```
