// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const currentImage = document.getElementById('current');
    const thumbnails = document.querySelectorAll('.thumb');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            currentImage.src = this.src;
            // Usuń aktywne obramowanie ze wszystkich miniaturek
            thumbnails.forEach(thumb => thumb.style.border = '2px solid transparent');
            // Dodaj aktywne obramowanie do klikniętej miniaturki
            this.style.border = '2px solid #007bff';
        });
    });
});
