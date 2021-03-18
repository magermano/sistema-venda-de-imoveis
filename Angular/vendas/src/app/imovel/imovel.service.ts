import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { Imovel } from '../shared/imovel.model';

@Injectable({
  providedIn: 'root'
})
export class ImovelService {
  private url = 'http://127.0.0.1:5000/Imoveis/';

  constructor(private http: HttpClient) { }

  getAll() {
    return this.http.get<Imovel>(this.url);
  }

  getByID(id: number) {
    return this.http.get(this.url + id);
  }

  create(imovelData: Imovel) {
    return this.http.post(this.url, imovelData);
  }

  edit(id: number, imovelData: Imovel) {
    return this.http.patch(this.url + id, imovelData);
  }

  delete(id: number) {
    return this.http.delete(this.url + id);
  }
}
