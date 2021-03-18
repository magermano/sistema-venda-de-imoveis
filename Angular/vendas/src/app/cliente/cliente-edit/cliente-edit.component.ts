import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { ClienteService } from '../cliente.service';
import { EstadoCivilService } from '../../shared/services/estado-civil.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'app-cliente-edit',
  templateUrl: './cliente-edit.component.html',
  styleUrls: ['./cliente-edit.component.css']
})
export class ClienteEditComponent implements OnInit {
  editForm: any;
  lista_estadocivil: any;
  mensagem = '';
  mensagemErro = '';
  cliente: Observable<any>;
  id = this.route.snapshot.params['id'];

  constructor(private serviceCliente: ClienteService,
              private serviceEcivil: EstadoCivilService,
              private route: ActivatedRoute,
              private router: Router) {
    this.cliente = new Observable();
  }

  ngOnInit(): void {
    this.editForm = new FormGroup({
      nome: new FormControl(),
      cpf: new FormControl(),
      rg: new FormControl(),
      data_nascimento: new FormControl(),
      profissao: new FormControl(),
      celular: new FormControl(),
      telefone: new FormControl(),
      email: new FormControl(),
      estado_civil_id: new FormControl()
    });
    this.cliente = this.serviceCliente.getClienteByID(this.id)
      .pipe(tap(cliente => this.editForm.patchValue(cliente)));
    this.serviceEcivil.getEstadoCivil()
      .subscribe(estadoCivilData => {
        this.lista_estadocivil = estadoCivilData;
      });
  }
  onSubmit() {
    this.mensagem = '';
    this.mensagemErro = '';
    this.serviceCliente.editCliente(this.id, this.editForm.value)
      .subscribe(returnData => {
      console.log(returnData);
      this.mensagem = 'Cliente editado com sucesso!';
    }, error => {
        this.mensagemErro = error.name;
      }
    );
  }

  onClearError() {
    this.mensagem = '';
    this.mensagemErro = '';
  }
}
