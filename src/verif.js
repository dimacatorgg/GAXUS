export default async function verification(){
    const data = await fetch(`http://localhost:8000/api/cockie`)
    return await data.json()
}