module.exports = {
  routes: [
    {
     method: 'GET',
     path: '/get-field',
     handler: 'get-field.getLayer',
     config: {
       policies: [],
       middlewares: [],
     },
    },
  ],
};
