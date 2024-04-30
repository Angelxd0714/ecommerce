import { Component, Inject } from '@angular/core';
import { Observable } from 'rxjs';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { CategoriaService } from '../../../services/categoria.service';
import { Categoria } from '../../../interfaces/categoria';
import { HttpClientModule } from '@angular/common/http';
import swal from 'sweetalert';
import { BrowserModule } from '@angular/platform-browser';
@Component({
  selector: 'app-categoria',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, HttpClientModule, FormsModule],
  templateUrl: './categoria.component.html',
  styleUrl: './categoria.component.css'
})
export class CategoriaComponent {

  listaCategorias: Categoria[] = [];
  titulo = "Categoria"
  busqueda = ""
  categoria = new FormGroup({
    nombre: new FormControl('', Validators.required)
  })
  constructor(private servicio$: CategoriaService) {

  }
  ngOnInit(): void {
    this.servicio$.obtenerCategorias().subscribe(data => this.listaCategorias = data)
  }
  onSubmit() {
    if (!this.categoria.invalid)
      this.servicio$.enviarData(this.categoria.value).subscribe((data: Categoria) => {
        swal("Se creo categoria con exito", {
          icon: "success"
        })
        this.categoria.reset();
      })
    else {
      swal("Error", "Complete los campos", "error");
    }
  }

  validarCampor(): boolean {
    return this.categoria.invalid;
  }
  validarCampoNombre(): boolean {
    return this.categoria.get('nombre')!.invalid;
  }
  eliminarCategoria(arg0: number | null) {
    if (arg0 == null) {
      return;
    }
    swal({
      title: "Desea eliminar la categoria?",
      icon: "warning",
      buttons: {
        cancel: true,
        confirm: true,

      },
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        this.servicio$.eliminarCategoria(arg0).subscribe(data => {
          swal("Se elimino la categoria con exito", {
            icon: "success",
            buttons: {
              cancel: true,
              confirm: true,
            },
            timer: 1500,
            title: "Categoria eliminada"
          })
        })
      }
    }).catch((e) => {
      swal("Se cancelo la eliminacion" + e, {
        icon: "error",
        buttons: {
          cancel: true,
          confirm: true,
        },
        timer: 1500
      })
    })
  }
  actualizarCategoria(arg0: number | null) {
    if (arg0 == null) {
      return;
    }
    swal({

      title: "Desea actualizar la categoria?",
      icon: "warning",
      content: {
        element: "input",
        attributes: {
          placeholder: "Ingrese el nombre",
          type: "text",
        },
      },
      buttons: {
        cancel: true,
        confirm: true,
      },
      dangerMode: true,
    }).then(nombre => {
      if (nombre) {
        const categoria: any = {
          nombre: nombre,
          id: arg0
        }
        this.servicio$.actualizarData(categoria, categoria.id).subscribe(data => {
          swal("Se actualizo la categoria con exito", {
            icon: "success",
            buttons: {
              cancel: true,
              confirm: true,
            },
            timer: 1500,
            title: "Categoria actualizada"
          })
        })
      }
      else {
        swal("Se cancelo la actualizacion", {
          icon: "error",
          buttons: {
            cancel: true,
            confirm: true,
          },
          timer: 1500
        })
      }
    }

    ).catch((e) => {
      swal("Se cancelo la actualizacion" + e, {
        icon: "error",
        buttons: {
          cancel: true,
          confirm: true,
        },
        timer: 1500
      })
    })
  }

  busquedaCategoria(): Categoria[] {
    return this.listaCategorias.filter(categoria => categoria.nombre.toLowerCase().includes(this.busqueda.toLowerCase()));
  }
}
