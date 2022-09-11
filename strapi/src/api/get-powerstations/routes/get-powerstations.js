module.exports = {
  routes: [
    {
      method: 'GET',
      path: '/get-powerstations',
      handler: 'get-powerstations.getLayer',
      config: {
        policies: [],
        middlewares: [],
      },
     },
  ],
};
