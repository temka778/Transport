const mainPhoto = document.getElementById('main-photo');
const miniatureCarousel = document.querySelector('.miniature-carousel');
const miniatures = document.querySelectorAll('.miniature-btn img');
const prevPhotoBtn = document.getElementById('prev-photo');
const nextPhotoBtn = document.getElementById('next-photo');

let currentPhotoIndex = 0;  // Индекс текущего фото

// Функция для смены главного фото
function setMainPhoto(url, index) {
  mainPhoto.src = url;
  currentPhotoIndex = index;
  centerMiniature();
}

// Обработчик кликов по миниатюрам
miniatures.forEach((miniature, index) => {
  miniature.addEventListener('click', function() {
    setMainPhoto(this.getAttribute('src'), index);
  });
});

// Функция для центрирования активной миниатюры
function centerMiniature() {
  const activeMiniature = miniatures[currentPhotoIndex];
  const miniatureCarouselWidth = miniatureCarousel.offsetWidth;
  const miniatureWidth = activeMiniature.offsetWidth;
  const offset = (miniatureCarouselWidth / 2) - (miniatureWidth / 2);
  miniatureCarousel.scrollTo({
    left: activeMiniature.offsetLeft - offset,
    behavior: 'smooth'
  });
}

// Обработчики для навигации по основным фото
nextPhotoBtn.addEventListener('click', function() {
  if (currentPhotoIndex < miniatures.length - 1) {
    currentPhotoIndex++;
  } else {
    currentPhotoIndex = 0;
  }
  setMainPhoto(miniatures[currentPhotoIndex].getAttribute('src'), currentPhotoIndex);
});

prevPhotoBtn.addEventListener('click', function() {
  if (currentPhotoIndex > 0) {
    currentPhotoIndex--;
  } else {
    currentPhotoIndex = miniatures.length - 1;
  }
  setMainPhoto(miniatures[currentPhotoIndex].getAttribute('src'), currentPhotoIndex);
});


// Свайп для основного фото
let startX = 0;
let endX = 0;

function handleSwipe() {
  if (endX < startX) {
    // Свайп влево (следующее фото)
    nextPhotoBtn.click();
  } else if (endX > startX) {
    // Свайп вправо (предыдущее фото)
    prevPhotoBtn.click();
  }
}

// Обработчики для свайпа на основном фото
mainPhoto.addEventListener('touchstart', (e) => {
  startX = e.touches[0].clientX;
});

mainPhoto.addEventListener('touchend', (e) => {
  endX = e.changedTouches[0].clientX;
  handleSwipe();
});

// Свайп для карусели миниатюр
let startScrollX = 0;
let isSwiping = false;

miniatureCarousel.addEventListener('touchstart', (e) => {
  startX = e.touches[0].clientX;
  startScrollX = miniatureCarousel.scrollLeft;
  isSwiping = true;
});

miniatureCarousel.addEventListener('touchmove', (e) => {
  if (!isSwiping) return;
  const moveX = e.touches[0].clientX - startX;
  miniatureCarousel.scrollLeft = startScrollX - moveX;
});

miniatureCarousel.addEventListener('touchend', () => {
  isSwiping = false;

  // Добавляем инерцию на основании скорости
  const momentumScroll = setInterval(() => {
    if (Math.abs(velocity) < 0.1) {
      clearInterval(momentumScroll);  // Останавливаем инерцию, если скорость слишком мала
    } else {
      miniatureCarousel.scrollLeft -= velocity;  // Продолжаем прокрутку
      velocity *= 0.25;  // Постепенно замедляем прокрутку
    }
  }, 400);  // 400 кадров в секунду (2.5 миллисекунд на кадр)
});