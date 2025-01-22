

const url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1';

fetch(url)
    .then(response => {
        return response.json();
    })
    .then(data => {
        const spots = [];
        const spotData = data.data.results;
        console.log(spotData);
        spotData.forEach(element => {
            let tempArr = element["filelist"].split("http");
            let imageUrl = "http" + tempArr[1];
            spots.push([element["stitle"], imageUrl]);
        });


        var secondSection = document.getElementById("second-section");

        for (let i = 0; i < 3; i++) {
            var node = document.createElement("div");
            var image = document.createElement("img");
            var spotName = document.createTextNode(spots[i][0]);

            image.src = spots[i][1];
            spotName.innerText = spots[i][0];

            node.className = "small-box";
            node.id = "promotion" + (Number(i) + 1);

            node.appendChild(image);
            node.appendChild(spotName);
            secondSection.appendChild(node);

        }

        let indexEnd = 13;

        for (let i = 3; i < indexEnd; i++) {
            var node = document.createElement("div");
            var image = document.createElement("img");
            var nameBox = document.createElement("div");
            var spotName = document.createElement("p");

            const number = (Number(i - 3) % 10) + 1

            spotName.innerText = spots[i][0];
            nameBox.className = "text-block";
            image.src = spots[i][1];
            node.className = "title" + number;
            node.classList.add("big-box");

            nameBox.appendChild(spotName);
            node.appendChild(image);
            node.appendChild(nameBox);
            secondSection.appendChild(node);


        }

        function showMore(startIndex, end) {
            var main = document.querySelector("#main");
            var section = document.createElement("div")

            for (let i = startIndex; i < end; i++) {
                var node = document.createElement("div");
                var image = document.createElement("img");
                var nameBox = document.createElement("div");
                var spotName = document.createElement("p");

                const number = (Number(i - 3) % 10) + 1

                spotName.innerText = spots[i][0];
                nameBox.className = "text-block";
                image.src = spots[i][1];
                node.className = "next" + number;
                node.classList.add("big-box");
                section.className = "section";

                nameBox.appendChild(spotName);
                node.appendChild(image);
                node.appendChild(nameBox);
                section.appendChild(node);
            }
            main.appendChild(section);
        }


        var burgerButton = document.querySelector(".nav-button");
        var closeButton = document.querySelector(".close-nav");
        var menu = document.querySelector(".menu");
        var word = document.querySelector("#first-section");
        var loadButton = document.querySelector("#load-button");


        burgerButton.addEventListener('click', function () {
            menu.classList.add("is-active");
            closeButton.classList.add("is-active");
        })


        closeButton.addEventListener('click', function () {
            menu.classList.remove("is-active");
            closeButton.classList.remove("is-active");
        })




        loadButton.addEventListener("click", function () {
            let remainData = spots.length - indexEnd;
            if (remainData >= 0 && remainData <= 10) {
                let startIndex = indexEnd;
                indexEnd = remainData;
                showMore(startIndex, indexEnd);
                loadButton.innerText = "資料到底";
                loadButton.disabled = true;
            }

            else if (remainData >= 10) {
                let startIndex = indexEnd;
                indexEnd += 10;
                showMore(startIndex, indexEnd);
                

            }
        });

    })
    .catch(error => {
        console.log(error);
    })




