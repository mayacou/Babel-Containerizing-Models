package services

import (
	"api/models"
	"bytes"
	"encoding/json"
	"fmt"
	"os/exec"
	"strings"
)

// TranslationService is a service for translating text
type TranslationService struct{}

// TranslateText sends a request to the translation API and returns the result
func (t *TranslationService) TranslateText(sourceText string, sourceLang string, targetLangs []string) (models.Translation, error) {
	// Prepare the Python script command
	cmdArgs := []string{
		"model_router.py",           // The Python script
		sourceText,                  // Source text
		sourceLang,                  // Source language
		strings.Join(targetLangs, " "), // Target languages as a space-separated string
	}

	// Execute the Python script
	cmd := exec.Command("python", cmdArgs...)
	cmd.Dir = "/path/to/your/python/script" // Set the working directory to where the script is located

	// Capture the output
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	if err != nil {
		return models.Translation{}, fmt.Errorf("failed to run Python script: %w", err)
	}

	// Decode the output into a list of translated texts
	var translatedTexts []models.TranslatedText
	if err := json.Unmarshal(out.Bytes(), &translatedTexts); err != nil {
		return models.Translation{}, fmt.Errorf("failed to decode translation response: %w", err)
	}

	// Return the full translation object
	translationResponse := models.Translation{
		SourceText:    sourceText,
		SourceLang:    sourceLang,
		TargetLangs:   targetLangs,
		TranslatedTexts: translatedTexts,
	}

	// Return the translation model
	return translationResponse, nil
}
