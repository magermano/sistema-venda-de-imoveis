import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-proprietario',
  templateUrl: './proprietario.component.html',
  styleUrls: ['./proprietario.component.css']
})
export class ProprietarioComponent implements OnInit {

  constructor(private router: Router,
              private route: ActivatedRoute) {}

  ngOnInit(): void {
  }

  onNovoProprietario() {
    this.router.navigate(['novo'], {relativeTo: this.route});
  }
}
