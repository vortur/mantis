module.exports = {
  routes: [
    {
     method: 'GET',
     path: '/get-energy-usage',
     handler: 'get-energy-usage.getData',
     config: {
       policies: [],
       middlewares: [],
     },
    },
  ],
};
