# Tài liệu Chẩn đoán & Xử lý Lỗi Kết nối IDEC HMI qua Nginx SSL Stream Proxy tới MQTT Broker

## 1. Mô hình Kiến trúc Hệ thống
- **Luồng kết nối:** `[IDEC HMI] --(TLS/SSL Port 8883)--> [Nginx Stream Proxy] --(TCP Port 1883 nội bộ)--> [MQTT Broker]`
- **Tên miền SSL:** `api-vending.doanhnghiep.com` (Sử dụng chứng chỉ Wildcard `*.doanhnghiep.com` do DigiCert cấp).

---

## 2. Tổng hợp các Lỗi Thường gặp & Giải pháp Chẩn đoán

### ❌ Lỗi 1: Tùy tiện nạp Client Key trên HMI khi Server chạy TLS 1 chiều (Server Authentication)
- **Hiện tượng:** Khi nạp Client Key vào HMI, kết nối bị từ chối hoặc đứt ngay lập tức.
- **Nguyên nhân:** Nginx chỉ cấu hình TLS 1 chiều (chỉ xác thực Server). Việc nạp Client Key khiến HMI ép luồng bắt tay sang Mutual TLS (mTLS 2 chiều), trong khi Nginx không phát tín hiệu `CertificateRequest` -> Xung đột TLS Handshake.
- **Khắc phục:** 
  - Phía HMI: Bỏ trống/tắt cấu hình Client Key & Client Certificate. Chỉ nạp duy nhất file **Root CA**.

---

### ❌ Lỗi 2: TLS Alert 48 (`tlsv1 alert unknown ca`)
- **Hiện tượng:** Log Nginx ghi nhận: `SSL_do_handshake() failed (SSL alert number 48: tlsv1 alert unknown ca)`.
- **Nguyên nhân:** HMI chủ động ngắt kết nối vì không thể đối chiếu/tin tưởng chuỗi chứng chỉ từ Server Nginx gửi sang.
  1. **Nginx dùng file Cert thiếu chuỗi (`doanhnghiep.com.pem`):** Chỉ chứa duy nhất Leaf Cert miền, thiếu Intermediate Cert (`RapidSSL`). Trình duyệt web có tính năng tự lên mạng tải Intermediate Cert (AIA Fetching), nhưng thiết bị nhúng (HMI) không có tính năng này.
  2. **HMI nạp sai phiên bản Root CA:** HMI nạp bản Root CA G1 cũ, trong khi chứng chỉ DigiCert hiện tại được ký bởi **`DigiCert Global Root G2`**.
- **Khắc phục:**
  - **Trên Nginx:** Khai báo file `fullchain.pem` chứa trọn bộ Leaf Cert + Intermediate Cert.
  - **Trên HMI:** Tải và nạp đúng file **`DigiCertGlobalRootG2.pem`** (Issuer: DigiCert Global Root G2).

---

### ❌ Lỗi 3: TLS Alert 42 (`sslv3 alert bad certificate`)
- **Hiện tượng:** Log Nginx ghi nhận: `SSL_do_handshake() failed (SSL alert number 42: sslv3 alert bad certificate)`.
- **Nguyên nhân:** HMI đánh giá chứng chỉ nhận được bị hỏng, rác hoặc không hợp lệ.
  1. **File Cert Nginx bị lẫn chứng chỉ rác:** File `fullchain.pem` bị nối dính chứng chỉ lạ (như ZeroSSL) ở cuối file, khiến parser của HMI đọc chuỗi bị lỗi.
  2. **Sai ngày giờ hệ thống (RTC) trên HMI (Rất phổ biến):** Đồng hồ nội bộ HMI bị reset về năm 1970/2000. Trong khi chứng chỉ có hiệu lực (2025–2026), HMI đối chiếu thấy thời gian hiện tại nằm ngoài khoảng hiệu lực -> Đánh giá chứng chỉ không hợp lệ.
- **Khắc phục:**
  - **Trên Nginx:** Làm sạch file Cert, loại bỏ các khối Cert rác không liên quan (`doanhnghiep_clean_chain.pem`).
  - **Trên HMI:** Thao tác trực tiếp trên màn hình HMI (giữ góc màn hình 3–5 giây vào `System Mode -> Maintenance -> Adjust Clock`) để cài lại đúng **Ngày/Tháng/Năm/Giờ** thực tế. Sau đó bấm **Download/Transfer Project** lại từ WindO/I-NV4 xuống HMI.

---

## 3. Quy trình Vận hành & Gia hạn SSL trong Tương lai

- **Hạn chứng chỉ tên miền:** Hết hạn sau 1–2 năm (Ví dụ: Oct 2026).
- **Hạn Root CA trên HMI:** `DigiCert Global Root G2` có thời hạn lên tới **25 năm (đến tận năm 2038 - 2045)**.

### 🔄 Quy trình khi Gia hạn SSL:
1. **Chỉ cần thao tác trên SERVER (Nginx):** Đổi file `.pem` và `.key` mới mua vào `/home/rd/SSL_RD/` và chạy `sudo nginx -s reload`.
2. **KHÔNG CẦN tác động vào HMI:** Tất cả HMI ngoài công trường vẫn giữ nguyên file `DigiCertGlobalRootG2.pem` và tự động tin tưởng chứng chỉ gia hạn mới mà không cần nạp lại phần mềm.

---

## 4. Tổng hợp các Script & Lệnh Linux Cần Thiết

### 🔍 4.1. Quét toàn bộ thông tin chứng chỉ trong thư mục
```bash
for f in /home/rd/SSL_RD/*; do
    echo "--------------------------------------------------"
    echo "📁 FILE: $f"
    echo "--------------------------------------------------"
    if [[ "$f" == *.pem ]] || [[ "$f" == *.crt ]]; then
        echo "📜 Thông tin chứng chỉ (Certificate):"
        openssl x509 -in "$f" -noout -subject -issuer -dates 2>/dev/null || echo "File chứa nhiều Cert hoặc không đúng định dạng X509"
    elif [[ "$f" == *.key ]]; then
        echo "🔑 Thông tin Private Key:"
        head -n 2 "$f"
    else
        echo "📄 Loại file khác:"
        file "$f"
    fi
    echo ""
done
```

### 🔗 4.2. Kiểm tra chuỗi chứng chỉ (Chain) trong file `.pem`
```bash
openssl crl2pkcs7 -nocrl -certfile /home/rd/SSL_RD/doanhnghiep_fullchain.pem | openssl pkcs7 -print_certs -noout -text | grep -E "(Subject:|Issuer:)"
```

### 📥 4.3. Tải trực tiếp file Root CA chuẩn `DigiCert Global Root G2`
```bash
curl -sS https://cacerts.digicert.com/DigiCertGlobalRootG2.crt.pem -o /home/rd/SSL_RD/DigiCertGlobalRootG2.pem
```

### 🧹 4.4. Script Python làm sạch file Cert (Lọc bỏ Cert rác ZeroSSL)
```bash
python3 -c '
with open("/home/rd/SSL_RD/doanhnghiep_fullchain.pem") as f:
    content = f.read()
parts = content.strip().split("-----END CERTIFICATE-----")
valid_certs = []
for p in parts:
    if "-----BEGIN CERTIFICATE-----" in p:
        cert = p.strip() + "\n-----END CERTIFICATE-----\n"
        if "ZeroSSL" not in cert:
            valid_certs.append(cert)
with open("/home/rd/SSL_RD/doanhnghiep_clean_chain.pem", "w") as f:
    f.write("".join(valid_certs[:2]))
'
```

### 🧪 4.5. Test giả lập kết nối SSL 8883 từ Client bằng OpenSSL
```bash
openssl s_client -connect api-vending.doanhnghiep.com:8883 -CAfile /home/rd/SSL_RD/DigiCertGlobalRootG2.pem
```

### 📜 4.6. Theo dõi Log Real-time trên Server Nginx
```bash
tail -f /var/log/nginx/stream_error.log /var/log/nginx/stream_access.log
```

### 🔄 4.7. Kiểm tra cú pháp & Reload Nginx
- Kiểm tra cú pháp Nginx
```bash
sudo nginx -t
```
- Reload Nginx
```bash
sudo nginx -s reload
```
