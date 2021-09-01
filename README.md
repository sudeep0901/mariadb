Running mysql in docker

docker run --name mysql -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql

Connecting to mysql in docker
 mysql --host=127.0.0.1 --port=3307 -u root -p root


# Check if bin log enabled

SHOW VARIABLES LIKE 'log_bin';
SHOW BINARY LOGS


# Backup data

```sh
mysqldump --user=root --password=admin test --single-transaction --routines --flush-logs  > sudeep_git_local_practice/mysql-mariadb/test
_db_backup.sql

When error use below command

 mysql_upgrade -u sp628k -p
```

# MYSQL Commands
```sh
    Show version
 SHOW VARIABLES Like '%version%'
show variables like '%binlog_gtid_simple_recovery%'
SET @@GLOBAL.gtid_purged
The values that enforce_gtid_consistency can be configured to are:
	• OFF: all transactions are allowed to violate GTID consistency.
	• ON: no transaction is allowed to violate GTID consistency.
	• WARN: all transactions are allowed to violate GTID consistency, but a warning is generated in this case.
SELECT @@ENFORCE_GTID_CONSISTENCY

SHOW VARIABLES LIKE 'ENFORCE_GTID_CONSISTENCY';

SHOW SLAVE STATUS

SHOW REPLICA STATUS

START SLAVE 

FLUSH LOGS
```
# Binlogs
## Show binary logs
```sh
SHOW BINARY LOGS;
show binlog events;
show binary log events in 'mysql-in-log.000001' from 27298;
show binlog events\G;
show variables like "%binlog_format%"
SET GLOBAL binlog_format = 'STATEMENT';
SET GLOBAL binlog_format = 'MIXED';		
SET GLOBAL binlog_format = 'ROW';


SELECT BINLOG_GTID_POS('mariadb-bin.000001', 510);

```
## Setting up enable bin log
```sh
SET sql_log_bin = 0;
SET sql_log_bin = 1;

PURGE BINARY LOGS TO 'mariadb-bin.000063';
PURGE BINARY LOGS BEFORE '2013-04-22 09:55:22';
flush logs




```

## Using BinLogs To Get Entries Of A Particular Database

mysqlbinlog --database mdata mysqld-bin.000001 > crm-event_log.txt

## Disabling MySQL BinLogs For Recovery

Creation of a MySQL BinLog during a database recovery is highly undesirable as it creates an unending loop that will keep on restoring data infinitely and each restore process will further create a binary log.

Disabling the BinLogs is, therefore a must and this can be done using the -D option in the mysqlbinlog command.

mysqlbinlog -D mysqld-bin.000001
mysqlbinlog --disable-log-bin mysqld-bin.000001 


## Specific Entry Extraction In BinLogs

### First 5 entries
### from 123 GTID
```sh
mysqlbinlog -o 5 mysqld-bin.000001
mysqlbinlog -j 123 mysqld-bin.000002 > from-123.txt
mysqlbinlog --stop-position=219 mysqld-bin.000001 > upto-219.txt
```
# MySQL BinLog Retention
```sh
show variables like "expire_logs_days";
SET GLOBAL expire_logs_days = number_of_days;
mysqlbinlog -v --base64-output=DECODE-ROW bin.000057
```