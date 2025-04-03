
def parse_docx(doc, text_map):
   # === Step 1: Collect paragraphs ===
   for idx, para in enumerate(doc.paragraphs):
      if para.text.strip():
         text_map.append({
            "type": "paragraph",
            "index": idx,
            "text": para.text
         })

   # === Step 2: Collect table cell text ===
   for table_idx, table in enumerate(doc.tables):
      for row_idx, row in enumerate(table.rows):
         for col_idx, cell in enumerate(row.cells):
            for para_idx, para in enumerate(cell.paragraphs):
               if para.text.strip():
                  text_map.append({
                     "type": "table_cell",
                     "table_idx": table_idx,
                     "row": row_idx,
                     "col": col_idx,
                     "para_idx": para_idx,
                     "text": para.text
                  })
   
   return text_map