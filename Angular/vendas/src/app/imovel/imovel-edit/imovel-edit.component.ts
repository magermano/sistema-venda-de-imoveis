import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { ImovelService } from '../imovel.service';
import { CategoriaService } from '../../shared/services/categoria.service';
import { ProprietarioService } from '../../proprietario/proprietario.service';

@Component({
  selector: 'app-imovel-edit',
  templateUrl: './imovel-edit.component.html',
  styleUrls: ['./imovel-edit.component.css']
})
export class ImovelEditComponent implements OnInit {
  editForm: any;
  lista_categoria: any;
  lista_proprietario: any;
  mensagem = '';
  mensagemErro = '';
  imovel: Observable<any>;
  id = this.route.snapshot.params.id;

  constructor(private serviceImovel: ImovelService,
              private serviceCategoria: CategoriaService,
              private serviceProprietario: ProprietarioService,
              private route: ActivatedRoute) {
    this.imovel = new Observable();
  }

  ngOnInit(): void {
    this.editForm = new FormGroup({
      matricula: new FormControl(),
      proprietario_id: new FormControl(),
      categoria_id: new FormControl(),
      data_posse: new FormControl()
    });
    this.serviceProprietario.getProprietarios()
      .subscribe(proprietarioData => {
        this.lista_proprietario = proprietarioData;
    });
    this.serviceCategoria.getAll()
      .subscribe(categoriaData => {
        this.lista_categoria = categoriaData;
    });
    this.imovel = this.serviceImovel.getByID(this.id)
      .pipe(tap(imovel => this.editForm.patchValue(imovel)));
  }

  onSubmit() {
    this.mensagem = '';
    this.mensagemErro = '';
    this.serviceImovel.edit(this.id, this.editForm.value)
      .subscribe(returnData => {
      console.log(returnData);
      this.mensagem = 'Imóvel editado com sucesso!';
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
