import { Component, OnInit } from '@angular/core';
import { ClienteService } from '../cliente.service';

@Component({
  selector: 'app-cliente-lista',
  templateUrl: './cliente-lista.component.html',
  styleUrls: ['./cliente-lista.component.css']
})
export class ClienteListaComponent implements OnInit {
  listaClientes: any;

  constructor(private service: ClienteService) { }

  ngOnInit(): void {
    this.service.getClientes()
      .subscribe(clientes => {
        this.listaClientes = clientes;
    });
  }
  onAtualizaCliente() {
    this.service.getClientes()
      .subscribe(clientes => {
        this.listaClientes = clientes;
    });
  }
}
