var counter = 0;
var counterButton = document.createElement("Button");

counterButton.setAttribute("id", "btn");
counterButton.setAttribute("class", "btnClass");
counterButton.innerHTML = counter;
counterButton.onclick = function() {
                counter ++;
                counterButton.innerHTML = counter;
            };
document.body.appendChild(counterButton);