import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Imovel} from '../shared/imovel.model';

@Injectable({
  providedIn: 'root'
})
export class EnderecoService {
  private url = 'http://127.0.0.1:5000/Imoveis/';

  constructor(private http: HttpClient) { }

  getImoveis() {
    return this.http.get<Imovel>(this.url);
  }

  getImovelByID(id: number) {
    return this.http.get(this.url + id);
  }

  createImovel(imovelData: Imovel) {
    return this.http.post(this.url, imovelData);
  }

  editImovel(id: number, imovelData: Imovel) {
    return this.http.patch(this.url + id, imovelData);
  }

  deleteImovel(id: number) {
    return this.http.delete(this.url + id);
  }
}
