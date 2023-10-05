const dom= document.getElementById("totalBytes")

chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
    let current_url = tabs[0].url;
    let URL = "https://api.websitecarbon.com/site?url=";

    const data = {
        "url": current_url,
    };
    
    const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      };
    
    fetch(URL+current_url, requestOptions)
    .then(
        function(u) { return u.json(); }
    )
    .then(
        function (json) {
            //document.getElementById("totalBytes").innerHTML=JSON.stringify(json)
            test.innerHTML = "Energy consumed is " + json["statistics"]["energy"];
            let circularProgress = document.querySelector(".circular-progress"),
            progressValue = document.querySelector(".progress-value");

            var authenticity_score=Math.round(json["cleanerThan"]*100);

            let progressStartValue = 0,    
            progressEndValue = authenticity_score,      
            speed = 10;

            let progress = setInterval(() => {

            progressValue.textContent = `${progressStartValue}%`
            circularProgress.style.background = `conic-gradient(#febd69 ${progressStartValue * 3.6}deg, #ededed 0deg)`

            if(progressStartValue == progressEndValue){
                clearInterval(progress);
            }    
            progressStartValue++;
            }, speed);
        })
});


