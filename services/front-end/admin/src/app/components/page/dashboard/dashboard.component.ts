import { Component } from '@angular/core';
import { NavbarComponent } from "./navbar/navbar.component";
import { DrawComponent } from "./draw/draw.component";

@Component({
    selector: 'app-dashboard',
    standalone: true,
    templateUrl: './dashboard.component.html',
    styleUrl: './dashboard.component.css',
    imports: [NavbarComponent, DrawComponent]
})
export class DashboardComponent {

}
