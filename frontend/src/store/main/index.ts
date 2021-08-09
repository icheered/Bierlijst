import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { MainState } from "./state";
import { Configuration } from "@/api/configuration";

const defaultState: MainState = {
    isLoggedIn: null,
    logInError: "",
    userProfile: null,
    notifications: [],
    configuration: new Configuration(),
};

export const mainModule = {
    state: defaultState,
    mutations,
    actions,
    getters,
};
