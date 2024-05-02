import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { user } from '../interfaces/login';
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private URL = "http://localhost:6000/login"
  constructor(private http:HttpClient) { 

  }
  login(user:user){
   const valor= this.http.post<user>(this.URL,user);
   return valor
  }
}
