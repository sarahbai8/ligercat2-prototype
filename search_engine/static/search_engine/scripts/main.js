function removeForm(element) {
  if (!element) {
    return;
  }
  var containerEl = element.parentElement,
    formEl = containerEl.parentElement;
  containerEl.remove();
  var newNumForms = getNumForms(formEl);
  if (newNumForms === 0) {
    hideFormset(formEl);
  }
  updateFormTotal(formEl, newNumForms);
}

function addForm(element) {
  if (!element) {
    return;
  }
  var formEl = document.querySelector(element.dataset.formSelector),
    emptyEl = document.querySelector(element.dataset.emptyFormSelector);
  var addingInput = element.parentElement.querySelector("input"),
    newForm = emptyEl.querySelector(".form__item").cloneNode(true),
    currNumForms = getNumForms(formEl);
  if (!addingInput.value) {
    return;
  }
  // update new form
  var newLabel = newForm.querySelector("label"),
    newInput = newForm.querySelector("input"),
    initialId = newLabel.getAttribute("for"),
    replacedId = initialId.replace("__prefix__", currNumForms); // zero-indexed so no need to add 1
  newLabel.setAttribute("for", replacedId);
  newInput.setAttribute("id", replacedId);
  newInput.value = addingInput.value;
  // insert new form + adjust display
  addingInput.value = "";
  formEl.appendChild(newForm);
  formEl.scrollTop = formEl.scrollHeight;
  updateFormTotal(formEl, currNumForms + 1); // one-indexed so need to add 1
  showFormset(formEl);
}

// Helpers
// -------

function getNumForms(form) {
  return form.querySelectorAll(".form__item").length;
}

function updateFormTotal(form, newTotal) {
  form.querySelector("[name=form-TOTAL_FORMS]").value = newTotal;
}

function hideFormset(form) {
  if (form) {
    form.style.display = "none";
  }
}

function showFormset(form) {
  if (form) {
    form.style.display = "block";
  }
}
