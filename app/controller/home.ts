import { Controller } from 'egg';

export default class HomeController extends Controller {
  public async index() {
    const { ctx } = this;
    const { query } = ctx;
    this.logger.info(query.x);
    ctx.body = await ctx.service.test.sayHi('egg');
  }
}
