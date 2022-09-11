module.exports = {
  routes: [
    {
     method: 'GET',
     path: '/geoserver',
     handler: 'geoserver.getGeoserver',
     config: {
       policies: [],
       middlewares: [],
     },
    },
  ],
};
