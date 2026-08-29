const mongoose = require("mongoose");

// Connection URI
// Note: Use '127.0.0.1' instead of 'localhost' to prevent connection issues in Node 18+
const mongoURI = 'mongodb://127.0.0.1:27017/Users';

// Export the function so you can call it after server start
const connectDB = async () => {
  try {
    await mongoose.connect(mongoURI);
    console.log('✅ MongoDB connected successfully!');
  } catch (err) {
    console.error('❌ MongoDB connection error:', err);
    process.exit(1);
  }
};

module.exports = connectDB;
