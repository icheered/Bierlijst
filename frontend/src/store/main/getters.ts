import { MainState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
    loginError: (state: MainState) => state.logInError,
    userProfile: (state: MainState) => state.userProfile,
    dashboardShowDrawer: (state: MainState) => state.dashboardShowDrawer,

    token: (state: MainState) => state.configuration!.accessToken,
    isLoggedIn: (state: MainState) => state.isLoggedIn,
    firstNotification: (state: MainState) => state.notifications.length > 0 && state.notifications[0],
};

const { read } = getStoreAccessors<MainState, State>("");

export const readDashboardShowDrawer = read(getters.dashboardShowDrawer);
export const readIsLoggedIn = read(getters.isLoggedIn);
export const readLoginError = read(getters.loginError);
export const readToken = read(getters.token);
export const readUserProfile = read(getters.userProfile);
export const readFirstNotification = read(getters.firstNotification);
