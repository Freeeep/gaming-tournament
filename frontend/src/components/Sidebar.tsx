import { Link } from 'react-router-dom'

function Sidebar(){
return(
        <nav className='bg-gray-800 p-4 flex flex-col h-screen w-64 fixed top-0 left-0'>
            <div className='flex  px-4 justify-center'>
                <Link to='/' className='text-white text-2xl font-bold text-center'>
                    {/* <img src="/icon.png" alt="Logo" className="w-15 h-15 mr-3 object-contain" /> */}
                    Tournament Platform
                </Link>
            </div>
            <div className='mt-auto border-t border-gray-700 h-12 flex items-center'>
                <Link 
                to='/login' 
                className='text-gray-300 hover:text-white transition-colors py-2'
                >
                    Login
                </Link>
            </div>
            <div className='border-t border-b border-gray-700 h-12 flex items-center'>
                <Link
                to='/register'
                className='text-gray-300 hover:text-white transition-colors py-bottom-2'
                >
                    Register
                </Link>
            </div>

        </nav>
    );
}

export default Sidebar