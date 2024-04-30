import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Categoria } from '../interfaces/categoria';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {
  eliminarCategoria(id: number) {
    return this.http.delete<Categoria>(this.URL+"/"+id);
  }
  URL:string = "http://localhost:8000/categoria"
  constructor(private http:HttpClient) { 
  
  }
  obtenerCategorias():Observable<Categoria[]>{
    return this.http.get<Categoria[]>(this.URL);
  }
  enviarData(data:any):Observable<Categoria>{
    return this.http.post<Categoria>(this.URL,data);
  }
  actualizarData(data:Categoria, id:number):Observable<Categoria>{
    return this.http.put<Categoria>(this.URL+"/"+id, data);
  }
}
