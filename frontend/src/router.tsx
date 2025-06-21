import { Route, Router, RootRoute } from '@tanstack/react-router';
import Home from './routes/Home';

const rootRoute = new RootRoute({
  component: () => <Home />,
});

const indexRoute = new Route({
  getParentRoute: () => rootRoute,
  path: '/',
  component: () => <Home />,
});

const routeTree = rootRoute.addChildren([indexRoute]);
export const router = new Router({ routeTree });
export type RouterType = typeof router;
