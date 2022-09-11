module.exports = {
  routes: [
    {
     method: 'GET',
     path: '/get-energy-generation',
     handler: 'get-energy-generation.getData',
     config: {
       policies: [],
       middlewares: [],
     },
    },
  ],
};
