const express= require("express");

const app= express();


app.get("/",(req,res)=>{
    res.json({message:"Hello world form docker application "});
    
})


app.listen(8000,()=>{
    console.log("Docker app is running at 8000");
    
})