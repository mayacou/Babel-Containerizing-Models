package controllers

import (
	"api/models"
	"api/services"
	"encoding/json"
	"fmt"
	"net/http"
)

// HandleTranslationRequest handles both PDF and text input for translation
func HandleTranslationRequest(w http.ResponseWriter, r *http.Request) {
	// Decode the incoming request
	request, err := decodeTranslationRequest(r)
	if err != nil {
		http.Error(w, fmt.Sprintf("Invalid request: %s", err), http.StatusBadRequest)
		return
	}

	// Initialize services
	pdfService := services.PDFService{}
	translationService := services.TranslationService{}

	// Extract text from the PDF or use the provided text
	textToTranslate, err := extractTextForTranslation(request, pdfService)
	if err != nil {
		http.Error(w, fmt.Sprintf("Error extracting text: %s", err), http.StatusInternalServerError)
		return
	}

	// Translate the extracted or provided text
	translationResponse, err := translateText(textToTranslate, request.SourceLanguage, request.TargetLanguages, translationService)
	if err != nil {
		http.Error(w, fmt.Sprintf("Error translating text: %s", err), http.StatusInternalServerError)
		return
	}

	// Send the translated text back to the client
	sendTranslationResponse(w, translationResponse)
}

// decodeTranslationRequest decodes the incoming request body into a TranslationRequest model
func decodeTranslationRequest(r *http.Request) (models.TranslationRequest, error) {
	var request models.TranslationRequest
	if r.Header.Get("Content-Type") != "application/json" {
		return request, fmt.Errorf("expected application/json")
	}
	err := json.NewDecoder(r.Body).Decode(&request)
	return request, err
}

// extractTextForTranslation extracts the text from either a PDF or directly from the text provided
func extractTextForTranslation(request models.TranslationRequest, pdfService services.PDFService) (string, error) {
	if request.PDFFile != nil {
		// Extract text from the PDF
		textToTranslate, err := pdfService.ExtractTextFromPDF(string(request.PDFFile))
		if err != nil {
			return "", fmt.Errorf("failed to extract text from PDF: %w", err)
		}
		return textToTranslate, nil
	}

	// If it's a text request, use the text directly
	return request.SourceText, nil
}

// translateText uses the TranslationService to translate the text into specified target languages
func translateText(textToTranslate, sourceLanguage string, targetLanguages []string, translationService services.TranslationService) (models.Translation, error) {
	translationResponse, err := translationService.TranslateText(textToTranslate, sourceLanguage, targetLanguages)
	if err != nil {
		return models.Translation{}, fmt.Errorf("translation failed: %w", err)
	}
	return translationResponse, nil
}

// sendTranslationResponse sends the translation response back to the client
func sendTranslationResponse(w http.ResponseWriter, response models.Translation) {
	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(response); err != nil {
		http.Error(w, "Failed to send response", http.StatusInternalServerError)
	}
}
