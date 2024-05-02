import { createAction,props } from "@ngrx/store";
import { Token } from "../interfaces/token";

export enum AuthActions {
    SET_TOKEN = '[Auth] Set Token',
    REMOVE_TOKEN = '[Auth] Remove Token',
    GET_TOKEN = '[Auth] Get Token',
  }
  
  export const setAuthToken = createAction(AuthActions.SET_TOKEN, props<{ token:Token}>());
  export const removeAuthToken = createAction(AuthActions.REMOVE_TOKEN);
  export const getAuthToken = createAction(AuthActions.GET_TOKEN)