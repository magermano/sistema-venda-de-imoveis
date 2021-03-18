import { Component, OnInit } from '@angular/core';
import {FormGroup, FormControl, Validators} from '@angular/forms';
import {ClienteService} from '../cliente.service';
import {EstadoCivilService} from '../../shared/services/estado-civil.service';

@Component({
  selector: 'app-cliente-novo',
  templateUrl: './cliente-novo.component.html',
  styleUrls: ['./cliente-novo.component.css']
})
export class ClienteNovoComponent implements OnInit {
  clienteForm: any;
  lista_estadocivil: any;
  mensagem = '';
  mensagemErro = '';

  constructor(private serviceCliente: ClienteService,
              private serviceEcivil: EstadoCivilService) { }

  ngOnInit(): void {
    this.clienteForm = new FormGroup({
      nome: new FormControl(null, Validators.required),
      cpf: new FormControl(null, Validators.required),
      rg: new FormControl(null, Validators.required),
      data_nascimento: new FormControl(null, Validators.required),
      profissao: new FormControl(null, Validators.required),
      celular: new FormControl(null, Validators.required),
      telefone: new FormControl(null),
      email: new FormControl(null, [Validators.required, Validators.email]),
      estado_civil_id: new FormControl(1)
    });
    this.serviceEcivil.getEstadoCivil()
      .subscribe(estadoCivilData => {
        this.lista_estadocivil = estadoCivilData;
      });
  }

  onSubmit() {
    this.mensagem = '';
    this.mensagemErro = '';
    this.serviceCliente.createCliente(this.clienteForm.value)
      .subscribe(returnData => {
      console.log(returnData);
      this.mensagem = 'Cliente adicionado com sucesso!';
    }, error => {
        this.mensagemErro = error.name;
      }
    );
    this.clienteForm.reset();
  }

  onClearError() {
    this.mensagem = '';
    this.mensagemErro = '';
  }
}
