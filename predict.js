$("#image-selector").change(function () {
    let reader = new FileReader();
    reader.onload = function () {
        let dataURL = reader.result;
        $("#selected-image").attr("src", dataURL);
        $("#prediction-list").empty();
    }
    let file = $("#image-selector").prop("files")[0];
    reader.readAsDataURL(file);
}); 
let model;
(async function () {
    model = await tf.loadModel("C:/Users/robot/projectJs/TensorFlowJs/static/tfjs-models/VGG16.h5");
    console.log("hello")
    $(".progress-bar").hide();
    let image = $("#selected-image").get(0);
    let predictions = await model.predict(tf.browser.fromPixels(image)
        .resizeNearestNeighbour([224,224])
        .toFloat()
        .expandDims()).data();
    let top5 = Array.from(predictions)
        .map(function (p, i) {
            return {
                probability: p,
                className: IMAGENET_CLASSES[i]
            };
        }).sort(function (a, b) {
            return b.probability - a.probability;
        }).slice(0, 5);
    $("#prediction-list").empty();
    top5.forEach(function (p) {
        $("#prediction-list").append(`<li>${p.className}: ${p.probability.toFixed(6)}</li>`);
    });
});