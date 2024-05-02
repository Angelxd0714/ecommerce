

import { initialState } from "./app.state"
import { createReducer, on } from "@ngrx/store"
import { AuthActions, getAuthToken, removeAuthToken, setAuthToken } from "./actions";
import { Token } from "../interfaces/token";




export const authReducer = (
    createReducer(
        initialState,
        on(setAuthToken, (state, { token }) => ({...state, auth: token })),
        on(removeAuthToken, (state) => ({...state, auth: { access_token: null, exp: null } })),
        on(getAuthToken, (state) => ({...state, auth: { access_token: null, exp: null } })),
    )
      
)