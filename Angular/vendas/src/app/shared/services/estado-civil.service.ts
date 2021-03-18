import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class EstadoCivilService {
  private url = 'http://127.0.0.1:5000/Estados-Civis/';

  constructor(private http: HttpClient) { }

  getEstadoCivil() {
    return this.http.get(this.url);
  }
}
