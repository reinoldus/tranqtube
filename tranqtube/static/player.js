var options = {};

var player = videojs('my-video', options, function onPlayerReady() {
  videojs.log('Your player is ready!');

  // In this context, `this` is the player that was created by Video.js.
  this.play();

  this.playbackRate(1);

  // How about an event listener?
  this.on('ended', function() {
    videojs.log('Awww...over so soon?!');
  });

  this.on('pause', function( something ) {
      console.log(something);
  });



});