// TODO: Change path to pdf parsing script

package services

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
)

// PDFService is a service to handle PDF parsing
type PDFService struct{}

// ExtractTextFromPDF extracts text from a given PDF file path
func (p *PDFService) ExtractTextFromPDF(pdfPath string) (string, error) {
	// Run the Python script to extract text
	args := []string{"pdf_parser.py", pdfPath}
	cmd := exec.Command("python3", args...)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	// Capture the output from the Python script
	output, err := cmd.Output()
	if err != nil {
		return "", fmt.Errorf("failed to execute Python script: %w", err)
	}

	// Assuming the output is JSON that contains "extracted_text"
	var result map[string]string
	if err := json.Unmarshal(output, &result); err != nil {
		return "", fmt.Errorf("failed to parse Python script output: %w", err)
	}

	return result["extracted_text"], nil
}
