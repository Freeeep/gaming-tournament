import { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import { login } from '../services/auth';

function Login(){
    // State to store form inputs
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();

    // Handle form submission
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('')
        setLoading(true);

        try {
            const response = await login(email, password);

            // Save authorization to localStorage
            localStorage.setItem('token', response.access_token);

            // Redirect to home page
            navigate('/');
        } catch (err: any) {
            setError(err.response?.data?.detail || 'Login failed');
        } finally {
            setLoading(false);
        }
        
        
    }
    
    return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
                <h2 className="text-2xl font-bold text-white mb-6 text-center">
                    Login
                </h2>
                {error && (
                    <div className="bg-red-500 text-white p-3 rounded mb-4 text-center">
                    {error}
                    </div>
                )}
                <form onSubmit={handleSubmit} className="space-y-4">
                    <div>
                        <label className="block text-gray-300 mb-2">Email</label>
                        <input 
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder='Email'
                            required
                            className="w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-blue-500" 
                        />
                    </div>
                    <div>
                        <label className='block text-gray-300 mb-2'>Password</label>
                            <input 
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder='Password'
                            required
                            className="w-full px-4 py-2 bg-gray-700 text-white rounded focus:outline-none focus:ring-2 focus:ring-blue-500" 
                        />
                    </div>
                    <div>
                        <button 
                        type='submit'
                        disabled={loading} 
                        className='bg-gray-700 text-white rounded px-4 py-2 hover:outline-none hover:ring-2 hover:ring-blue-500'>
                            {loading ? 'Logging in...' : 'Login'}
                            </button>
                    </div>
                </form>

            </div>
        </div>
    )
}

export default Login;