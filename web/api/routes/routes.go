package routes

import (
	"api/controllers"

	"github.com/gorilla/mux"
)

func SetupRoutes() *mux.Router {
	r := mux.NewRouter()

	// Route to translate function
	r.HandleFunc("/api/translate", controllers.HandleTranslationRequest).Methods("POST")

	return r
}
