import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ImovelService} from '../imovel.service';
import { CategoriaService } from '../../shared/services/categoria.service';
import { ProprietarioService } from '../../proprietario/proprietario.service';


@Component({
  selector: 'app-imovel-novo',
  templateUrl: './imovel-novo.component.html',
  styleUrls: ['./imovel-novo.component.css']
})
export class ImovelNovoComponent implements OnInit {
  imovelForm: any;
  lista_categoria: any;
  lista_proprietario: any;
  mensagem = '';
  mensagemErro = '';

  constructor(private serviceProprietario: ProprietarioService,
              private serviceImovel: ImovelService,
              private serviceCategoria: CategoriaService) { }

  ngOnInit(): void {
    this.imovelForm = new FormGroup({
      matricula: new FormControl(null, Validators.required),
      proprietario_id: new FormControl(),
      categoria_id: new FormControl(1),
      data_posse: new FormControl(1)
    });
    this.serviceProprietario.getProprietarios()
      .subscribe(proprietarioData => {
        this.lista_proprietario = proprietarioData;
      });
    this.serviceCategoria.getAll()
      .subscribe(categoriaData => {
        this.lista_categoria = categoriaData;
    });
  }
  onSubmit() {
    this.mensagem = '';
    this.mensagemErro = '';
    this.serviceImovel.create(this.imovelForm.value)
      .subscribe(returnData => {
      console.log(returnData);
      this.mensagem = 'Imóvel adicionado com sucesso!';
    }, error => {
        this.mensagemErro = error.name;
      }
    );
    this.imovelForm.reset();
  }

  onClearError() {
    this.mensagem = '';
    this.mensagemErro = '';
  }
}
