const express =require("express")
const  connectDB=require("./db.js");
const {route}= require("./routes/userRoute.js");

const PORT=3000;
const app=express();
app.use(express.json());



connectDB()

app.get('/',async(_req,res)=>{
    res.status(200).json({
        message:"This endpoint for this project "
    });
});
app.use('/api',route)

app.listen(PORT,()=>{
    console.log(`The Backend ser is running on PORT ${PORT}`);
    
});