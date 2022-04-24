const express = require("express");
const app = express();
const bodyParser = require('body-parser')
const spawnSync = require("child_process").spawnSync;

app.set('view engine', 'pug');
app.set('views', './views')
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const port = 80;
const fs = require('fs')
app.get("/", (req, res) => {
    res.status(200).render('homepage.pug');
});


app.post("/submit", (req, res) => {
    console.log(req.body)
    let search=req.body.myName.toString();
    let limit=req.body.number.toString();
    //console.log(search)
    //console.log(limit)
    // let process = spawnSync('python3',["./starter.py",search,limit] );
    // let str1=process.output.toString();
    //console.log(str1)
    let data=fs.readFileSync('sample.json', 'utf8');
    let words=JSON.parse(data);
    //console.log(typeof(words))
    words=words.bbc
    //console.log(words)
    const params={'words':words};
    res.status(200).render('indi_res.pug',params);

});


app.listen(port, () => {
    console.log(`The application started successfully on port ${port}`);
});
