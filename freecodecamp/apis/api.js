var express = require('express');
var app = express();


app.use(function requestLog(req,res,next){
    let request = req.method + " " + req.path + " " + req.ip;
    console.log(request); 
    next();
})

app.get("/", (req, res) => res.sendFile(__dirname + "/views/index.html"));

app.get("/api/timestamp", (req, res) => {
    let time = new Date();
    res.json({unix:time.getTime(), utc:time.toUTCString()});
});

app.get("/api/timestamp/:timeIn", (req, res) => {
    let timeIn = req.params.timeIn;

    if(/\d{5,}/.test(timeIn)){
        let timeInt = parseInt(timeIn);
        let time = new Date(timeInt);
        res.json({unix:time.getTime(), utc:time.toUTCString()});
    }else{
        let time = new Date(timeIn);
        if(time.toString() === "Invalid Date"){
            res.json({error:"invalid Date"});
        }else{
            res.json({unix:time.getTime(), utc:time.toUTCString()});
        }        
    }
});

app.get("/api/whoami", (req,res) => res.json({ipaddress:req.ip,language:req.headers['accept-language'],software:req.headers['user-agent']}));