$.getJSON("https://api.ipify.org?format=json", function (data) {
  //url format : https://example.com/counterIncrease/
    let url="<PASTE YOUR API URL HERE>" + data.ip;
    fetch(url).then((repo)=>repo.json()).then( (data) => {console.log(data)})
  //use the data variable to show contents on the webpage
  //Data variable format: 
  /*
  {
    "count": int,
    "location": {
        "city": "string",
        "country": "string",
        "ip": "string",
        "region": "string"
     }
  } 
  */
})   
