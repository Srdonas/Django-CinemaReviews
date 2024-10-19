document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".delete-movie");
    const confirmDeleteButton = document.getElementById("confirmDeleteButton");
    let movieIdToDelete = null;
    let tokenToDelete = null;

    // Open the modal when a delete button is clicked
    deleteButtons.forEach((button) => {
        button.addEventListener("click", () => {
            movieIdToDelete = button.getAttribute("data-id");
            tokenToDelete = button.getAttribute("data-token");

            const deleteModal = new bootstrap.Modal(
                document.getElementById("deleteConfirmationModal")
            );
            deleteModal.show();
        });
    });

    // Confirm the deletion and make the fetch request
    confirmDeleteButton.addEventListener("click", async () => {
        if (movieIdToDelete) {
            try {
                const response = await fetch(`/movie/${movieIdToDelete}/delete/`, {
                    method: "DELETE",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": tokenToDelete,
                    },
                });

                if (response.ok) {
                    // Remove the movie card from the DOM
                    document.getElementById(`movie-card-${movieIdToDelete}`).remove();

                    // Show the success toast
                    const toastElement = document.getElementById("successToast");
                    const toast = new bootstrap.Toast(toastElement);
                    toast.show();
                } else {
                    const errorData = await response.json();
                    alert(`Error: ${errorData.message || "Failed to delete movie."}`);
                }
            } catch (error) {
                console.error("Error:", error);
                alert("An error occurred while deleting the movie.");
            }
        }

        // Hide the modal after deletion attempt
        const deleteModal = bootstrap.Modal.getInstance(
            document.getElementById("deleteConfirmationModal")
        );
        deleteModal.hide();
    });
});
