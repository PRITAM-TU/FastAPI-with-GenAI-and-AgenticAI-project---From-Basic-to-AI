const express = require("express");
const User_route = express.Router();
const User = require("../models/User.js");

User_route.get("/user", async (_req, res) => {
  try {
    const userdata = await User.find();

    if (!userdata || userdata.length === 0) {
      return res.status(404).json({
        success: false,
        message: "Data not found",
      });
    }

    return res.status(200).json({
      success: true,
      data: userdata,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
});

// post user data
User_route.post("/user", async (req, res) => {
  try {
    const { name, email, password } = req.body;
    console.log(name);

    // Create and save the new user using your schema rules
    const newUser = new User({
      name,
      email,
      password,
    });

    const savedUser = await newUser.save();

    return res.status(200).json({
      success: true,
      data: savedUser,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
});

//put user data 
User_route.put('/user/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email, password } = req.body;

    const updatedUser = await User.findByIdAndUpdate(
      id,
      { name, email, password },
      { new: true, runValidators: true }
    );

    if (!updatedUser) {
      return res.status(404).json({
        success: false,
        message: "User not found",
      });
    }

    return res.status(200).json({
      success: true,
      data: updatedUser,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
});

// delete user data based on id
User_route.delete('/user/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const deletedUser = await User.findByIdAndDelete(id);

    if (!deletedUser) {
      return res.status(404).json({
        success: false,
        message: 'User not found',
      });
    }

    return res.status(200).json({
      success: true,
      message: 'User deleted successfully',
      delete_data: deletedUser,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
});


module.exports = User_route;
