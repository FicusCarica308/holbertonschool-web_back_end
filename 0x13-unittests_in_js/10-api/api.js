const express = require('express')

const app = express()
app.use(express.json());
const port = 7865;

app.get('/', function (req, res) {
  res.send('Welcome to the payment system')
});

app.get('/cart/:id', function (req, res) {
  if (!isNaN(Number(req.params.id))) {
    res.send(`Payment methods for cart ${req.params.id}`);
  } else {
    res.status(404).end();
  }
});

app.get('/available_payments', function (req, res) {
  res.send({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', function (req, res) {
  res.send(`Welcome ${req.body.userName}`);
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
