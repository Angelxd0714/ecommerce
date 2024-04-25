import { Component, Inject } from '@angular/core';
import { NavbarComponent } from "./navbar/navbar.component";
import { DrawComponent } from "./draw/draw.component";
import { ProductsComponent } from "../products/products.component";
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';


@Component({
    selector: 'app-dashboard',
    standalone: true,
    templateUrl: './dashboard.component.html',
    styleUrl: './dashboard.component.css',
    imports: [NavbarComponent, DrawComponent, ProductsComponent, RouterOutlet]
})
export class DashboardComponent {
    pageTitle: string = "Dashboard"


  
}
