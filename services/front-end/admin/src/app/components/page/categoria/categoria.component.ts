import { Component, Inject } from '@angular/core';
import { Observable } from 'rxjs';

import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { CategoriaService } from '../../../services/categoria.service';
import { Categoria } from '../../../interfaces/categoria';
import { HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-categoria',
  standalone: true,
  imports: [ReactiveFormsModule,CommonModule,HttpClientModule],
  templateUrl: './categoria.component.html',
  styleUrl: './categoria.component.css'
})
export class CategoriaComponent {
  listaCategorias:Categoria[] = [];

  categoria = new FormGroup({
  nombre: new FormControl('',Validators.required)
 })
 constructor(private servicio$:CategoriaService) {
  
 }
 ngOnInit(): void {
 
 }
 onSubmit() {
  if(this.categoria.invalid)
  this.servicio$.enviarData(this.categoria.value).subscribe((data:Categoria) => {
    console.log(data)
  })
}

 validarCampor():boolean{
  return this.categoria.invalid;
 }
}
