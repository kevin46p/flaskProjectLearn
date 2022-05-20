new TypeIt("#pllzy", {
        loop: true,
        cursorSpeed: 1000,
        speed: 100
    })
    .type("PL && LZY")
    .pause(2000)
    .delete(null, {
        delay: 500
    })
    .type("崽崽，520快乐哦")
    .pause(3000)
    .go();

new TypeIt('#talkToLZY', {
    lifeLike: true,
    cursorSpeed: 1000,
    waitUntilVisible: true,
    speed: 100
}).go();