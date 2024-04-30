import { Routes } from '@angular/router';
import { DashboardComponent } from './components/page/dashboard/dashboard.component';
import { ProductsComponent } from './components/page/products/products.component';
import { CategoriaComponent } from './components/page/categoria/categoria.component';
import { LoginComponent } from './components/login/login.component';

export const routes: Routes = [
  {
    path: '', children: [ // Only one child route for now
      {
        path: 'admin', component: DashboardComponent, children: [
          {
            path: 'productos', component: ProductsComponent, data: {
              title: 'Productos'
            }
          },
          {
            path:"Categoria", component:CategoriaComponent
          }
        ]
      }
    ], component:LoginComponent
  },
];
