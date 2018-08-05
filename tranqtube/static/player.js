var options = {};

var x = $("#last_paused");
var y = $("#last_left");

$(window).on("unload", function(){
        let data = JSON.stringify({
            src: player.currentSrc(),
            time: player.currentTime()
        });
        console.log(data);

        $.ajax({
            type: "POST",
            url: "/leaving",
            data:  data,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            async: false
        });

        return "Bye";
});

x.on("click", function() {
    console.log(x.text());
    player.currentTime(x.text());
});

y.on("click", function() {
    console.log(y.text());
    player.currentTime(y.text());
});

var player = videojs('my-video', options, function onPlayerReady() {
    videojs.log('Your player is ready!');

    // In this context, `this` is the player that was created by Video.js.
    this.play();

    this.playbackRate(1);

    // How about an event listener?
    this.on('ended', function () {
        videojs.log('Awww...over so soon?!');
    });

    this.on('pause', function (something) {
        console.log(something);
        // $.post("/pause/" + player.currentTime(),);

        let data = JSON.stringify({
            src: player.currentSrc(),
            time: player.currentTime()
        });

        console.log(data);
        $.ajax({
            type: "POST",
            url: "/pause",
            data:  data,
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        });
    });

});

