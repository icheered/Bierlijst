import { User } from "@/api/api";
import { Configuration } from "@/api/configuration";

export interface AppNotification {
    content: string;
    color?: string;
    showProgress?: boolean;
}

export interface MainState {
    isLoggedIn: boolean | null;
    logInError: string;
    userProfile: User | null;
    notifications: AppNotification[];
    configuration: Configuration;
}
