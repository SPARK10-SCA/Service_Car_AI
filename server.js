const express = require('express');
const path = require('path')
const app = express();
const cors = require('cors')

app.set('port', 3000)

app.use(express.json());
app.use(cors());
app.use(express.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname, 'react-project/build')));
app.get('*', function (req, res) {
    res.sendFile(path.join(__dirname, '/react-project/build/index.html'));
});

app.listen(3000, () => {
    console.log("Server started on port", app.get('port'));
})