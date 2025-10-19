from fastapi import APIRouter, UploadFile, File, HTTPException
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import io, docx
from pdf2image import convert_from_bytes

router = APIRouter(
    prefix="/api/v1/extract",
    tags=["Extract"]
)

@router.post("/")
async def extract_text(file: UploadFile = File(...)):
    filename = file.filename.lower()
    content = ""

    # PDF
    if filename.endswith(".pdf"):
        # Try PyPDF2 first
        reader = PdfReader(file.file)
        for page in reader.pages:
            text = page.extract_text() or ""
            content += text

        # If no text found, use OCR
        if not content.strip():
            file.file.seek(0)  # reset file pointer
            images = convert_from_bytes(await file.read())
            for img in images:
                content += pytesseract.image_to_string(img)

    # DOCX
    elif filename.endswith(".docx"):
        doc = docx.Document(file.file)
        for para in doc.paragraphs:
            content += para.text + "\n"

    # Images
    elif filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
        image = Image.open(file.file)
        content = pytesseract.image_to_string(image)

    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    return {"filename": file.filename, "text": content}
