import sys

from backend.app.rag.pdf_loader import extract_pdf_pages

if len(sys.argv) != 2:
	print("Usage: python -m backend.tests.test_pdf_loader <pdf_path>")
	raise SystemExit(1)

pdf_path = sys.argv[1]

try:
	result = extract_pdf_pages(pdf_path)
	print("\nPDF EXTRACTION SUCCESSFUL")
	print("-------------------------")
	print("File:", result["file_name"])
	print("Total pages:", result["total_pages"])
	print("Pages with text:", result["pages_with_text"])
	print("Total characters:", result["total_characters"])

	for page in result["pages"][:3]:
		print(f"\n--- Page {page['page_number']} ---")
		print("Characters:", page["character_count"])
		print("Text preview:", page["text"][:500])
except Exception as error:
	print("PDF EXTRACTION FAILED:", error)
