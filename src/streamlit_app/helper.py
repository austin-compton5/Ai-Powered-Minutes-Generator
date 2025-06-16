from weasyprint import HTML
import io 

def convert_html_to_pdf(html_string: str) -> bytes:
    pdf_io = io.BytesIO()
    HTML(string=html_string).write_pdf(target=pdf_io)
    return pdf_io.getvalue()