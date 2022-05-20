var swiper = new Swiper('.swiper-container-lovelzy1', {
    pagination: '.swiper-pagination-lovelzy1',
    paginationClickable: true,
    spaceBetween: 30,
});

var swiper = new Swiper('.swiper-container-lovelzy2', {
    pagination: '.swiper-pagination-lovelzy2',
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    coverflow: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true
    }
});

var swiper = new Swiper('.swiper-container-lovelzy3', {
    pagination: '.swiper-pagination-lovelzy3',
    effect: 'flip',
    grabCursor: true,
    nextButton: '.swiper-button-next-lovelzy3',
    prevButton: '.swiper-button-prev-lovelzy3'
});