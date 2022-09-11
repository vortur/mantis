'use strict';

/**
 * A set of functions called "actions" for `get-energy-usage`
 */

module.exports = {
  getData: async (ctx, next) => {
    try {
      const site_id = 1
      const entries = await strapi.entityService.findMany('api::energy-usage.energy-usage');
      const formatted_data = []
      
      const rows = entries.filter((el=>parseInt(el.site_id) === site_id )).filter((el,i)=>(el.id%121 && i%2 && i%8 )).map((element,index)=>{
        return {x:element.to_time.replace('T',' ').replace('Z','').split('.')[0],y:element.energy }
      })

      formatted_data.push(
        {
          id:site_id,
          data:rows
        }
      )
       
      ctx.body = formatted_data
    } catch (err) {
      ctx.body = err;
    }
  }
};
