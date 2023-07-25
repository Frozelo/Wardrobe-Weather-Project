$(document).ready(function() {
    $("#search-form").submit(function(event) {
        event.preventDefault();
        var city = $("#city-input").val();
        fetchWeather(city);
    });
});

function fetchWeather(city) {
    var weatherInfo = $("#weather-info");
    weatherInfo.html("Загрузка...");

    $.ajax({
        url: "",
        type: "POST",
        data: {
            city: city,
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
        },
        dataType: "json",
        success: function(response) {
            // Очищаем содержимое элемента weatherInfo
            weatherInfo.empty();

            if (response.error) {
                weatherInfo.html("Ошибка: " + response.error);
            } else {
                // Отображаем информацию о погоде
                weatherInfo.html("Город: " + response.city + "<br>");
                // и так далее - добавьте нужные поля из полученного JSON-ответа
            }
        },
        error: function() {
            weatherInfo.html("Ошибка при получении данных о погоде.");
        }
    });
}
