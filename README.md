﻿# App_canh_bao_py
Cơ chế:
- Check các link được định nghĩa từ trước trên list danh_sach
- Mỗi link sẽ khởi tạo 1 luồng check (Check vô hạn). Nếu trả về mã lỗi (HTTP ERROR CODE) != 200 thì sẽ thực hiện hành động insert dữ liệu vào DB.
- USB 3G được cắm trên máy chủ, trên máy chủ đó có app SMS_Auto kết nối với USB qua COM
- SMS_Auto scan DB liên tục, nếu có bản ghi mới sẽ tự động kết nối cổng COM để gửi SMS
