document.getElementById('profile-pic-input').addEventListener('change', function (e) {
  const file = e.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      document.getElementById('profile-pic').src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
});