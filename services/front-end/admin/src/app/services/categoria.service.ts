import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Categoria } from '../interfaces/categoria';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {
  URL:string = "http://localhost:8080/Orders/categoria"
  constructor(private http:HttpClient) { 
  
  }
  obtenerCategorias():Observable<Categoria[]>{
    return this.http.get<Categoria[]>(this.URL);
  }
  enviarData(data:any):Observable<Categoria>{
    return this.http.post<Categoria>(this.URL,data);
  }
}
