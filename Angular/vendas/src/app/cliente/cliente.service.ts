import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Cliente } from '../shared/cliente.model';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {
  private url = 'http://127.0.0.1:5000/Clientes/';

  constructor(private http: HttpClient) { }

  getClientes() {
    return this.http.get<Cliente>(this.url);
  }

  getClienteByID(id: number) {
    return this.http.get(this.url + id);
  }

  createCliente(clientData: Cliente) {
    return this.http.post(this.url, clientData);
  }

  editCliente(id: number, clientData: Cliente) {
    return this.http.patch(this.url + id, clientData);
  }

  deleteCliente(id: number) {
    return this.http.delete(this.url + id);
  }
}
