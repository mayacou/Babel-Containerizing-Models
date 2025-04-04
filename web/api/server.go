package main

import (
	"api/routes"
	"fmt"
	"net/http"
)
const PORT = ":3000"

func main() {
	r := routes.SetupRoutes()

	// Start the server
	fmt.Println("Starting server on ", PORT)
	if err := http.ListenAndServe(PORT, r); err != nil {
		fmt.Printf("Error starting server: %v\n", err)
	}
}
