import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Params, Router} from '@angular/router';
import {ClienteService} from '../cliente.service';

@Component({
  selector: 'app-cliente-detalhe',
  templateUrl: './cliente-detalhe.component.html',
  styleUrls: ['./cliente-detalhe.component.css']
})
export class ClienteDetalheComponent implements OnInit {
  isExclusao = false;
  cliente: any;
  id = this.route.snapshot.params['id'];

  constructor(private service: ClienteService,
              private route: ActivatedRoute,
              private router: Router) { }

  ngOnInit(): void {
    this.service.getClienteByID(this.id)
      .subscribe(cliente => {
        console.log(cliente);
        this.cliente = cliente;
      });
    this.route.params
      .subscribe((params: Params) => {
        this.id = params['id'];
        this.service.getClienteByID(this.id)
      .subscribe(cliente => {
        this.cliente = cliente;
      });
      });
  }

  onDeleteCliente() {
    this.service.deleteCliente(this.id).subscribe(cliente => {
      console.log(cliente);
    });
    this.router.navigate(['clientes']);
  }

  onEditCliente() {
    this.router.navigate(['clientes', 'edit', this.id]);
  }

  onPerguntar() {
    this.isExclusao = true;
  }

  onRetornar() {
    this.isExclusao = false;
  }
}
