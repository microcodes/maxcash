var count = 3600 * 12;
var counter = setInterval(timer, 1000); //1000 will  run it every 1 second

function timer() {
    count = count - 1;
    if (count == -1) {
        clearInterval(counter);
        return;
    }

    var seconds = count % 60;
    var minutes = Math.floor(count / 60);
    var hours = Math.floor(minutes / 60);
    minutes %= 60;
    hours %= 60;

    document.getElementById("demo").innerHTML = hours + "h " + minutes + "m " + seconds + "s left"; // watch for spelling
}


/*<!DOCTYPE html>
<html>
<head>
<script>
  var counter = setInterval(timer, 1000);
  localStorage.limit = 3600 * 12;

  function timer() {
    localStorage.limit -= 1;
    if (localStorage.limit == -1) {
      clearInterval(counter);
      return;
    }

    var seconds = localStorage.limit % 60;
    var minutes = Math.floor(localStorage.limit / 60);
    var hours = Math.floor(minutes / 60);
    minutes %= 60;
    hours %= 60;

    document.getElementById("demo").innerHTML = hours + "h " + minutes + "m " + seconds + "s left";
  }

  function sendSignal() {
    $post({
        
    });
  }
</script>
</head>
<body>
  <div id="demo"></div>
</body>
</html>*/