var checkbox = document.getElementById('hamburgerCheckbox');

checkbox.addEventListener('change', function() {
  if (this.checked) {
    document.body.classList.add('no-scroll');
  } else {
    document.body.classList.remove('no-scroll');
  }
});