const express = require("express");
const { get_all_products, create_product } = require("../controllers/products_details.js");

const product_route = express.Router();

product_route.get("/products", get_all_products);
product_route.post("/products", create_product);

module.exports = product_route;