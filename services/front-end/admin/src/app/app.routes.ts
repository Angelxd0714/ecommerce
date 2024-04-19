import { Routes } from '@angular/router';
import { DashboardComponent } from './components/page/dashboard/dashboard.component';

export const routes: Routes = [
    { path: '', children: [ // Only one child route for now
    { path: 'admin', component: DashboardComponent }
  ]},
];
