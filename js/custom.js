var canvas = new fabric.Canvas('c1');
canvas.isDrawingMode = true;
canvas.freeDrawingBrush.width = 5;
console.log(canvas);

var button = document.getElementById('btn-download');
button.addEventListener('click', function (e) {
    var dataURL = canvas.toDataURL('image/png');
    button.href = dataURL;
});