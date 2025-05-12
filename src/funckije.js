export default async function register(name,gmail,password){
   /* const res = await fetch(`https://localhost:8000/api/register/?name=${name}&?gmail=${gmail}&?password=${password}`)
    const data = await res.json()
    return data;*/
    var res = await fetch(`https://localhost:8000/api/ses/?name=${name}`)
    return await res.json();
   
}
