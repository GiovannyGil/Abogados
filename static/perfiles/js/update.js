    document.addEventListener("DOMContentLoaded", function () {
        const editProfileBtn = document.getElementById("edit-profile-btn");
        const profileOverviewTab = document.getElementById("profile-overview");
        const editProfileTab = document.getElementById("profile-edit");
        const editProfileForm = document.getElementById("edit-profile-form");

        editProfileBtn.addEventListener("click", function () {
            profileOverviewTab.style.display = "none";
            editProfileTab.style.display = "block";
        });

        editProfileForm.addEventListener("submit", function (e) {
            e.preventDefault();

            // Realizar la solicitud AJAX
            const formData = new FormData(editProfileForm);
            fetch(editProfileForm.getAttribute("action"), {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": formData.get("csrfmiddlewaretoken")
                }
            })
                .then(response => response.json())
                .then(data => {
                    // Manejar la respuesta del servidor y actualizar la información en la página
                    if (data.success) {
                        // Actualizar los elementos de la página con los nuevos datos
                        // Puedes mostrar un mensaje de éxito si lo deseas
                    } else {
                        // Manejar los errores si es necesario
                    }
                })
                .catch(error => {
                    console.error("Error en la solicitud AJAX: " + error);
                });
        });
    });
