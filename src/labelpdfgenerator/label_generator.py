from __future__ import annotations

from io import BytesIO, StringIO
from tempfile import NamedTemporaryFile

from labelpdfgenerator.label_utils import PDFLabel
from labelpdfgenerator.models import LabelItem
from labelpdfgenerator.qrcode_generator import create_qrcode


def create_label_pdf(items: list[LabelItem], format="Avery-3422") -> StringIO:
    pdf = PDFLabel(format)
    pdf.add_page()
    for item in items:
        with NamedTemporaryFile(suffix=".png") as f:
            qr = create_qrcode(item.qrcode)
            qr.save(f, "PNG")
            pdf.add_label(item.serialize(), f.name)
    pdf.set_font("Arial", "B", 16)
    string_io = StringIO()
    string_io = pdf.output(dest="S").encode("latin-1")
    return string_io
