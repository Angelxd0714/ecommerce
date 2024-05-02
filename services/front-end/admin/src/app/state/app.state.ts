import { Token } from "../interfaces/token";

export interface AppState {
    auth: Token;
  }
  
  export const initialState: AppState = {
    auth: {
      access_token: null,
      exp: null,
    },
  };