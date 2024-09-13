document.addEventListener('DOMContentLoaded', function () {
    const mainPhoto = document.getElementById('main-photo');
    const miniatureButtons = document.querySelectorAll('.miniature-btn');
  
    miniatureButtons.forEach(button => {
      button.addEventListener('click', function() {
        const newPhotoUrl = this.getAttribute('data-photo');
        mainPhoto.setAttribute('src', newPhotoUrl);
        document.querySelectorAll('.miniature-btn img').forEach(img => img.classList.remove('active'));
        this.querySelector('img').classList.add('active');
      });
    });
  });
  