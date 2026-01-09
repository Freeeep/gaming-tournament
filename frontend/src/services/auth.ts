import api from "./api";

interface LoginData{
    username: string;
    password: string;
}

interface RegisterData{
    email: string;
    display_name: string;
    password: string;
}

interface AuthResponse{
    access_token: string;
    token_type: string;
}

// Login function
export async function login(email: string, password: string): Promise<AuthResponse>{
    // Backend expect form data, not JSON for login
    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);

    const response = await api.post('/auth/login', formData, {
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    });
    return response.data;
}

// Regsiter Function
export async function register(email: string, displayName: string, password: string){
    const response = await api.post('/auth/register',{
        email,
        display_name: displayName,
        password,
    });
    return response.data;
}
    
