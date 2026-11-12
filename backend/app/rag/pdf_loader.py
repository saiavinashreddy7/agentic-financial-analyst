from pathlib import Path

import pymupdf

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB


class PDFProcessingError(Exception):
	"""Raised when a PDF cannot be processed."""

	pass


def extract_pdf_pages(file_path: str | Path) -> dict:
	"""
	Extract text from every page of a PDF.

	Returns document metadata and page-level text.
	"""
	path = Path(file_path)

	# 1. Check file existence
	if not path.exists():
		raise PDFProcessingError("PDF file does not exist.")

	# 2. Validate file extension
	if path.suffix.lower() != ".pdf":
		raise PDFProcessingError("Only PDF files are supported.")

	# 3. Check file size
	if path.stat().st_size > MAX_FILE_SIZE:
		raise PDFProcessingError("PDF exceeds the 50 MB limit.")

	pdf = pymupdf.open(path)

	# 4. Validate it is actually a PDF
	if not pdf.is_pdf:
		pdf.close()
		raise PDFProcessingError("File is not a valid PDF.")

	# 5. Reject encrypted documents
	if pdf.is_encrypted:
		pdf.close()
		raise PDFProcessingError("Encrypted PDFs are not supported.")

	pages_data = []
	total_characters = 0
	pages_with_text = 0

	for index, page in enumerate(pdf):
		text = page.get_text().strip()
		character_count = len(text)
		has_text = character_count > 0

		if has_text:
			pages_with_text += 1
		total_characters += character_count

		pages_data.append(
			{
				"page_number": index + 1,
				"text": text,
				"character_count": character_count,
				"has_text": has_text,
			}
		)

	pdf.close()

	return {
		"file_name": path.name,
		"total_pages": len(pages_data),
		"pages_with_text": pages_with_text,
		"total_characters": total_characters,
		"pages": pages_data,
	}
