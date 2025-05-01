function slugify(text) {
  return text.toString().toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/\s+/g, '-')
    .replace(/[^\w\-]+/g, '')   
    .replace(/\-\-+/g, '-') 
    .replace(/^-+/, '')     
    .replace(/-+$/, ''); 
}

document.addEventListener("DOMContentLoaded", function () {
  const titleInput = document.getElementById("id_title");
  const slugInput = document.getElementById("id_slug");

  titleInput.addEventListener("input", function () {
    slugInput.value = slugify(titleInput.value);
  });
});
