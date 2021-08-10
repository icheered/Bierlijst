import { User } from "@/api/api";
import { MainState, AppNotification } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";


export const mutations = {
    setToken(state: MainState, payload: string) {
        state.configuration!.accessToken = payload;
    },
    setLoggedIn(state: MainState, payload: boolean) {
        state.isLoggedIn = payload;
    },
    setLogInError(state: MainState, payload: string) {
        state.logInError = payload;
    },
    setUserProfile(state: MainState, payload: User) {
        state.userProfile = payload;
    },
    addNotification(state: MainState, payload: AppNotification) {
        state.notifications.push(payload);
    },
    removeNotification(state: MainState, payload: AppNotification) {
        state.notifications = state.notifications.filter((notification) => notification !== payload);
    },
    setDashboardShowDrawer(state: MainState, payload: boolean) {
        state.dashboardShowDrawer = payload;
    },
};

const { commit } = getStoreAccessors<MainState | any, State>("");

export const commitSetLoggedIn = commit(mutations.setLoggedIn);
export const commitSetLogInError = commit(mutations.setLogInError);
export const commitSetToken = commit(mutations.setToken);
export const commitSetUserProfile = commit(mutations.setUserProfile);
export const commitAddNotification = commit(mutations.addNotification);
export const commitRemoveNotification = commit(mutations.removeNotification);
export const commitSetDashboardShowDrawer = commit(mutations.setDashboardShowDrawer);

