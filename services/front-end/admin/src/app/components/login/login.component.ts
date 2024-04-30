import { Component, Inject } from '@angular/core';
import { LoginService } from '../../services/login.service';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { user } from '../../interfaces/login';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, HttpClientModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
 private servicioLogin$= Inject(LoginService)
 login = new FormGroup({
  correo: new FormControl('', Validators.required),
  constrasena: new FormControl('', Validators.required)
 })
 onSubmit():void{
   if(!this.login.invalid){
     this.servicioLogin$.login(this.login.value).subscribe((data:user)=>{
       console.log(data)
     })
   }
  
 }
}
