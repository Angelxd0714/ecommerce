import { Component, Inject } from '@angular/core';
import { LoginService } from '../../services/login.service';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { user } from '../../interfaces/login';
import { Token } from '../../interfaces/token';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, HttpClientModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  constructor(private _loginService: LoginService){

  }
  login = new FormGroup({
    correo: new FormControl('', Validators.required),
    contrasena: new FormControl('', Validators.required)
  })
  onSubmit(e: any): void {
    e.preventDefault();
    let user = {
      correo: this.login.value.correo as string, // Assert `correo` is a string
      contrasena: this.login.value.contrasena as string // Assert `contrasena` is a string
    };
    console.log(user)
    this._loginService.login(user).subscribe((data: Token) => {
      console.log(data)
    })


  }
}
