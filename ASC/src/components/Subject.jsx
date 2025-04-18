import '../styles.css'

function Subject({ name, rank, onCheckboxChange }) {
    return (
        <div>
            <div className='border-4 border-pwred mb-2 font-semibold text-4xl flex justify-between
                            p-4'>
                <span className='w-1/3'>{name}</span>
                <span className='w-1/3 text-center'>{rank}</span>
                <input
                    type="checkbox"
                    className='my-auto ml-auto mr-8 w-10 h-10'
                    onChange={(e) => onCheckboxChange(name, e.target.checked)} />
            </div>

        </div>
    )
}

export default Subject
