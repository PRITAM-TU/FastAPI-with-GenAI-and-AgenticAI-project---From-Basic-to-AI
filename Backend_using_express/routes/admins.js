const express = require('express');
const route = express.Router();

route.use(express.json());

const logging = (_req, _res, next) => {
  console.log('Logging the user');
  next();
};

const isStudent = (_req, _res, next) => {
  console.log('Student login');
  next();
};

const isAdmin = (_req, _res, next) => {
  console.log('Admin login');
  next();
};

route.get('/student', logging, isStudent, (_req, res) => {
  res.json({
    success: true,
    message: 'This is student route'
  });
});

route.get('/admin', logging, isAdmin, (_req, res) => {
  res.json({
    success: true,
    message: 'This is admin endpoint'
  });
});

module.exports = route;