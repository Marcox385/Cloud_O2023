// IS727272 - Server code
// Modules
const path = require('path');
const dotenv = require('dotenv');
const express = require('express');
const bodyParser = require('body-parser')
const { engine } = require('express-handlebars');

// Environment variables loading
dotenv.config();

// Server
const app = express();
const port = process.env.PORT || 3000;

// Render engine
app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set('views', './views');

// Static files
const assetsUrl = path.join(__dirname, 'public');
app.use('/assets', express.static(assetsUrl));

// Parse request correctly
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.get('', (req, res) => {
    const url = path.join(__dirname, 'public', 'index.html');
    res.sendFile(url);
});

app.get('/about', (req, res) => {
    const url = path.join(__dirname, 'public', 'about.html');
    res.sendFile(url);
});

app.post('/short-url', (req, res) => {
    console.log(req.body);
    
    res.status(200).render('url_result', {
        short_url: req.body.url
    });
});

// Run server
app.listen(port, () => {
    console.log(`App running on port ${port}`);
});
