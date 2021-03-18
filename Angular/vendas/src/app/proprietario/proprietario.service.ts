import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Proprietario} from '../shared/proprietario.model';


@Injectable({
  providedIn: 'root'
})
export class ProprietarioService {
  private url = 'http://127.0.0.1:5000/Proprietarios/';

  constructor(private http: HttpClient) { }

  getProprietarios() {
    return this.http.get<Proprietario>(this.url);
  }

  getProprietarioByID(id: number) {
    return this.http.get(this.url + id);
  }

  createProprietario(proprietarioData: Proprietario) {
    return this.http.post(this.url, proprietarioData);
  }

  editProprietario(id: number, proprietarioData: Proprietario) {
    return this.http.patch(this.url + id, proprietarioData);
  }

  deleteProprietario(id: number) {
    return this.http.delete(this.url + id);
  }
}
