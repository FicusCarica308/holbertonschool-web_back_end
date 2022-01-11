import express from 'express';
import { createClient, print } from 'redis';
const { promisify } = require("util");

const redisClient = createClient();

const app = express();
const port = 1245;

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

function getItemById(id) {
  for (const item of listProducts) {
    if (item.itemId === id) {
      return (item);
    }
  }
  return (false);
}

function reserveStockById(itemId, stock) {
  redisClient.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const clientGetPromise = promisify(redisClient.get).bind(redisClient);
  const stock = await clientGetPromise(`item.${itemId}`);
  return (stock);
}

app.get('/list_products', (req, res) => {
  res.send(listProducts);
});

app.get('/list_products/:itemId', (req, res) => { // FIXED
  const item = getItemById(Number(req.params.itemId));
  const reserveStock = getCurrentReservedStockById(req.params.itemId);
  if (item === false) {
    res.send({"status":"Product not found"})
  } else {
    reserveStock
    .then((reserved) => {
      console.log(typeof reserved);
      if (!reserved) {
        item.currentQuantity = 0;
        res.send(item);
      } else {
        item.currentQuantity = reserved;
        res.send(item);
      }
    });
  }
});

app.get('/reserve_product/:itemId', (req, res) => { // FIXED
  const item = getItemById(Number(req.params.itemId));
  const reserveStock = getCurrentReservedStockById(req.params.itemId);
  if (item === false) {
    res.send({"status":"Product not found"})
  } else {
    reserveStock
    .then((reserved) => {
      if (item.initialAvailableQuantity <= Number(reserved)) {
        res.send({"status":"Not enough stock available","itemId": item.itemId});
      } else {
        reserveStockById(item.itemId, Number(reserved) + 1);
        res.send({"status":"Reservation confirmed","itemId": item.itemId});
      }
    });
  }
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
