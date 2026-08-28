import express from 'express';
import route from './routes/admins.js';


const app = express();
app.use(express.json());
const PORT = 3000;



app.use('/api', route);
app.get('/', (_req, res) => {
    res.json({
        message: "This is root route "
    });
});


app.listen(PORT, () => {
    console.log(`The Backend server is running on port ${PORT}`);
});