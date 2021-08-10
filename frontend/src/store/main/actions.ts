/* eslint-disable */
import {
    LoginApiFactory, UserApiFactory,
} from "@/api/api";
import router from "@/router";
import { getLocalToken, removeLocalToken, saveLocalToken } from "@/utils";
import { AxiosError } from "axios";
import { getStoreAccessors } from "typesafe-vuex";
import { ActionContext } from "vuex";
import { State } from "../state";
import {
    commitAddNotification,
    commitRemoveNotification,
    commitSetLoggedIn,
    commitSetLogInError,
    commitSetToken,
    commitSetUserProfile,
} from "./mutations";
import { AppNotification, MainState } from "./state";

type MainContext = ActionContext<MainState, State>;

export const actions = {
    async actionLogIn(context: MainContext, payload: { username: string; password: string; rememberme: boolean }) {
        try {
            const response = await LoginApiFactory(context.state.configuration)
                .loginAccessTokenApiLoginAccessTokenPost(payload.username, payload.password);
            const token = response.data.access_token;
            if (token) {
                if (payload.rememberme) {
                    saveLocalToken(token);
                }
                commitSetToken(context, token);
                commitSetLoggedIn(context, true);
                commitSetLogInError(context, "");
                await dispatchGetUserProfile(context);
                await dispatchRouteLoggedIn(context);
                commitAddNotification(context, { content: "Logged in", color: "success" });
            } else {
                await dispatchLogOut(context);
            }
        } catch (err) {
            if (err.response.status === 400) {
                commitSetLogInError(context, "Invalid email/username or password");
            } else if (err.response.status === 422) {
                if (payload.username === "") {
                    commitSetLogInError(context, "Please enter your username or email");
                } else if (payload.password === "") {
                    commitSetLogInError(context, "Please enter your password");
                } else {
                    commitSetLogInError(context, "Unexpected input.");
                }
            } else {
                commitSetLogInError(context, "Unknown error occured.");
            }
            await dispatchLogOut(context);
        }
    },
    async actionGetUserProfile(context: MainContext) {
        const response = await UserApiFactory(context.state.configuration).readUserMeApiUserMeGet();
        if (response.data) {
            commitSetUserProfile(context, response.data);
        }
        /*
        try {
            const response = await UsersApiFactory(context.state.configuration).readUserMeApiV1UsersMeGet();
            if (response.data) {
                commitSetUserProfile(context, response.data);
            }
        } catch (err) {
            throw err;
        }
        */
    },
    async actionUpdateUserProfile(context: MainContext, payload: any) {
        try {
            const loadingNotification = { content: "saving", showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                UserApiFactory(context.state.configuration).updateUserMeApiUserMePut(payload),
                await new Promise((resolve) => setTimeout(() => resolve(true), 500)),
            ]))[0];
            commitSetUserProfile(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: "Profile successfully updated", color: "success" });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCheckLoggedIn(context: MainContext) {
        if (!context.state.isLoggedIn) {
            let token = context.state.configuration?.accessToken;
            if (!token) {
                const localToken = getLocalToken();
                if (localToken) {
                    commitSetToken(context, localToken);
                    token = localToken;
                }
            }
            if (token) {
                try {
                    const response = await UserApiFactory(context.state.configuration).readUserMeApiUserMeGet();
                    commitSetLoggedIn(context, true);
                    commitSetUserProfile(context, response.data);
                } catch (error) {
                    await dispatchRemoveLogIn(context);
                }
            } else {
                await dispatchRemoveLogIn(context);
            }
        }
    },
    async actionRemoveLogIn(context: MainContext) {
        removeLocalToken();
        commitSetToken(context, "");
        commitSetLoggedIn(context, false);
    },
    async actionLogOut(context: MainContext) {
        await dispatchRemoveLogIn(context);
        await dispatchRouteLogOut(context);
    },
    async actionUserLogOut(context: MainContext) {
        await dispatchLogOut(context);
        commitAddNotification(context, { content: "Logged out", color: "success" });
    },
    actionRouteLogOut(context: MainContext) {
        if (router.currentRoute.path !== "/login") {
            router.push("/login");
        }
    },
    async actionCheckApiError(context: MainContext, payload: AxiosError) {
        if (payload.response!.status === 401) {
            await dispatchLogOut(context);
        } else {
            const err: string = `${payload.response?.status} - ${payload.response?.statusText}: ${payload.response?.data.detail}`;
            commitAddNotification(context, { content: err, color: "error" });
        }
    },
    actionRouteLoggedIn(context: MainContext) {
        if (router.currentRoute.path === "/login" || router.currentRoute.path === "/") {
            router.push("/main");
        }
    },
    async removeNotification(context: MainContext, payload: { notification: AppNotification, timeout: number }) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                commitRemoveNotification(context, payload.notification);
                resolve(true);
            }, payload.timeout);
        });
    },
};

const { dispatch } = getStoreAccessors<MainState | any, State>("");

export const dispatchCheckApiError = dispatch(actions.actionCheckApiError);
export const dispatchCheckLoggedIn = dispatch(actions.actionCheckLoggedIn);
export const dispatchGetUserProfile = dispatch(actions.actionGetUserProfile);
export const dispatchLogIn = dispatch(actions.actionLogIn);
export const dispatchLogOut = dispatch(actions.actionLogOut);
export const dispatchUserLogOut = dispatch(actions.actionUserLogOut);
export const dispatchRemoveLogIn = dispatch(actions.actionRemoveLogIn);
export const dispatchRouteLoggedIn = dispatch(actions.actionRouteLoggedIn);
export const dispatchRouteLogOut = dispatch(actions.actionRouteLogOut);
export const dispatchUpdateUserProfile = dispatch(actions.actionUpdateUserProfile);
export const dispatchRemoveNotification = dispatch(actions.removeNotification);
