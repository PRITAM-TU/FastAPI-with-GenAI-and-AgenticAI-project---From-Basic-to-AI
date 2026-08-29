const mongoose =require("mongoose");
const {model,Schema}=mongoose;

// Ensure Schema is capitalized
const ProductSchema = new Schema(
  {
    title: {
      type: String,
      required: [true, "Product title is required"],
      trim: true,
      index: true
    },
    description: {
      type: String,
      required: [true, "Product description is required"],
      trim: true
    },
    price: {
      type: Number,
      required: [true, "Product price is required"],
      min: [0, "Price cannot be negative"]
    },
    category: {
      type: String,
      required: [true, "Category is required"],
      lowercase: true,
      trim: true
    },
    stock: {
      type: Number,
      required: [true, "Stock count is required"],
      min: [0, "Stock cannot be negative"],
      default: 0
    },
    images: {
      type: [String], // Array of image URLs
      default: []
    },
    isAvailable: {
      type: Boolean,
      default: true
    }
  },
  {
    timestamps: true, // Automatically manages createdAt and updatedAt
    versionKey: false // Removes the "__v" field automatically
  }
);

// Exports the model. Collection name will automatically be "product_details"
module.exports =model("Product_detail", ProductSchema);
