"""
Module: pdf_converter.py
Chuyển đổi file .docx sang file .pdf sử dụng Microsoft Word COM Automation trên Windows.
Đảm bảo độ phân giải cao nhất, giữ trọn vẹn bố cục và font chữ song ngữ.
"""

import os
import sys

def convert_docx_to_pdf(docx_path: str, pdf_path: str = None) -> str:
    """
    Chuyển đổi file .docx sang .pdf thông qua Microsoft Word.
    Trả về đường dẫn tuyệt đối của file PDF sinh ra.
    """
    abs_docx = os.path.abspath(docx_path)
    if not os.path.exists(abs_docx):
        raise FileNotFoundError(f"Không tìm thấy file docx: {abs_docx}")
    
    if pdf_path is None:
        abs_pdf = os.path.splitext(abs_docx)[0] + ".pdf"
    else:
        abs_pdf = os.path.abspath(pdf_path)

    # Đảm bảo thư mục đích tồn tại
    os.makedirs(os.path.dirname(abs_pdf), exist_ok=True)

    try:
        import win32com.client
    except ImportError:
        raise RuntimeError("Cần thư viện pywin32 để tự động xuất PDF qua Word. Hãy chạy: pip install pywin32")

    # wdFormatPDF hằng số chuẩn trong Word Object Model là 17
    WD_FORMAT_PDF = 17

    # Khởi tạo instance Word riêng biệt
    word = None
    doc = None
    try:
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = False

        doc = word.Documents.Open(abs_docx, ReadOnly=True)
        # Lưu định dạng PDF
        doc.SaveAs(abs_pdf, FileFormat=WD_FORMAT_PDF)
        return abs_pdf
    except Exception as e:
        raise RuntimeError(f"Lỗi khi chuyển đổi Word sang PDF: {e}")
    finally:
        if doc:
            try:
                doc.Close(SaveChanges=False)
            except Exception:
                pass
        if word:
            try:
                word.Quit()
            except Exception:
                pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sử dụng: python pdf_converter.py <duong_dan_file.docx> [duong_dan_file.pdf]")
        sys.exit(1)
    
    in_docx = sys.argv[1]
    out_pdf = sys.argv[2] if len(sys.argv) > 2 else None
    result = convert_docx_to_pdf(in_docx, out_pdf)
    print(f"Đã xuất thành công PDF: {result}")
