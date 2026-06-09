# PostgreSQL Backup & Restore Guide

## Mục lục

1. Kiểm tra đang kết nối vào đâu
2. Kiểm tra database có dữ liệu không
3. Xem danh sách database
4. Backup database
5. Kiểm tra file backup
6. Restore database
7. Kiểm tra sau restore
8. Các cạm bẫy thường gặp
9. Bộ lệnh điều tra nhanh
10. Checklist trước khi backup

---

# 1. Kiểm tra đang kết nối vào đâu

Trước khi backup hoặc restore, luôn kiểm tra chính xác:

* PostgreSQL version
* Data directory
* Port
* Database hiện tại

```sql
SELECT version();

SHOW data_directory;

SHOW port;

SELECT current_database();
```

Ví dụ:

```text
PostgreSQL 12.16
C:/Program Files/PostgreSQL/12/data
5432
reportdb
```

---

# 2. Kiểm tra database có dữ liệu không

## Xem danh sách bảng

```sql
\dt
```

Hoặc:

```sql
SELECT schemaname,
       tablename
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema');
```

## Đếm số lượng bảng

```sql
SELECT count(*)
FROM information_schema.tables
WHERE table_schema = 'public';
```

## Xem schema hiện có

```sql
\dn
```

---

# 3. Xem danh sách database

```sql
\l
```

Hoặc:

```sql
SELECT datname
FROM pg_database
ORDER BY datname;
```

Ví dụ:

```text
PRODUCTION231222
postgres
reportdb
template0
template1
```

---

# 4. Backup Database

## Backup dạng Custom (.dump)

Khuyến nghị sử dụng định dạng Custom để dễ restore.

```powershell
& "C:\Program Files\PostgreSQL\18\bin\pg_dump.exe" `
-U postgres `
-h localhost `
-p 5432 `
-F c `
-b `
-v `
-f "D:\reportdb.dump" `
reportdb
```

### Ý nghĩa tham số

| Tham số | Ý nghĩa               |
| ------- | --------------------- |
| -F c    | Custom Format         |
| -b      | Bao gồm Large Objects |
| -v      | Hiển thị log chi tiết |
| -f      | File output           |

---

# 5. Kiểm tra file backup

Sau khi backup, luôn kiểm tra nội dung file dump:

```powershell
& "C:\Program Files\PostgreSQL\18\bin\pg_restore.exe" `
-l "D:\reportdb.dump"
```

## Backup đúng

Ví dụ:

```text
TABLE public.users
TABLE DATA public.users
SEQUENCE public.users_id_seq
INDEX public.pk_users
```

## Backup sai hoặc database trống

Ví dụ:

```text
SCHEMA public
ACL public
```

Nếu chỉ có SCHEMA và ACL thì database nguồn gần như không có dữ liệu.

---

# 6. Restore Database

## Tạo database trước

```sql
CREATE DATABASE reportdb;
```

## Restore

```powershell
& "C:\Program Files\PostgreSQL\18\bin\pg_restore.exe" `
-U postgres `
-h localhost `
-p 5432 `
-d reportdb `
-v `
"D:\reportdb.dump"
```

---

# 7. Kiểm tra sau restore

Đăng nhập:

```powershell
psql -U postgres -d reportdb
```

## Xem bảng

```sql
\dt
```

## Đếm số lượng bảng

```sql
SELECT count(*)
FROM information_schema.tables
WHERE table_schema = 'public';
```

## Kiểm tra dữ liệu

```sql
SELECT count(*)
FROM ten_bang;
```

---

# 8. Các cạm bẫy thường gặp

## 8.1 Cùng tên database nhưng khác server

Ví dụ:

```text
localhost:5432/reportdb
localhost:5433/reportdb
```

Tên database giống nhau nhưng dữ liệu khác nhau.

Luôn kiểm tra:

```sql
SHOW port;
SHOW data_directory;
```

---

## 8.2 Nhiều PostgreSQL trên cùng máy

Ví dụ:

```text
PostgreSQL 12
PostgreSQL 18
```

Kiểm tra service:

```powershell
Get-Service *postgres*
```

Hoặc:

```powershell
sc query type= service | findstr /I postgres
```

---

## 8.3 pgAdmin Server không phải PostgreSQL Server

Trong pgAdmin:

```text
Servers
 └─ dev
```

`dev` chỉ là một Connection Profile.

Không phải Database.

Không phải PostgreSQL Instance.

---

## 8.4 Backup thành công nhưng file dump rỗng

Dấu hiệu:

```text
SCHEMA public
ACL public
```

Nguyên nhân:

* Backup nhầm database
* Backup nhầm port
* Backup nhầm PostgreSQL instance
* Database thực sự không có dữ liệu

---

# 9. Bộ lệnh điều tra nhanh

## Xem phiên bản PostgreSQL

```sql
SELECT version();
```

## Xem port

```sql
SHOW port;
```

## Xem thư mục dữ liệu

```sql
SHOW data_directory;
```

## Xem database hiện tại

```sql
SELECT current_database();
```

## Xem danh sách bảng

```sql
\dt
```

## Xem schema

```sql
\dn
```

## Xem tất cả database

```sql
\l
```

## Xem dung lượng database

```sql
SELECT pg_size_pretty(
    pg_database_size(current_database())
);
```

## Xem địa chỉ server

```sql
SELECT inet_server_addr(),
       inet_server_port();
```

---

# 10. Checklist trước khi backup

## Kiểm tra môi trường

* [ ] Đúng PostgreSQL Instance
* [ ] Đúng Port
* [ ] Đúng Database
* [ ] Đúng Data Directory

## Kiểm tra dữ liệu

* [ ] `\dt` thấy đủ bảng
* [ ] Kiểm tra số lượng bảng
* [ ] Kiểm tra dữ liệu mẫu

## Kiểm tra file dump

* [ ] Backup thành công
* [ ] Chạy `pg_restore -l`
* [ ] Thấy TABLE
* [ ] Thấy TABLE DATA
* [ ] Thấy INDEX
* [ ] Thấy SEQUENCE

## Kiểm tra restore

* [ ] Restore không báo lỗi
* [ ] `\dt` thấy đủ bảng
* [ ] Kiểm tra số lượng record

---

# Bài học quan trọng

Không nên chỉ nhìn tên database.

Luôn xác minh:

```sql
SHOW port;

SHOW data_directory;
```

Hai lệnh này giúp xác định chính xác PostgreSQL Instance đang được sử dụng và tránh backup hoặc restore nhầm hệ thống.
