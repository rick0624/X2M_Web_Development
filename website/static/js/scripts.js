/*!
 * Start Bootstrap - Business Frontpage v5.0.8 (https://startbootstrap.com/template/business-frontpage)
 * Copyright 2013-2022 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-frontpage/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project
// let p_html = document.querySelector("p").html();
let p_tag = document.querySelector("p");
let content = p_tag.innerText;
p_tag.remove();
console.log(content);
let div_tag = document.querySelector("div.newsContent");
// console.log(div_tag);
// content = "ddd";
div_tag.innerHTML = `${content}`;
