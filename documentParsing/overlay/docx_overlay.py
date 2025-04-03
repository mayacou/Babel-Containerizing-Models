from docx.shared import Inches
from io import BytesIO

def overlay_docx(doc, text_map, translated_texts, image_map):
   # === Step 5: Reinsert translated text ===
   for entry, translated in zip(text_map, translated_texts):
      if entry["type"] == "paragraph":
         para = doc.paragraphs[entry["index"]]
         for run in para.runs:
            run.clear()
         para.add_run(translated)

      elif entry["type"] == "table_cell":
         cell = doc.tables[entry["table_idx"]].rows[entry["row"]].cells[entry["col"]]
         para = cell.paragraphs[entry["para_idx"]]
         for run in para.runs:
            run.clear()
         para.add_run(translated)

      elif entry["type"] == "ocr_image":
         # Insert image and translated caption at end
         doc.add_paragraph()  # Spacing
         para = doc.add_paragraph()
         run = para.add_run()

         # Find corresponding image blob
         for img_entry in image_map:
            if img_entry["ocr_text"] == entry["ocr_text"]:
               image_stream = BytesIO(img_entry["image_blob"])
               run.add_picture(image_stream, width=Inches(4))  # Adjust size if needed
               break

         doc.add_paragraph(translated, style='Normal')
   return doc