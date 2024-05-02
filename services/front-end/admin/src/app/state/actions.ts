import { createAction,props } from "@ngrx/store";
import { Token } from "../interfaces/token";
import { user } from "../interfaces/login";

export enum AuthActions {
  INICIAR_SESION = '[Auth] Iniciar Sesión',
  INICIO_SESION_EXITOSO = '[Auth] Inicio de Sesión Exitoso',
  INICIO_SESION_FALLIDO = '[Auth] Inicio de Sesión Fallido',
}

