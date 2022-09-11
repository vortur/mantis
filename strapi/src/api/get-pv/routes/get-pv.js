module.exports = {
  routes: [
    {
     method: 'GET',
     path: '/get-pv',
     handler: 'get-pv.getLayer',
     config: {
       policies: [],
       middlewares: [],
     },
    },
  ],
};
