
        const regionsAndCities = {
            "Astrakhan Oblast": ["Astrakhan", "Akhtubinsk", "Znamensk", "Kamyzyak"],
            "Bashkortostan": ["Ufa", "Sterlitamak", "Salavat", "Oktyabrsky"],
            "Chelyabinsk Oblast": ["Chelyabinsk", "Magnitogorsk", "Zlatoust", "Miass"],
            "Chita Oblast": ["Chita", "Borzya", "Krasnokamensk", "Sretensk"],
            "Irkutsk Oblast": ["Irkutsk", "Angarsk", "Usolye-Sibirskoye", "Shelekhov"],
            "Kaliningrad Oblast": ["Kaliningrad", "Baltiysk", "Svetlogorsk", "Pionersky"],
            "Kemerovo Oblast": ["Kemerovo", "Novokuznetsk", "Prokopyevsk", "Leninsk-Kuznetsky"],
            "Khabarovsk Krai": ["Khabarovsk", "Komsomolsk-on-Amur", "Sovetskaya Gavan", "Amursk"],
            "Kirov Oblast": ["Kirov", "Kirovo-Chepetsk", "Slobodskoy", "Omutninsk"],
            "Krasnodar Krai": ["Krasnodar", "Sochi", "Novorossiysk", "Anapa"],
            "Leningrad Oblast": ["Vyborg", "Luga", "Kingisepp", "Volkhov"],
            "Lipetsk Oblast": ["Lipetsk", "Yelets", "Zadonsk", "Lebedyan"],
            "Murmansk Oblast": ["Murmansk", "Apatity", "Severomorsk", "Kirovsk"],
            "Moscow": ["Moscow", "Krasnogorsk", "Podolsk", "Zelenograd"],
            "Novosibirsk Oblast": ["Novosibirsk", "Berdsk", "Iskitim", "Tatarsk"],
            "Omsk Oblast": ["Omsk", "Tara", "Isil'kul", "Kalachinsk"],
            "Penza Oblast": ["Penza", "Kuznetsk", "Zarechny", "Gorodishche"],
            "Rostov Oblast": ["Rostov-on-Don", "Taganrog", "Shakhty", "Novocherkassk"],
            "Samara Oblast": ["Samara", "Tolyatti", "Syzran", "Novokuybyshevsk"],
            "Sverdlovsk Oblast": ["Yekaterinburg", "Nizhny Tagil", "Kamensk-Uralsky", "Pervouralsk"],
            "Tatarstan": ["Kazan", "Naberezhnye Chelny", "Almetyevsk", "Zelenodolsk"],
            "Tomsk Oblast": ["Tomsk", "Seversk", "Strezhevoy", "Asino"],
            "Tver Oblast": ["Tver", "Rzhev", "Kashin", "Kalyazin"],
            "Tyumen Oblast": ["Tyumen", "Tobolsk", "Ishim", "Yalutorovsk"],
            "Vladimir Oblast": ["Vladimir", "Alexandrov", "Gus-Khrustalny", "Murom"],
            "Volgograd Oblast": ["Volgograd", "Volzhsky", "Kamyshin", "Mikhaylovka"],
            "Krasnoyarsk Krai": ["Krasnoyarsk", "Norilsk", "Achinsk", "Divnogorsk"],
            "Sakhalin": ["Yuzhno-Sakhalinsk", "Korsakov", "Nevelsk", "Poronaysk"],
            "St. Petersburg": ["St. Petersburg", "Kronstadt", "Peterhof", "Pushkin"],
            "Tula Oblast": ["Tula", "Novomoskovsk", "Alekseyevka", "Bogoroditsk"],

        };



        const regionSelect = document.getElementById("region");
    const citySelect = document.getElementById("city");
    const submitButton = document.getElementById("submit-button");

    // Заполнение всплывающего списка регионов.
    for (const region in regionsAndCities) {
        const option = document.createElement("option");
        option.value = region;
        option.textContent = region;
        regionSelect.appendChild(option);
    }

    regionSelect.addEventListener("change", function () {
        citySelect.innerHTML = '<option value="">Select a city</option>';

        // Получение выбранного региона.
        const selectedRegion = regionSelect.value;

        // Заполнение списка городов на основе выбранного региона.
        if (selectedRegion in regionsAndCities) {
            for (const city of regionsAndCities[selectedRegion]) {
                const option = document.createElement("option");
                option.value = city;
                option.textContent = city;
                citySelect.appendChild(option);
            }
        }
        checkSelection();
    });

    citySelect.addEventListener("change", checkSelection);

    function checkSelection() {
        // Проверяем, что регион и город не равны "Select a region" и "Select a city".
        if (regionSelect.value !== "" && citySelect.value !== "") {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    }

    // Изначально отключаем кнопку "Save".
    submitButton.disabled = true;