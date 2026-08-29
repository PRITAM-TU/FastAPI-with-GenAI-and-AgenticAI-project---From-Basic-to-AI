const express=require("express");
const dotenv=require("dotenv");
const connectDB=require("./config/db.js");
const product_route=require("./routes/product_rotues.js")
dotenv.config()


const app=express();
app.use(express.json());

connectDB()
app.get('/',(req,res)=>{
    res.status(200).json({
        succes:true,
        message:"Root Endpoints.................."
    });


});
app.use('/api',product_route)

app.listen(process.env.PORT,()=>{
    console.log(`The application running on port ${process.env.PORT}`);
});