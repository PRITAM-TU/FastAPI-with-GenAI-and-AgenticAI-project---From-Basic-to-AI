const express=require("express");
const route=express.Router()
const User = require("../models/User.js");



route.get('/user', async (_req, res) => {
    try {
        const userdata = await User.find();

        if (!userdata || userdata.length === 0) {
            return res.status(404).json({
                success: false,
                message: "Data not found"
            });
        }

        return res.status(200).json({
            success: true,
            data: userdata
        });
    } catch (error) {
        return res.status(500).json({
            success: false,
            message: error.message
        });
    }
});

module.exports = route;
