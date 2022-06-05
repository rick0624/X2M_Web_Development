let edit_button = document.querySelector("button.edit");
edit_button.addEventListener("click", () => {
  let a_tag_edit = document.querySelectorAll("a.edit");
  let a_tag_remove = document.querySelectorAll("a.remove");
  for (let i = 0; i < a_tag_edit.length; i++) {
    a_tag_edit[i].style.display = "inline";
    a_tag_remove[i].style.display = "none";
  }
});

let remove_button = document.querySelector("button.remove");
remove_button.addEventListener("click", () => {
  let a_tag_remove = document.querySelectorAll("a.remove");
  let a_tag_edit = document.querySelectorAll("a.edit");
  for (let i = 0; i < a_tag_remove.length; i++) {
    a_tag_remove[i].style.display = "inline";
    a_tag_edit[i].style.display = "none";
  }
});

let alterPage_button = document.querySelector("button.pageAlter");
alterPage_button.addEventListener("click", (e) => {
  let form = document.querySelector("form");
  let page_input = document.querySelector("input.page");
  form.style.display = "block";
  page_input.style.display = "none";
});
