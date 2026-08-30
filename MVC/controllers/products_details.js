const Product_detail = require("../models/products");

//for get all product details
const get_all_products = async (_req, res) => {
  try {
    const get_product = await Product_detail.find();
    if (!get_product || get_product.length === 0) {
      res.status(404).json({
        success: true,
        message: "Data not found",
      });
      return;
    }
    res.status(200).json({
      success: true,
      message: get_product,
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      message: err.message,
    });
  }
};

//post data in database
const create_product = async (req, res) => {
  try {
    const { title, description, price, category, stock, images, isAvailable } = req.body;
    const newproduct = new Product_detail({title, description, price, category, stock, images, isAvailable});
    console.log(newproduct);
    
    if (!newproduct){
      res.status(400).json({
        success:true,
        message:"Data not comming from interface"
      })
    }
    const product= await newproduct.save();
    res.status(201).json({
      success: true,
      message: product,
    });
  } catch (err) {
    res.status(400).json({
      success: false,
      message: err.message,
    });
  }
};

module.exports = {
  get_all_products,
  create_product,
};
