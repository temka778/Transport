function openModal(url) {
  const modalContent = document.getElementById("modal-content");
  modalContent.innerHTML = `
    <div class="text-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Загрузка...</span>
      </div>
    </div>`;
  
  fetch(url, { headers: { "X-Requested-With": "XMLHttpRequest" } })
    .then(response => {
      if (!response.ok) throw new Error("Ошибка загрузки формы.");
      return response.text();
    })
    .then(html => {
      modalContent.innerHTML = html;
      const form = modalContent.querySelector("form");
      if (form) initializeFormHandler(form);
    })
    .catch(error => {
      console.error("Ошибка:", error);
      modalContent.innerHTML = `<p class="text-danger">Ошибка загрузки формы. Попробуйте позже.</p>`;
    });

  const modal = new bootstrap.Modal(document.getElementById("universalModal"));
  modal.show();
}

function initializeFormHandler(form) {
  form.addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    fetch(form.action, {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
    .then(response => {
      if (!response.ok) throw new Error("Не удалось выполнить запрос. Проверьте данные или повторите позже.");
      return response.json();
    })
    .then(data => {
      if (data.redirect_url) {
        window.location.href = data.redirect_url;
      } else {
        displayFormError(form, "Произошла ошибка. Попробуйте позже.");
      }
    })
    .catch(error => {
      console.error("Ошибка:", error);
      displayFormError(form, "Проверьте корректность дат начала и завершения аренды!");
    });
  });
}

function displayFormError(form, message) {
  const errorDiv = document.createElement("div");
  errorDiv.classList.add("alert", "alert-danger", "mt-3");
  errorDiv.textContent = message;
  if (!form.querySelector(".alert")) form.prepend(errorDiv);
}