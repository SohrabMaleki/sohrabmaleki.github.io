(() => {
    const lightbox = document.getElementById('lightbox');
    if (!lightbox) return;
    const image = document.getElementById('lightbox-img');
    const closeButton = lightbox.querySelector('.close-lightbox');
    let previousFocus;
    let previousOverflow;
    function openLightbox(link) {
        previousFocus = link;
        previousOverflow = document.body.style.overflow;
        image.src = link.href;
        image.alt = link.querySelector('img').alt;
        lightbox.hidden = false;
        document.body.style.overflow = 'hidden';
        closeButton.focus();
    }
    function closeLightbox() {
        lightbox.hidden = true;
        image.removeAttribute('src');
        document.body.style.overflow = previousOverflow || '';
        if (previousFocus) previousFocus.focus();
    }
    document.querySelectorAll('[data-poster]').forEach(link => {
        link.addEventListener('click', event => { event.preventDefault(); openLightbox(link); });
    });
    closeButton.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', event => { if (event.target === lightbox) closeLightbox(); });
    document.addEventListener('keydown', event => {
        if (lightbox.hidden) return;
        if (event.key === 'Escape') closeLightbox();
        if (event.key === 'Tab') { event.preventDefault(); closeButton.focus(); }
    });
})();
