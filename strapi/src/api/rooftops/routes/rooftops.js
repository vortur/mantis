module.exports = {
  routes: [
    {
     method: 'GET',
     path: '/rooftops',
     handler: 'rooftops.getLayer',
     config: {
       policies: [],
       middlewares: [],
     },
    },
  ],
};
