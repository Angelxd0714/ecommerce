import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { user } from '../interfaces/login';
import { Token } from '../interfaces/token';
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private URL = "http://127.0.0.1:4000/login"
  constructor(private http: HttpClient) {

  }
  
  login(user: user) {
    return this.http.post<Token>(this.URL, user)
   
  }
}
