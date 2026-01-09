import { Link } from 'react-router-dom'

function Navbar(){
    return(
        <nav className='bg-gray-800 p-4 fixed top-0 left-0 w-full z-50'>
            <div className='flex justify-between items-center w-full px-4'>
                <Link to='/' className='text-white text-2xl font-bold flex items-center'>
                    <img src="/icon.png" alt="Logo" className="w-15 h-15 mr-3 object-contain" />
                    Tournament Platform
                </Link>
                <div className='space-x-4 flex items-center'>
                    <Link 
                    to='/login' 
                    className='text-gray-300 hover:text-white transition-colors'
                    >
                        Login
                    </Link>
                    <span className='text-gray-500'>|</span>
                    <Link
                    to='/register'
                    className='text-gray-300 hover:text-white transition-colors'
                    >
                        Register
                    </Link>
                </div>
            </div>

        </nav>
    );
}

export default Navbar;