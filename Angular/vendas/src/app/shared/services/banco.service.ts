import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BancoService {
  private url = 'http://127.0.0.1:5000/Bancos/';

  constructor(private http: HttpClient) { }

  getBancos() {
    return this.http.get(this.url);
  }

  getBancoByName(id: number) {
    return this.http.get(this.url + id);
  }

  createBanco(banco: any) {
    return this.http.post(this.url, banco);
  }

  editBanco(id: number, banco: any) {
    return this.http.patch(this.url + id, banco);
  }

  deleteBanco(id: number) {
    return this.http.delete(this.url + id);
  }

}
