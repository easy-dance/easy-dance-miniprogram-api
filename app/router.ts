import { Application } from 'egg';

export default (app: Application) => {
  const { controller, router } = app;
  app.once('server', server => console.log(server));
  router.get('/', controller.home.index);
};
