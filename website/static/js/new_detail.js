/*!
 * Start Bootstrap - Business Frontpage v5.0.8 (https://startbootstrap.com/template/business-frontpage)
 * Copyright 2013-2022 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-frontpage/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project

// let p_html = document.querySelector("p").html();
// app.use("/static/js", express.static("./static/js/"));
// console.log(555);
let p_tag = document.querySelector("p");
let content = p_tag.innerText;
p_tag.remove();
// console.log(content);
let div_tag = document.querySelector("div.newsContent");
// console.log(div_tag);
// content = "ddd";
div_tag.innerHTML = `${content}`;

let a_goBack = document.querySelector("a.goBack");
// console.log(a_goBack);
a_goBack.addEventListener("click", () => {
  //   console.log(555);
  let form = document.createElement("form");
  form.action = "";
  form.method = "GET";
  let input_page = document.createElement("input");
  input_page.type = "text";
  input_page.name = "page";
  input_page.value = 1;
  input_page.class = "page";
  let input_p = document.createElement("input");
  input_p.type = "text";
  input_p.name = "p";
  input_p.value = 3;
  input_p.class = "p";
  form.appendChild(input_page);
  form.appendChild(input_p);
  document.body.appendChild(form);
  form.submit();
  document.body.removeChild(form);
});

let a_remove_tag = document.querySelector("a.remove");
// console.log(a_remove_tag);
a_remove_tag.addEventListener("click", () => {
  let check = confirm("你確定要刪除嗎?");
  if (check) {
    // console.log(555);
    let hidden_remove = document.querySelector("input#remove");
    let url = $(hidden_remove).attr("data-url");
    document.location.href = url;
  }
});
