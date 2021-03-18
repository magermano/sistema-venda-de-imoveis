import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {
  private url = 'http://127.0.0.1:5000/Categoria-de-Imóvel/';

  constructor(private http: HttpClient) { }

  getAll() {
    return this.http.get(this.url);
  }
}
